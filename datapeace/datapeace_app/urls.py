from django.urls import path, re_path
from datapeace_app import views

app_name = "datapeace"
urlpatterns = [

    path('api/users/', views.ListAddUsersDataView.as_view(), name='users'),

    re_path(r'^api/users/(?P<user_id>[\w]{1,24})/$',
            views.UserDetailEditeDeleteView.as_view(), name='user_detail'),

]