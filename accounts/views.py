from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.db import connection
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
class UserProfileRegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        city = request.data.get("city")
        age = request.data.get("age")
        interests = request.data.get("interests")
        bio = request.data.get("bio")

        # Create the user
        user = User(username=username, email=email, password=make_password(password))
        user.save()

        # Insert into UserProfile using raw SQL
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO user_profile (user_id, city, age, interests, bio)
                VALUES (%s, %s, %s, %s, %s)
                """,
                [user.id, city, age, interests, bio]
            )

        return Response({"username": username}, status=status.HTTP_201_CREATED)

class AllUsersView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT u.username, u.email, p.city, p.age, p.interests, p.bio
                FROM auth_user u
                JOIN user_profile p ON u.id = p.user_id
                """
            )
            rows = cursor.fetchall()

        user_data = []
        for row in rows:
            user_data.append({
                "username": row[0],
                "email": row[1],
                "city": row[2],
                "age": row[3],
                "interests": row[4],
                "bio": row[5],
            })

        return Response(user_data)
def home(request):
    return render(request, 'accounts/home.html')

def dashboard(request):
    all_users_view = AllUsersView()
    user_data = all_users_view.get({})
    return render(request, 'accounts/dashboard.html', {'data': user_data})
