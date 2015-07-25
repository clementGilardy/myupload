from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^connexion','django.contrib.auth.views.login',{'template_name':'connexion.html'}),
    url(r'^deconnexion','user.views.deconnexion'),
    url(r'^inscription','user.views.inscription')
]
