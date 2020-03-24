from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('schoollist/',views.SchoolListView.as_view(),name = 'list'),
    path('schooldetail/<int:pk>/',views.SchoolDetailView.as_view(),name = 'detail'),
    path('studentlist/',views.StudentListView.as_view(),name = 'slist'),
    path('studentdetail/<int:pk>/',views.StudentDetailView.as_view(),name = 'sdetail'),
    path('createschool/',views.SchoolCreateView.as_view(),name = 'create'),
    path('createstudent/',views.StudentCreateView.as_view(),name = 'screate'),
    path('updateschool/<int:pk>/',views.SchoolUpdateView.as_view(),name = 'update'),
    path('deleteschool/<int:pk>/',views.SchoolDeleteView.as_view(),name = 'delete'),
    path('updatestudent/<int:pk>/',views.StudentUpdateView.as_view(),name = 'supdate'),
    path('deletestudent/<int:pk>/',views.StudentDeleteView.as_view(),name = 'sdelete'),
    # path('updateschool/<int:pk>/',views.SchoolUpdateView.as_view(),name = 'update'),
    # path('deleteschool/<int:pk>/',views.SchoolDeleteView.as_view(),name = 'delete'),
]
