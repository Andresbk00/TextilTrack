from pathlib import Path

# 📂 BASE_DIR: ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔒 Seguridad básica
SECRET_KEY = 'django-insecure-1234567890-camilo-reemplazar-esto-si-es-produccion'
DEBUG = True
ALLOWED_HOSTS = []

# 📦 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps personalizadas
    'usuarios',
    'inventario',
]

# ⚙️ Middleware (necesarios para sesiones, auth, etc)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Configuración raíz de URL
ROOT_URLCONF = 'textiltrack.urls'

# 🧱 Templates (necesarios para el admin y tus vistas HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'usuarios' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ⚙️ WSGI
WSGI_APPLICATION = 'textiltrack.wsgi.application'

# 🗃️ Base de datos SQLite (simple y lista para usar)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔑 Validaciones de contraseña (por defecto)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌎 Idioma y zona horaria
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# 🧾 Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'usuarios' / 'static']

# 🔧 Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuarios.Usuario'

# 🪪 Redirecciones tras login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# ✅ ID por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
