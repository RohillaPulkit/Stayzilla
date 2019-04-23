from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views

urlpatterns = [
    path(r'', views.sign_in_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('listing/', include('listing.urls')),
]

urlpatterns += staticfiles_urlpatterns()
