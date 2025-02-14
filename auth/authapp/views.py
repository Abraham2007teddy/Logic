from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import UserCheckSerializer, UserProfileSerializer
from .models import UserProfile
from rest_framework import viewsets

# UserProfile ViewSet (for user profile data)
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Check if user exists by username and password
@api_view(['POST'])
def check_user_exists(request):
    """
    Check if a user exists with the given username and password.
    Returns a message 'Yes' if the user exists and credentials are correct.
    Returns a message 'No' if the user does not exist or credentials are incorrect.
    """
    # Validate input with serializer
    serializer = UserCheckSerializer(data=request.data)
    
    if serializer.is_valid():
        # Extract username and password from validated data
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Try to authenticate the user
        user = authenticate(request, username=username, password=password)
        
        # Check if the user exists and the password is correct
        if user is not None:
            user_name = user.get_full_name() if user.get_full_name() else user.username
            return Response({"message": "Yes", "name": user_name}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No"}, status=status.HTTP_404_NOT_FOUND)

    # Return validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin-only user creation
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
    """
    Create a new user if the authenticated user is an admin.
    The user must provide a username and password in the request body.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create the user
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

# User login and token generation
@api_view(['POST'])
def login_user(request):
    """
    Login a user by username and password and return an authentication token.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Validate input
    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    
    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Generate or retrieve the token
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key}, status=status.HTTP_200_OK)

# User logout - invalidate token
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Logout a user by deleting their authentication token.
    """
    # Delete the authentication token
    request.user.auth_token.delete()
    
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
