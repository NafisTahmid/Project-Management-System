from django.shortcuts import render
from app_auth.forms import RegistrationForm, LoginForm, UpdateUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Tokens
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT Token Authentication
from rest_framework.authtoken.models import Token  # F
# Create your views here.
@csrf_exempt
def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
          
            return HttpResponseRedirect(reverse('app_management:home'))
    return render(request, 'app_auth/register.html', context={'form':form})

@csrf_exempt
def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                response_data = {
                    'status':'login successful'         
                }
                return HttpResponseRedirect(reverse('app_management:home'))
                # return JsonResponse(response_data)

    return render(request, 'app_auth/login.html', context={'form':form})

@login_required
@csrf_exempt
def update_user(request, pk):
    user_object = User.objects.get(pk=pk)

    form = UpdateUserForm(instance=user_object)
    if request.method == 'POST':
        form = UpdateUserForm(data = request.POST, instance=user_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_auth:update_user', kwargs={'pk':pk}))
    return render(request, 'app_auth/update_user.html', context={'form':form})


@login_required
@csrf_exempt
def user_details(request, pk):
    user_object = User.objects.get(pk=pk)
    return render(request, 'app_auth/user_profile.html', context={'user_object':user_object})


@login_required
@csrf_exempt
def delete_user(request, pk):
    user_object = get_object_or_404(User, pk=pk)
    user_object.delete()
    return HttpResponseRedirect(reverse('app_auth:login'))


@login_required
@csrf_exempt
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_auth:login'))

@login_required
@csrf_exempt
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return HttpResponseRedirect(reverse('app_auth:login'))

    return render(request, 'App_auth/change_password.html', {'form':form})
