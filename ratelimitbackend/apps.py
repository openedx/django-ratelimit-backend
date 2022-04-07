from django.contrib.admin.apps import AdminConfig

class RateLimitBackendConfig(AdminConfig):
    default_site = 'ratelimitbackend.admin.RateLimitAdminSite'
