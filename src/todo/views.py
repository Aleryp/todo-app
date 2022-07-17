from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
from .services.user_auth import register_user, login_user, logout_user
from .services import todo_task, todo_category


logger = logging.getLogger(__name__)


def register_page(request):
    return register_user(request)

def login_page(request):
    return login_user(request)

def logout(request):
    return logout_user(request)


@login_required
def get_todo_page(request, category_slug:str='all'):
    user_id = request.user.id
    categories = todo_category.get_categories(user_id=user_id)
    tasks = todo_task.get_tasks(category_slug=category_slug, user_id=user_id)

    context = {
        'current_category_slug': category_slug,
        'categories': categories,
        'tasks': tasks,
    }
    return render(request, 'todo/todo.html', context)


@login_required
def redirect_to_page_all_tasks(request):
    category_slug = 'all'
    url = reverse('category', args=(category_slug,))
    return redirect(url)


@login_required
def add_new_category(request, category_slug: str):
    if request.method == 'POST':
        new_category_name = request.POST.get('new_category')
        if new_category_name is not None and new_category_name != '':
            user_id = request.user.id
            new_category = todo_category.add_new_category(
                name=new_category_name,
                user_id=user_id,)
            category_slug = new_category.slug

        url = reverse('category', args=(category_slug,))
        return redirect(url)


@login_required
def delete_category(request, category_slug: str):
    if request.method == 'GET':
        user_id = request.user.id
        todo_category.delete_category_by_slug(slug=category_slug, user_id=user_id)

    url = reverse('category', args=('all',))
    return redirect(url)


@login_required
def add_new_task(request, category_slug: str):
    if request.method == 'POST':
        new_task_text = request.POST.get('new_task_text')
        new_task_desc = request.POST.get('new_task_desc')
        new_task_date = request.POST.get('new_task_date')
        if new_task_text is not None and new_task_text != '':
            if new_task_desc is not None and new_task_desc != '':
                if new_task_date is not None and new_task_date != '':
                    user_id = request.user.id
                    new_task = todo_task.add_task(
                        text=new_task_text,
                        description=new_task_desc,
                        due_date=new_task_date,
                        category_slug=category_slug,
                        user_id=user_id,)

                url = reverse('category', args=(category_slug,))
                return redirect(url)


@login_required
def finish_task(request, category_slug: str, task_id: int):
    if request.method == 'GET':
        user_id = request.user.id
        todo_task.finish_task(task_id=task_id)

    url = reverse('category', args=(category_slug,))
    return redirect(url)


@login_required
def remove_from_completed(request, category_slug: str, task_id: int):
    if request.method == 'GET':
        user_id = request.user.id
        todo_task.remove_from_completed(task_id=task_id)

    url = reverse('category', args=(category_slug,))
    return redirect(url)


@login_required
def delete_task(request, category_slug: str, task_id: int):
    if request.method == 'GET':
        todo_task.delete_task(task_id=task_id)

    url = reverse('category', args=(category_slug,))
    return redirect(url)


@login_required
def set_task_important(request, category_slug: str, task_id: int):
    if request.method == 'GET':
        todo_task.set_task_important(task_id=task_id)

    url = reverse('category', args=(category_slug,))
    return redirect(url)


@login_required
def set_task_not_important(request, category_slug: str, task_id: int):
    if request.method == 'GET':
        todo_task.set_task_not_important(task_id=task_id)

    url = reverse('category', args=(category_slug,))
    return redirect(url)


