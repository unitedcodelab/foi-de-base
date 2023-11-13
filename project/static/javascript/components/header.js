const sideBar = document.querySelector("#side-bar");
const openMenuButton = document.querySelector("#open-side-bar");
const closeMenuButton = document.querySelector("#close-side-bar");

openMenuButton.addEventListener("click", () => {
    sideBar.setAttribute("class", "d-flex justify-content-between offcanvas offcanvas-start show");
});

closeMenuButton.addEventListener("click", () => {
    sideBar.setAttribute("class", "offcanvas offcanvas-start hide");
});

window.addEventListener('click', (event) => {
    !(sideBar.contains(event.target) || openMenuButton.contains(event.target)) &&
        sideBar.setAttribute("class", "offcanvas offcanvas-start hide");
});