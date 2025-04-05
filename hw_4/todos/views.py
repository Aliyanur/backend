from unicodedata import category

from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from .forms import TodoCreationForm, TodoListForm, EditProductForm


def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        return render(request, 'index2.html', {'todos': todos})
    elif request.method == 'POST':
        form = TodoCreationForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get('category')

            if category is None:
                return render(request, 'index2.html', {
                    'todos': Todo.objects.all(),
                    'form': form,
                })

            category_id = category.id

            if not Category.objects.filter(id=category_id).exists():
                return render(request, 'index2.html', {
                    'todos': Todo.objects.all(),
                    'form': form,
                    'error': 'Category does not exist!'
                })

            form.save()
            return redirect('/todos/')
        else:
            todos = Todo.objects.all()
            return render(request, 'index2.html', {'todos': todos, 'form': form})


def get_student(request, pk):
    w = Todo.objects.get(id=pk)
    return render(request, 'pruduct-details.html', {'todo': w})


def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist as e:
        todos = Todo.objects.all()
        form = TodoCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form, 'error': 'Todo does not exist'})

def edit_todo(request, pk):
    categories= Category.objects.all()
    if request.method == 'GET':
        todo = get_object_or_404(Todo, id=pk)
        category_id=todo.category.id
        form = EditProductForm(instance=todo)
        return render(request, 'edit_todo.html', {'todo': todo, 'form': form, 'category_id':category_id, 'categories':categories})

    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=pk)
        form = EditProductForm(request.POST, instance=todo)
        if form.is_valid():
            todo.title = form.cleaned_data.get('title')
            todo.description = form.cleaned_data.get('description')
            todo.due_date = form.cleaned_data.get('due_date')
            todo.status = request.POST.get('status') == 'on'
            todo.save()
            return redirect('edit_todo', pk=todo.id)
        else:
            return render(request, 'edit_todo.html', {'todo': todo, 'form': form, 'error': 'Something went wrong'})

def get_todo_lists_list(request):
    if request.method=='GET':
        categories = Category.objects.all()
        form = TodoListForm()
        return render(request, 'categories.html', {'form': form, 'categories': categories})
    if request.method=='POST':
        categories = Category.objects.all()
        form = TodoListForm(request.POST)
        if form.is_valid():
            category = Category(title=form.data.get('title'))
            category.save()
            return redirect(to='categories_list_page')
        else:
            return render(request, 'categories.html', {'form': form, 'categories': categories, 'error':'SOMETHING WENT WRONG'}, )




def get_todo_list_todos(request, pk):
    if request.method=='GET':
        category = Category.objects.get(id=pk)
        todos = Todo.objects.filter(category_id=category.id)
        form=TodoCreationForm()
        return render(request, 'category-todos.html', {'todos': todos, 'category': category, 'form':form})
    if request.method=='POST':
        category = Category.objects.get(id=pk)
        form=TodoCreationForm(request.POST)
        if form.is_valid():
            title= form.data.get('title')
            description = form.data.get('description')
            status = request.POST.get('status') == 'on'
            category_id = category.id
            due_date = form.data.get('due_date')
            if not due_date:
                todos = Todo.objects.filter(category_id=category.id)
                return render(request, 'category-todos.html', {
                    'todos': todos,
                    'category': category,
                    'form': form,
                    'error': 'Due date is required!'
                })
            new_todo=Todo(title=title, description=description, status=status, category_id=category_id, due_date=due_date)
            new_todo.save()
            return redirect(to='category_todo_list', pk=category_id)
        else:
            return render(request, 'category-todos.html', {'todos': todos, 'category': category, 'form': form, 'error':'ERROR!'})






def edit_todo_list(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'GET':
        form = TodoListForm(data={'title': category.title})
        return render(request, 'edit-category.html', {'form': form, 'category':category})
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            category.title=form.data.get('title')
            category.save()
            return redirect(to='categories_list_page')
        else:
            return render(request, 'edit-category.html',{'form': form, 'category':category, 'error': 'SOMETHING WENT WRONG'}, )



def delete_todo_list(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
        return redirect(to='categories_list_page')
    except Category.DoesNotExist as e:
        categories = Category.objects.all()
        form = TodoListForm()
        return render(request, 'categories.html', {'categories': categories, 'form': form, 'error': 'Todo does not exist'})




