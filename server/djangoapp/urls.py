# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('login', view=views.login_user, name='login'),
    path('logout', view=views.logout_user, name='logout'),
    path('register', view=views.registration, name='register'),
    path('dealer_reviews', view=views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
