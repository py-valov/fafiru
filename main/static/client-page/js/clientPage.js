// Важные обращения
const pageClientAppealContentItem = document.querySelectorAll(
  ".page-client__appeal__content-item"
);

pageClientAppealContentItem.forEach((el) => {
  let status = el.querySelector(".page-client__appeal__content-item-status");

  switch (status.innerHTML.trim()) {
    case "Склад":
      el.classList.add("item-red");
      break;
    case "Счета":
      el.classList.add("item-green");
      break;
  }
});

// Открытие попапа
const pageBtn = document.querySelector(".page__btn");
const popupCreateAppeal = document.querySelector(".popup__create-appeal");
const popupCreateAppealExit = document.querySelector(
  ".popup__create-appeal__exit"
);

if (pageBtn) {
  pageBtn.addEventListener("click", () => {
    popupCreateAppeal.classList.add("popup-active");
    document.body.classList.add("ovh");
  });

  popupCreateAppealExit.addEventListener("click", () => {
    popupCreateAppeal.classList.remove("popup-active");
    document.body.classList.remove("ovh");
  });
}
// Попап изменения счета
const tableBtn = document.querySelector(".table-btn");
const popupCheckBtnExit = document.querySelector(".popup__check__btn-exit");
const popupCheck = document.querySelector(".popup__check");

if (tableBtn) {
  tableBtn.addEventListener("click", () => {
    popupCheck.classList.add("popup__check-active");
  });

  popupCheckBtnExit.addEventListener("click", () => {
    popupCheck.classList.remove("popup__check-active");
  });
}
// Проценты за перевод в попапе изменения счета
const popupSelectData = document.querySelector(".popup__select-data");
const inputOne = document.querySelector(".inputOne");
const inputTwo = document.querySelector(".inputTwo");
const inputThree = document.querySelector(".inputThree");

if (popupSelectData) {
  popupSelectData.addEventListener("change", () => {
    let selectVal = popupSelectData.value;

    switch (selectVal) {
      case "%":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputOne.classList.add("input-active");
        break;
      case "$":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputTwo.classList.add("input-active");
        break;
      case "₽":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputThree.classList.add("input-active");
        break;
      case "% + $":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputOne.classList.add("input-active");
        inputTwo.classList.add("input-active");
        break;
      case "% + ₽":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputOne.classList.add("input-active");
        inputThree.classList.add("input-active");
        break;
      case "$ + ₽":
        inputOne.classList.remove("input-active");
        inputTwo.classList.remove("input-active");
        inputThree.classList.remove("input-active");

        inputTwo.classList.add("input-active");
        inputThree.classList.add("input-active");
        break;
      case "% + $ + ₽":
        inputOne.classList.add("input-active");
        inputTwo.classList.add("input-active");
        inputThree.classList.add("input-active");
        break;
    }
  });
}

// Вывод статуса выполнения обращения
const doneAppeal = document.querySelectorAll('.done-appeal');

if (doneAppeal) {
  doneAppeal.forEach(el => {
    if (el.innerHTML == 'False') {
      el.innerHTML = "&#10008;"
    } else {
      el.innerHTML = "&#10004; &#10004; &#10004;"
      el.style.color = 'white'
    }
  })

}

// Фильт обращений
const btnAll = document.querySelector('.btn-all');
const btnTrue = document.querySelector('.btn-true');
const btnFalse = document.querySelector('.btn-false');

const cardAppeal = document.querySelectorAll('.page-client__appeal__content-item')

btnAll.addEventListener('click', () => {
  btnAll.classList.add('btn-filter__active');
  btnTrue.classList.remove('btn-filter__active');
  btnFalse.classList.remove('btn-filter__active');

  cardAppeal.forEach(el => {
    el.classList.remove('card-appeal-deactive')
  })
})

btnTrue.addEventListener('click', () => {
  
  btnAll.classList.remove('btn-filter__active');
  btnTrue.classList.add('btn-filter__active');
  btnFalse.classList.remove('btn-filter__active');

  cardAppeal.forEach(el => {
    elDone = el.querySelector('.done-appeal')
    if (elDone.innerHTML == '✘') {
      el.classList.add('card-appeal-deactive');
    } else {
      el.classList.remove('card-appeal-deactive')
    }
  })
})

btnFalse.addEventListener('click', () => {
  
  btnAll.classList.remove('btn-filter__active');
  btnTrue.classList.remove('btn-filter__active');
  btnFalse.classList.add('btn-filter__active');

  cardAppeal.forEach(el => {
    elDone = el.querySelector('.done-appeal')
    if (elDone.innerHTML == '✘') {
      el.classList.remove('card-appeal-deactive');
    } else {
      el.classList.add('card-appeal-deactive')
    }
  })
})

// Загрузка файлов
function upload(selector) {
  const input = document.querySelector(`.${selector}`);
  const preview = document.createElement("div");

  preview.classList.add("file-block-fileblock");

  const open = document.createElement("div");
  open.classList.add("file-block-btn");
  open.textContent = "Добавить файл";

  input.insertAdjacentElement("afterend", preview);
  input.insertAdjacentElement("afterend", open);

  const triggerInput = () => {
    input.click();
  };

  const changeHandler = (event) => {
    if (!event.target.files.length) {
      return;
    }

    const files = Array.from(event.target.files);
    const now = new Date();

    files.forEach((file) => {
      const name = file.name;

      const day = now.getDate() < 10 ? "0" + now.getDate() : now.getDate();
      const month =
        now.getMonth() < 10 ? "0" + (now.getMonth() + 1) : now.getMonth();
      const year = now.getFullYear();

      const reader = new FileReader();

      reader.addEventListener("load", (ev) => {
        preview.insertAdjacentHTML(
          "afterbegin",
          `
          <div class="file-block-fileblock__item">
            <p class="file-block-fileblock__item-name string">${name}</p>
            <p class="file-block-fileblock__item-li">${day}.${month}.${year}</p>
          </div>
          `
        );
      });

      reader.readAsDataURL(file);
    });
  };

  open.addEventListener("click", triggerInput);
  input.addEventListener("change", changeHandler);
}

const file_btn = document.querySelector(".file-btn")
if (file_btn) {
  upload("file-btn");
}

// Работа с кнопкой добавления файлов в попап

function BtnFileName() {
  const popupHistoryFile = document.querySelectorAll(".popup-history__file");

  popupHistoryFile.forEach((element) => {
    let label = element.previousElementSibling;
    let labelValue = label.innerHTML;
    
    element.addEventListener("change", (e) => {
      let fileName = element.files[0].name;
      
      if (fileName.length > 20) {
        fileName = fileName.substr(0, 20);
      }
      
      if (fileName) {
        label.innerHTML = fileName;
      } else {
        label.innerHTML = labelValue;
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", BtnFileName);