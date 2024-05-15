from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic


from accounts.forms import UserProfileForm, RegisterForm
from accounts.models import CustomUser


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def admin_redirect(request):
    return redirect('/admin')


def view_profile(request):
    return render(request, "accounts/profile.html")


def view_profile_edit(request):
    user = request.user  # Obtener el usuario actual
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Obtener los datos limpios del formulario
            cleaned_data = form.cleaned_data
            # Actualizar los campos del usuario con los nuevos valores si se proporcionan, de lo contrario, mantener los valores anteriores
            user.username = cleaned_data.get('username', user.username)
            user.first_name = cleaned_data.get('first_name', user.first_name)
            user.last_name = cleaned_data.get('last_name', user.last_name)
            user.email = cleaned_data.get('email', user.email)
            user.save()  # Guardar los cambios en el usuario
            return redirect('profile')  # Redirigir a la página de perfil
    else:
        # Si no es una solicitud POST, inicializar el formulario con los datos actuales del usuario
        initial_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        form = UserProfileForm(initial=initial_data)
    return render(request, "accounts/profile_edit.html", {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = CustomUser.objects.filter(username=username, is_active=True).first()
        if user is not None:
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("/")

        error_message = "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."
        return render(request, "registration/login.html", {"error_message": error_message})
    else:
        return render(request, "registration/login.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = response.POST.get('username')
            password = response.POST.get('password1')
            user = CustomUser.objects.filter(username=username, is_active=True).first()
            if user is not None:
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user is not None:
                    login(response, authenticated_user)
                    return redirect("/")
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "registration/signup.html", {"form": form})