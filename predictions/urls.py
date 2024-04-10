from django.urls import path

from .views import predictions_view
from .views import empty_view
from .views import random_view
from .views import index_view
from .views import nested_view
from .views import depends_on_number_in_url_view
from .views import dashboard_view
from .views import writers_view
from .views import article_view



urlpatterns = [
    path('prediction/',predictions_view),
    path('', empty_view, name="MAIN_PAGE"),
    path('random/', random_view),
    path('index/', index_view, name='index'),
    path('dashbord/', dashboard_view, name='dashboard'),
    path('writers/', writers_view, name='Writers'),
    path('nested/new', nested_view),
    path('article/', article_view, name='article'),
    path('article/<int:some_number>/', depends_on_number_in_url_view, name="random_article"),
    path('article/<int:some_number>/<slug:slug_text>/', depends_on_number_in_url_view, name="random_article")
]