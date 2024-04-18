// Открытие окон
// Попап поступления
const symbolNew = document.querySelector(".symbol-new");
const btnAdmission = document.querySelector(".btn-admission");
const btnExitAdmission = document.querySelector(".btn__exit-admission");
const popupAdmission = document.querySelector(".popup-admission");

document.addEventListener("DOMContentLoaded", () => {
  if (symbolNew) {
    symbolNew.addEventListener("click", () => {
      popupAdmission.classList.add("active__popup-history");
    });
  }
  
  if (btnAdmission) {
    btnAdmission.addEventListener("click", () => {
      popupAdmission.classList.add("active__popup-history");
    });
  }
  
  if (btnExitAdmission) {
    btnExitAdmission.addEventListener("click", () => {
      popupAdmission.classList.remove("active__popup-history");
    });
  }
  
});

// Попап изменения счета
const pageContentCheckBlockInfoBtn = document.querySelector(
  ".page-content__check__block-info-btn"
);
const popupCheckBtnExit = document.querySelector(".popup__check__btn-exit");
const popupCheck = document.querySelector(".popup__check");
if (pageContentCheckBlockInfoBtn) {
  pageContentCheckBlockInfoBtn.addEventListener("click", () => {
    popupCheck.classList.add("popup__check-active");
  });

  popupCheckBtnExit.addEventListener("click", () => {
    popupCheck.classList.remove("popup__check-active");
  });
}
// Попап покупки
const popupPurchase = document.querySelector(".popup-purchase");
const btnPurchase = document.querySelector(".btn-purchase");
const btnExitPurchase = document.querySelector(".btn__exit-purchase");

if (btnPurchase) {
  btnPurchase.addEventListener("click", () => {
    popupPurchase.classList.add("active__popup-history");
  });
}

if (btnExitPurchase) {
  btnExitPurchase.addEventListener("click", () => {
    popupPurchase.classList.remove("active__popup-history");
  });
}


// Попап продажи
const popupSale = document.querySelector(".popup-sale");
const btnSale = document.querySelector(".btn-sale");
const btnExitSale = document.querySelector(".btn__exit-sale");

if (btnSale) {
  btnSale.addEventListener("click", () => {
    popupSale.classList.add("active__popup-history");
  });

}

if (btnExitSale) {
  btnExitSale.addEventListener("click", () => {
    popupSale.classList.remove("active__popup-history");
  });
}


// Попап оплаты
const popupPayment = document.querySelector(".popup-payment");
const btnPayment = document.querySelector(".btn-payment");
const btnExitPayment = document.querySelector(".btn__exit-payment");

if (btnPayment) {
  btnPayment.addEventListener("click", () => {
    popupPayment.classList.add("active__popup-history");
  });
}


if (btnExitPayment) {
  btnExitPayment.addEventListener("click", () => {
    popupPayment.classList.remove("active__popup-history");
  });
}


// Попап возврат
const popupReturnPay = document.querySelector(".popup-return-pay");
const btnReturnPay = document.querySelector(".btn-return-pay");
const btnExitReturnPay = document.querySelector(".btn__exit-return-pay");

if (btnReturnPay) {
  btnReturnPay.addEventListener("click", () => {
    popupReturnPay.classList.add("active__popup-history");
  });
}


if (btnExitReturnPay) {
  btnExitReturnPay.addEventListener("click", () => {
    popupReturnPay.classList.remove("active__popup-history");
  });
}


// Попап письма
const popupLetter = document.querySelector(".popup-letter");
const btnLetter = document.querySelector(".btn-letter");
const btnExitLetter = document.querySelector(".btn__exit-letter");

if (btnLetter) {
  btnLetter.addEventListener("click", () => {
    popupLetter.classList.add("active__popup-history");
  });
}


if (popupLetter) {
  btnExitLetter.addEventListener("click", () => {
    popupLetter.classList.remove("active__popup-history");
  });
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