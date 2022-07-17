from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from todo.models import Category, Task
from datetime import date
import logging


logger = logging.getLogger(__name__)


def get_tasks(category_slug: str, user_id: int):
    if category_slug == 'all':
        tasks = get_all_tasks(user_id)
    elif category_slug == 'important':
        tasks = get_important_tasks(user_id)
    elif category_slug == 'my_day':
        tasks = get_my_day_tasks(user_id)
    else:
        tasks = get_custom_category_tasks(category_slug, user_id)
    return tasks


def get_all_tasks(user_id: int):
    tasks = Task.objects.filter(user_id=user_id).order_by(
        'is_completed',
        '-is_important',
        '-date_created')
    logger.debug(f'getting all tasks for user_id: {user_id}')
    return tasks


def get_important_tasks(user_id: int):
    tasks = Task.objects.filter(
        user_id=user_id,
        is_important=True).order_by(
            'is_completed',
            '-is_important',
            '-date_created')

    logger.debug(f'getting all important tasks for user_id: {user_id}')
    return tasks


def get_my_day_tasks(user_id: int):
    today = date.today()
    tasks = Task.objects.filter(
        user_id=user_id,
        date_created__date=today).order_by(
            'is_completed',
            '-is_important',
            '-date_created')

    logger.debug(f'getting all myDay tasks for user_id: {user_id}')

    return tasks


def get_custom_category_tasks(category_slug: str, user_id: int):
    tasks = Task.objects.filter(
        user=User.objects.get(id=user_id),
        category=Category.objects.get(slug=category_slug)).order_by(
            'is_completed',
            '-date_created')
    logger.debug(f'getting all custom category tasks for '
        f'user_id: {user_id}, category_slug: {category_slug}')
    return tasks


def add_task(text: str, description: str, due_date: date, category_slug: str, user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        logger.error(f'User not found. '
            f'user: {user_id} category_slug: {category_slug}')
        return

    standard_categories = ['all', 'important', 'my_day']

    category = Category.objects.filter(slug=category_slug, user=user)

    if not category and category_slug not in standard_categories:
        logger.error(f'Category not found. '
            f'user: {user_id} category_slug: {category_slug}')
        return

    is_important = True if category_slug == 'important' else False

    text = text[:100]
    desc = description[:400]

    task = Task.objects.create(task=text, description=description, due_date=due_date, is_important=is_important, user=user)

    task.category.add(*category)

    logger.info(f'Task was added. '
        f'user: {user_id} category_slug: {category_slug} task_id: {task.id}')

    return task


def delete_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        logger.error(f'Task not found. task_id: {task_id}')
        return

    logger.info(f'Task was deleted. task_id: {task_id}')

    task.delete()


def finish_task(task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        logger.error(f'Task not found. task_id: {task_id}')
        return

    if task.is_completed is False:
        task.is_completed = True
        logger.info(f'Task is completed. task_id: {task_id}')
        task.save()


def remove_from_completed(task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        logger.error(f'Task not found. task_id: {task_id}')
        return
    if task.is_completed is True:
        task.is_completed = False
        logger.info(f'Task was removed from completed. task_id: {task_id}')
        task.save()


def set_task_important(task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        logger.error(f'Task not found. task_id: {task_id}')
        return

    if task.is_important is False:
        task.is_important = True
        logger.info(f'Task is set to important. task_id: {task_id}')
        task.save()


def set_task_not_important(task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        logger.error(f'Task not found. task_id: {task_id}')
        return
    if task.is_important is True:
        task.is_important = False
        logger.info(f'Task was removed from important. task_id: {task_id}')
        task.save()
