function showPopUp(popUp, x, y) {
    popUp.style.display = 'flex';
    popUp.style.top = y + 'px';
    popUp.style.left = x + 'px';
}

function hidePopUp(popUp) {
    popUp.style.display = 'none';
    popUp.style.top = 0;
    popUp.style.left = 0;
}


