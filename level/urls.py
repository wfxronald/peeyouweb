from django.urls import path
from . import views

urlpatterns = [
	path("<int:level>", views.level_detail, name="level_detail"),
	path("<int:level>/", views.level_detail, name="level_detail")
]