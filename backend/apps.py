from django.contrib.admin import apps as admin_apps
from django.contrib.auth import apps as auth_apps
from django.contrib.contenttypes import apps as contenttypes_apps


class MongoAdminConfig(admin_apps.AdminConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'


class MongoAuthConfig(auth_apps.AuthConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'


class MongoContentTypesConfig(contenttypes_apps.ContentTypesConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
