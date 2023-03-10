"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from homeowners import homeowner
import listing
from student import students
from nonstudent import nonstudents
from auth_account import user_auth,views
from listing import listings
from rent import rents


schema_view = get_schema_view(
    openapi.Info(
        title="RENT API",
        default_version='v1',
        description="Welcome SMART TERK",
        terms_of_service="#",
        contact=openapi.Contact(email="terkpeh1990@gmail.cpm"),
        license=openapi.License(name="#"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_router = DefaultRouter()
api_router.register('homeowners',homeowner.HomeownersViewSet),
api_router.register('students',students.StudentsViewSet)
api_router.register('nonstudents',nonstudents.NonStudentsViewSet)
api_router.register('listings',listings.ListingsViewSet)
api_router.register('rents', rents.RentsViewSet)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),  

    path('docs',schema_view),
    path('admin/', admin.site.urls),
    path('',include(api_router.urls)),

    # path('all_listings',listings.all_listings,name='all_listings'),

    path('register', user_auth.RegisterView.as_view()),
    path('login', user_auth.LoginView.as_view()),
    path('user', user_auth.UserView.as_view()),
    path('logout', user_auth.LogoutView.as_view()),

   

]
