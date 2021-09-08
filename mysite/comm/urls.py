from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "comm"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('handleLogout', views.handleLogout, name='handleLogout'),
    path('profile', views.profile, name='profile'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('cart', views.cart, name='cart'),
    path('productPage/<int:id>/', views.productPage, name='productPage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
