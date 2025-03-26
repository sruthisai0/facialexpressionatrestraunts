from django.urls import path

from . import views

urlpatterns = [path("index.html", views.Index, name="Index"),
	       path("User.html", views.User, name="User"),
	       path("Rating", views.Rating, name="Rating"),
	       path("Admin.html", views.Admin, name="Admin"),
	       path("AdminLogin", views.AdminLogin, name="AdminLogin"),
	       path("ViewRating", views.ViewRating, name="ViewRating"),
]