from db_multitenant import mapper
from django.conf import settings
from django.db import connection


def get_default_db_name():
    db_name = connection.threadlocal.get_db_name()
    if db_name is None:
        db_name = settings.DATABASES['default']['NAME']
    return db_name


def extract_tenant_name(full_path):
    return full_path.strip("/").split("/")[0].lower()


class SimpleTenantMapper(mapper.TenantMapper):
    def get_tenant_name(self, request):
        return extract_tenant_name(request.get_full_path())

    def get_db_name(self, request, tenant_name):
        return f'{get_default_db_name()}_{tenant_name}'

    def get_cache_prefix(self, request, tenant_name, db_name):
        return f'{get_default_db_name()}_{tenant_name}'
