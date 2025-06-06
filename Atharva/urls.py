from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('newfilm/', views.newfilm, name='newfilm'),  # Add new film page
    path('addfilm/', views.addfilm, name='addfilm'),  # Handle adding a new film
    path('filmreport/', views.filmreport, name='filmreport'),  # View films report
    path('searchgen/', views.genresearch, name='genresearch'),  # Search films by genre page
    path('langsearch/', views.langsearch, name='langsearch'),  # Search films by language page
    path('searchonlang/<str:lang>/', views.searchonlang, name='searchonlang'),  # Search films by language (with lang parameter)
    path('genresearch/', views.linkgenresearch, name='linkgenresearch'),  # Link to genre search page
    path('login/', views.login, name='login'),  # Login page
    path('del/', views.delete, name='delete'),  # Delete page (interface)
    path('delfilm/', views.delfilm, name='delfilm'),  # Delete film action
    path('ajaxgenresearch/', views.ajaxgenresearch, name='ajaxgenresearch'),  # Ajax search for genres
    path('ajaxgen/<str:gen>/', views.ajaxgen, name='ajaxgen'),  # Ajax search for specific genre
]
