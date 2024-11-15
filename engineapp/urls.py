from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('categories/',views.categories_page, name='categories_page'),
    path('guides/',views.guides_page, name='guides_page'),
    path('guides/detail/<int:pk>',views.guide_detail_page, name='guide_detail_page'),
    path('sign-up/',views.sign_up_page,name='sign_up_page'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_action,name='logout_action'),
    path('categories//<int:id>/', views.categories_page, name='categories_page'),
    path('mashiny/', views.mashiny_page, name='mashiny_page'),
    path('car-detail/<int:car_id>/', views.car_detail, name='car-detail'),
    path('ads/', views.ads_list, name='ads_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)