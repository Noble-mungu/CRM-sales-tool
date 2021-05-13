from pathlib import Path
import os
import environ
from datetime import timedelta

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'django_cleanup',
    # 'social_django',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.linkedin_oauth2',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOCAL_APPS = [
    'apps.common',
    'apps.userprofile',
    'apps.linkedin',
    'apps.instagram',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ],
#
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.AllowAny',
#     ),
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }
#
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'SIGNING_KEY': os.environ['SECRET_KEY'],
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'CRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'CRM.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm',
        'USER': 'postgres',
        'PASSWORD': env.str('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = 'dashboard'

SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'

# SOCIALACCOUNT_PROVIDERS = {
#     'linkedin': {
#         'SCOPE': [
#             'r_liteprofile',
#             'r_emailaddress',
#             'w_member_social',
#         ],
#         'PROFILE_FIELDS': [
#             'id',
#             'first-name',
#             'last-name',
#             'emailAddress',
#             'email-address',
#             'picture-url',
#             'public-profile-url',
#         ],
#         'LOCATION_FIELDS': [
#             'location',
#         ],
#         'POSITION_FIELDS': [
#             'company',
#         ]
#     }
# }

# for key in [env.str('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY'),
#             env.str('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET'), ]:
#     exec("SOCIAL_AUTH_{key} = os.environ.get('{key}', '')".format(key=key))

# # Add email to requested authorizations.
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_liteprofile', 'r_emailaddress']
# # Add the fields so they will be requested from linkedin.
# SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['emailAddress']
# # Arrange to add the fields to UserSocialAuth.extra_data
# SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
#                                           ('firstName', 'first_name'),
#                                           ('lastName', 'last_name'),
#                                           ('emailAddress', 'email_address')]

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = env.str('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = env.str('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')

LINKEDIN_SECRET = env.str('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'
SOCIAL_AUTH_LOGIN_URL = '/'

# print email in console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# sending actual email to an existing email address
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sm.crm.tool@gmail.com'
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <- this line not included by default
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SITE_ID = 2

APPEND_SLASH=False
