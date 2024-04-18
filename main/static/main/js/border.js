// Добавление фона для платежей
const cardStatusItems = document.querySelectorAll(".card-status__items");

cardStatusItems.forEach((el) => {
  if (el.innerHTML == "Оплачено") {
    el.parentNode.classList.add("price__border");
  }
});
