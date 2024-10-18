from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,BookingViewSet,MenuViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'bookings',BookingViewSet)
router.register(r'menu',MenuViewSet)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]