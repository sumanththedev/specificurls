from app.views import*
from django.urls import path
app_name="anything"
urlpatterns = [
    path('pirate/',pirate,name='pirate'),
]