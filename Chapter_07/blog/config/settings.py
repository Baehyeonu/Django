"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@y8aoepy(nd!3!8%p+*hi_p8bcn_qh(al0^_01cv3c&5_a0n30"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",]

OWN_APPS = [
    "blog",
    "member",
            ]

THIRD_PARTY_APPS = [
    "django_extensions",
    "django_summernote",
]

INSTALLED_APPS = DJANGO_APPS + OWN_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-KR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_DIR = BASE_DIR / "static"

STATICFILES_DIRS = [
    STATIC_DIR
]

STATIC_ROOT =  BASE_DIR / '.static_root'


#media
MEDIA_URL = "madia/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# login
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

#summermote

## settings.py


# summernote
SUMMERNOTE_CONFIG = {

    # Or, you can set it to `False` to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery sources and dependencies manually.
    # Use this when you're already using Bootstrap/jQuery based themes.
    'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Use proper language setting automatically (default)
        'lang': None,

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

        # Or, explicitly set language/locale for editor
        'lang': 'ko-KR',
        

        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
    },

    # Require users to be authenticated for uploading attachments.
    'attachment_require_authentication': True,

    # You can completely disable the attachment feature.
    'disable_attachment': False,

    # Set to `False` to return attachment paths in relative URIs.
    'attachment_absolute_uri': True,

    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin

    # You can add custom css/js for SummernoteWidget.
#     'css': (
#     ),
#     'js': (
#     ),

#     # You can also add custom css/js for SummernoteInplaceWidget.
#     # !!! Be sure to put {{ form.media }} in template before initiate summernote.
#     'css_for_inplace': (
#     ),
#     'js_for_inplace': (
#     ),

#     # Codemirror as codeview
#     # If any codemirror settings are defined, it will include codemirror files automatically.
#     'css': (
#         '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
#     ),

#     # Lazy initialization
#     # If you want to initialize summernote at the bottom of page, set this as True
#     # and call `initSummernote()` on your page.
#     'lazy': True,

#     # To use external plugins,
#     # Include them within `css` and `js`.
#     'js': {
#         '/some_static_folder/summernote-ext-print.js',
#         '//somewhere_in_internet/summernote-plugin-name.js',
#     },
}