from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserInfoView

schema_view = get_schema_view(
   openapi.Info(
      title="UserInfo API",
      default_version='v1',
      description="API for managing user profiles and locations",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 🧾 Public API endpoint to list all users or create a new one (GET or POST)
    path('users/', UserInfoView.as_view(), name='user_list'),

    # 🔍 Authenticated API endpoint to get, update, or delete a specific user by primary key
    path('users/<int:pk>/', UserInfoView.as_view(), name='user_detail'),

    # 📄 Raw OpenAPI schema in JSON or YAML format (used for importing into Postman, etc.)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # 💡 Swagger UI – a beautiful interactive interface to explore and test the API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # 📘 ReDoc – alternative API documentation interface (cleaner and minimalist style)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
