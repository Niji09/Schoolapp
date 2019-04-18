from django.urls import path, re_path
from CVB import views

#namespace
app_name ='CVB'

urlpatterns = [
	path('school_list/', views.SchoolListView.as_view(), name='school_list'),
	re_path(r'school_list/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
	path('create/', views.SchoolCreateView.as_view(), name='create'),
	re_path(r'update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
	re_path(r'delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
	re_path(r'school_list/(?P<pk>\d+)/add_student/$',
		views.StudentCreateView.as_view(),
		name='add_student'
	),
	re_path(r'school_list/update_student/(?P<pk>\d+)/$',
		views.StudentUpdateView.as_view(),
		name='update_student'
	),
	re_path(r'school_list/delete_student/(?P<pk>\d+)/$',
		views.StudentDeleteView.as_view(),
		name='delete_student'
	),
]