const popUpEditTasks = document.getElementById('edit-task-pop-up');
const addTaskInput = document.querySelector('.add-task-input');
const addTaskIcon = document.getElementById('add-task-icon');


document.addEventListener('DOMContentLoaded', (e) => {
    addTaskInput.addEventListener('focus', function () {
        setUncheckedIcon(addTaskIcon);
    });
    addTaskInput.addEventListener('blur', function () {
        setAddIcon(addTaskIcon);
    });
    setAllTasksStyles();

});


document.querySelectorAll('.task-item').forEach(item => {
    addEditPopUpListener(item);
});


function addEditPopUpListener(taskItem){
    taskItem.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        const url = taskItem.getElementsByTagName('a')[0].href.replace('finish_task', '');
        showPopUp(popUp = popUpEditTasks, x = e.clientX, y = e.clientY);

        const moveToCompletedBtn = document.getElementById('move-to-completed-btn');
        moveToCompletedBtn.href = url + 'finish_task';

        const removeFromCompletedBtn = document.getElementById('remove-from-completed-btn');
        removeFromCompletedBtn.href = url + 'remove_from_completed';

        const deleteBtn = document.getElementById('delete-task-btn');
        deleteBtn.href = url + 'delete_task';

        return false;
    });
}

document.addEventListener('click', (e) => {
    if (popUpEditTasks.display === 'none') {
        return;
    }
    if (!popUpEditTasks.contains(e.target)) {
        hidePopUp(popUpEditTasks);
    }
});

function setAllTasksStyles() {
    tasks.forEach(function (item) {

        let taskId = item.pk;
        let taskText = item.fields.task;
        let isImportant = item.fields.is_important;
        let isCompleted = item.fields.is_completed;
        let task = document.getElementById(taskId);

        if (isCompleted) {
            setTaskCompleted(taskItem = task);
        }

        if (isImportant) {
            setTaskImportant(taskItem = task);
            setNotImportantHref(taskItem = task);
        }
    });
}

function setNotImportantHref(taskItem){
    const importantBtn = taskItem.querySelector('.important-btn');
    importantBtn.href = importantBtn.href.replace(
        'set_task_important',
        'set_task_not_important');

}

function setTaskCompleted(taskItem) {
    taskItem.classList.add('completed');
    icon = taskItem.getElementsByTagName('i')[0];
    setCheckedIcon(icon);
}

function setTaskUncompleted(taskItem) {
    taskItem.classList.remove('completed');
    icon = taskItem.getElementsByTagName('i')[0];
    setUncheckedIcon(icon);
}

function setTaskImportant(taskItem) {
    taskItem.classList.add('important');
    icon = taskItem.getElementsByTagName('i')[1]; // second i tag
    setImportantIcon(icon);
}

function setTaskNotImportant(taskItem) {
    taskItem.classList.remove('important');
    icon = taskItem.getElementsByTagName('i')[1]; // second i tag
    setNotImportantIcon(icon);
}

function setUncheckedIcon(elem) {
    elem.textContent = 'radio_button_unchecked';
}
function setCheckedIcon(elem) {
    elem.textContent = 'check_circle';
}
function setAddIcon(elem) {
    elem.textContent = 'control_point';
}

function setImportantIcon(elem) {
    elem.textContent = 'star';
}
function setNotImportantIcon(elem) {
    elem.textContent = 'star_border';
}
