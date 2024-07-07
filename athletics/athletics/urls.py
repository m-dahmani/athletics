"""
URL configuration for athletics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
import authentication.views
import races.views

urlpatterns = [
    path("admin/", admin.site.urls),

    # path('signup/', authentication.views.SignupView.as_view(), name='signup'),
    # path('accounts/login/', authentication.views.LoginView.as_view(), name='login'),

    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),

    path('logout/', LogoutView.as_view(
        template_name='authentication/login.html'),
         name='logout'),
    path("password_change/", PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name="password_change"),

    path("password_change/done/", PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name="password_change_done",),

    path('manage_results/', races.views.manage_results, name='manage_results'),
    path('edit_result/<int:result_id>/', races.views.edit_result, name='edit_result'),
    path('races_list', races.views.races_list, name='races_list'),  # Home page displaying the Races list
    path('race_detail/<int:race_id>/', races.views.race_detail, name='race_detail'),
    path('athletes/', races.views.athlete_list, name='athlete_list'),
    path('athlete/<int:athlete_id>/', races.views.athlete_detail, name='athlete_detail'),
    path('contact/', races.views.contact, name='contact'),
    path('send_email/', races.views.send_email_view, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



