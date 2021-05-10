from django.contrib import admin
from django.urls import path, include
from apps.common import views
from apps.common.views import ProfileUpdateView, ProfileView, SignUpView, DashboardView
from apps.instagram.views import *
from apps.linkedin.views import LinkedinView, exchange_token
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'), name='logout'),

    path('register/', SignUpView.as_view(), name='register'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('linkedin/', LinkedinView.as_view(), name='linkedin'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='common/change-password.html',
        success_url='/'), name='change-password'),

    path('api/social/<str:backend>/', exchange_token),
    path('accounts/', include('allauth.urls')),
   path('instagram/', instagramView, name='instagram'),
   path('personal-profile/', personal_profile, name='personal-profile'),
   path('competitors-profile/', competitors_profile, name='competitors-profile'),
   path('post/', show_post, name='posts'),
   path('upload/', upload_pic, name='upload'),
    
    # Forgot password

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
