from django.urls import path
from .views import predictions_view
from .views import empty_view
from .views import random_view
from .views import index_view
from .views import nested_view
from .views import depends_on_number_in_url_view
urlpatterns = [
    path('prediction/',predictions_view),
     path('', empty_view),
    path('random/', random_view),
    path('index/', index_view),
    path('nested/new', nested_view),
    path('<int:some_number>', depends_on_number_in_url_view)
]