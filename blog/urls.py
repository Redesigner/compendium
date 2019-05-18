from django.urls import include, path

urlpatterns = [
    path('', include('landing.urls')),
    path('compendium', include('compendium.urls')),
    path('contact', include('contact.urls')),
    path('posts', include('posts.urls')),
]
