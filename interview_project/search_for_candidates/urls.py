from django.urls import path

from . import views

app_name = "search_for_candidates"
urlpatterns = [
    path('', views.search, name='search'),

    path('all_candidates', views.all_candidates, name='all_candidates'),

    path('add_candidate/<candidate_username>/',
         views.add_candidate, name='add_candidate'),

    path('delete_candidate/<candidate_id>/',
         views.delete_candidate, name='delete_candidate'),

    path('update_candidate_notes/<candidate_id>/',
         views.update_candidate_notes, name='update_candidate_notes'),

    path('<int:candidate_id>/', views.detail, name='detail'),
]
