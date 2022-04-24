from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'yelprestaurant', views.YelpRestaurantViewSet)
router.register(r'homeview',views.HomeViewSet, basename='HomeView')
#router.register(r'homeview',views.home_view, basename='HomeView')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home-view/', views.home_view, name='homeview'),
    path('add-restaurants/', views.add_all_restaurants_to_model, name='addrestaurants'),
    path('delete-restaurants/', views.delete_all_restaurants_in_model, name='deleterestaurants'),
    path('default-home-view/', views.home_view, name='defaulthomeview')
]