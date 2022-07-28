from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.template import TemplateDoesNotExist

from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'notes/home.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'notes/signup.html', {'form': UserCreationForm()})  # 'notes/signup.html'
    else:
        if "password" in request.POST:
            try:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                if user is None:
                    return render(request, 'notes/signup.html',
                                  {'error': "Вы ввели не верный логин или пароль,повторите попытку"})
                login(request, user)
                return redirect('home')
            except TemplateDoesNotExist:
                return render(request, 'notes/signup.html',
                              {'error': "Вы ввели не верный логин или пароль,повторите попытку"})
            except AttributeError:
                return render(request, 'notes/signup.html',
                              {'error': "Вы ввели не верный логин или пароль,повторите попытку"})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    if len(request.POST['password1']) < 8:
                        return render(request, 'notes/signup.html',
                                      {'form': UserCreationForm(),
                                       'error': "Пароль должен состоять из не менее 8 символов"})
                    else:
                        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                        user.save()
                        login(request, user)
                        return redirect('home')
                except IntegrityError:
                    return render(request, 'notes/signup.html',
                                  {'form': UserCreationForm(),
                                   'error': 'Такое имя уже существует, введите пожалуйста новое имя.'})


            else:
                return render(request, 'notes/signup.html',
                              {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')


@login_required
def currentuser(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'notes/curents.html', {'todo': todos})


@login_required
def complated(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'notes/complated.html', {'todo': todos})


@login_required
def createnotes(request):
    if request.method == 'GET':
        return render(request, 'notes/create.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('current')
        except ValueError:
            return render(request, 'notes/create.html',
                          {'form': TodoForm(), 'error': 'Слишком много информации в загаловке'})


@login_required
def todoviews(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'notes/todoviews.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current')
        except ValueError:
            return render(request, 'notes/todoviews.html',
                          {'form': TodoForm(), 'error': 'Слишком много информации в загаловке'})


@login_required
def completed(request, todo_pk):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return render(request, 'notes/complated.html', {'todo': todos, 'comp': 'Good! You was completed note!!'})


@login_required
def deleted(request, todo_pk):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return render(request, 'notes/curents.html', {'todo': todos, 'del': 'Заметка успешно удалена!'})
