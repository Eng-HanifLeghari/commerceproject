from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from commerce import views


urlpatterns = [
    path('', views.index1, name='index1'),
    path('getCategory/<int:id>/', views.index, name='category'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product', views.product, name='product'),
    # path("rate_reviews/<int:pk>/", views.rate_reviews, name="reviews"),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('checkout', views.checkout_cart, name='checkout_cart'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
