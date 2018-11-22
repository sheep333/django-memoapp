from django.urls import path

from . import views

urlpatterns = [
    path('',views.AnalyzeListView.as_view(),name='analyze_list'),
    path('detail/<int:pk>',views.AnalyzeDetailView.as_view(),name='analyze_detail'),
    path('create/',views.AnalyzeCreateView.as_view(),name='analyze_create'),
    path('update/<int:pk>',views.AnalyzeUpdateView.as_view(),name='analyze_update'),
    path('delete/<int:pk>',views.AnalyzeDeleteView.as_view(),name='analyze_delete'),
]