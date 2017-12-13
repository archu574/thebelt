from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^create$',views.create),
    url(r'^logout$', views.logout),
    url(r'^home$',views.home),
    url(r'^add$', views.add),
    url(r'^adding_to_wishlist/(?P<item_id>\d+)$', views.adding_to_wishlist),
    url(r'^removing_from_wishlist/(?P<item_id>\d+)$', views.removing_from_wishlist),
    url(r'^delete/(?P<item_id>\d+)$',views.delete),
    url(r'^showingitem/(?P<item_id>\d+)$', views.showingitem),



]
