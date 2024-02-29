from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################


def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')

def edit(request, item_id):
	item = Todo.objects.get(id=item_id)
	if request.method == "GET":
		form = TodoForm(data={'title':item.title, 'details': item.details, 'date': item.date})
		return render (request, 'todo/edit-todolist.html', {'item': item, 'form': form})
	if request.method == "POST":
		form = TodoForm(data = request.POST)
		if form.is_valid ():
			item.title = form.data.get('title', item.title)
			item.details = form.data.get('details', item.details)
			item.date = form.data.get('date', item.date)
			item.save()
			return redirect(to ='todo')