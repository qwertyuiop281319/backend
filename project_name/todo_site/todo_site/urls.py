from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name="todo"),
	path('del/<str:item_id>', views.remove, name="del"),
	path('edit/<str:item_id>',views.edit,name="edit")
]

