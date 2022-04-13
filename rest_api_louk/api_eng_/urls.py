from django.urls import include, path
from api_eng_ import views as views_api

app_name = 'api_eng_'
urlpatterns = [
    path('check_health/', views_api.index, name='index'),
    path('eval_any/', views_api.eval_any, name='eval_any'),
    path('get_list/', views_api.get_list, name='get_list'),
    path('eval_any_dev/', views_api.eval_any_dev, name='eval_any_dev'),
]