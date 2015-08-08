from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^accueil$','upload.views.home'),
    url(r'^documents/(\d+)','upload.views.documents'),
    url(r'^ajout-document','upload.views.add_folder'),
]
