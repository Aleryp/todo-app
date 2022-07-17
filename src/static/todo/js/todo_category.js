const popUpEditCategories = document.getElementById('edit-category-pop-up');
const hideCategoriesBtn = document.getElementById('hide-categories-btn');
const tasksTitle = document.querySelector('.tasks .title');

document.addEventListener('DOMContentLoaded', (e) => {
    highlightCurrentCategoryMenu();
    autoHideCategories();
});


hideCategoriesBtn.addEventListener('click', (e) => {
    hideCategories();
});

function hideCategories() {
    let categoriesClassList = document.querySelector('.categories').classList;
    let isHidden = categoriesClassList.contains('hidden') === true;
    categoriesClassList.toggle("hidden");
    localStorage.setItem("isCategoriesHidden", !isHidden);
}

function autoHideCategories() {
    const isCategoriesHidden = localStorage.getItem("isCategoriesHidden");
    if (isCategoriesHidden === 'true') {
        hideCategories();
    }
}

function highlightCurrentCategoryMenu() {
    let currentURL = window.location.href;

    document.querySelectorAll('.categories a').forEach(item => {
        if(currentURL.indexOf(item.getAttribute('href')) !== -1){
            item.classList.add('active');
            let name = item.getElementsByTagName('span')[0].textContent;
            tasksTitle.innerHTML = name + '<br>' + new Date().toDateString();
        }
    });
}


document.querySelectorAll('.custom-category').forEach(item => {
    item.addEventListener('contextmenu', (e) =>{
        e.preventDefault();

        showPopUp(popUp=popUpEditCategories, x=e.clientX, y=e.clientY);
        delete_btn = document.getElementById('delete-category-btn');
        delete_btn.href = item.href + 'delete_category';
        return false;
    });
});

document.addEventListener('click', (e) => {
    if (popUpEditCategories.display === 'none') {
        return;
    }

    if (!popUpEditCategories.contains(e.target)) {
        hidePopUp(popUpEditCategories);
    }
});
