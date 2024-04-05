from django.urls import path
from lessond_drf import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get_product/', views.ListInfo.as_view()),
    path('get_product_list/', views.NewsViewSet.as_view({'get': 'list'})),
    path('get_product_category/', views.NewsViewSet.as_view({'get': 'category'})),
    path('create_product/', views.NewsViewSet.as_view({'get': 'create'})),
    path('update_product/', views.NewsViewSet.as_view({'post': 'update'})),
    path('delete_product/', views.NewsViewSet.as_view({'post': 'delete'})),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]