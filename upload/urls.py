from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^accueil$','upload.views.home'),
    url(r'^documents$','upload.views.documents')
]
