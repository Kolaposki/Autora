from django.urls import include, path
from django.contrib.auth import views as auth_views  # Use django inbuilt authentication to handle login and logout
from . import views
from django_registration.backends.one_step.views import RegistrationView
from django_registration.forms import RegistrationFormUniqueEmail

from django.conf import settings

urlpatterns = [
    path('', include("django.contrib.auth.urls")),  # for authentication purposes
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail, template_name='register.html',
                                               success_url=settings.LOGIN_REDIRECT_URL),
         name='django_registration_register'),

    path('', include('django_registration.backends.one_step.urls')),
]

