from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="accueil"),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfoliodetail, name='portfolio-details'),
    path('services/', views.services, name='services'),
    path('team', views.team, name='team'),
    path('blog/blog-details/<int:post_id>', views.blogdetails, name='blogsingle'),
    path('connexion/', views.connexion, name="connexion"),
    path('inscription/', views.signup, name="inscription"),
    path('logout/', views.deconnexion, name='logout'),
    path('new_post/', views.post, name='new_pub'),
]
