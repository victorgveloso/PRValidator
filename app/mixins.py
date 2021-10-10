import db_multitenant.middleware
from django.utils.decorators import decorator_from_middleware
from rest_framework import viewsets


class FieldsFilterMixin(viewsets.ModelViewSet):
    @decorator_from_middleware(db_multitenant.middleware.MultiTenantMiddleware)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def ignore_nested_field_access(self, r):
        return r.split("__")[0]

    def extract_fields(self, d: dict):
        field_names = [i.name for i in self.serializer_class.Meta.model._meta.get_fields() if hasattr(i, 'name')]
        return {k: v for k, v in d.items() if self.ignore_nested_field_access(k) in field_names}

    def get_queryset(self):
        return self.queryset.filter(**self.extract_fields(self.request.query_params.dict()))