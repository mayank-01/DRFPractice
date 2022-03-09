"""restfk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from api2 import views as views2
from api3 import views as views3
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('studentapi', views3.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.StudentAPI.as_view()),

    # For Function Based api_view
    # path('stuapi2/', views2.studentapi),
    # path('stuapi2/<int:id>', views2.studentapi),

    # For Class based API View
    # path('stuapi2/', views2.StudentAPI.as_view()),
    # path('stuapi2/<int:id>', views2.StudentAPI.as_view()),

    # For Generic API View and Mixins
    path('stuapi2/', views2.LCStudentAPI.as_view()),
    path('stuapi2/<int:pk>', views2.RUDStudentAPI.as_view()),

    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    #path('gettoken/', obtain_auth_token),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    
]
