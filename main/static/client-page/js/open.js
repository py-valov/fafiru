// Открытие окна главного меню
const mainMenuBtn = document.querySelector(".main-menu__btn");
const mainMenuPopup = document.querySelector(".main-menu__popup");
const popupActive = "popup-active";

document.addEventListener("DOMContentLoaded", () => {
  mainMenuBtn.addEventListener("click", () => {
    if (mainMenuPopup.classList[1] == popupActive) {
      mainMenuPopup.classList.remove(`${popupActive}`);
    } else if (mainMenuPopup.classList[1] !== popupActive) {
      mainMenuPopup.classList.add(`${popupActive}`);
    }
  });
});
