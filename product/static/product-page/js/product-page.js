const popupCheck = document.querySelector(".popup-stock");
const BtnActivePopupCheck = document.querySelector(".content-card-btn");
const btnExitPopupCheck = document.querySelector(".btn-exit");

BtnActivePopupCheck.addEventListener("click", () => {
  popupCheck.classList.add("popup-active")
})

btnExitPopupCheck.addEventListener("click", () => {
  popupCheck.classList.remove("popup-active")
})

// Выбор клиента
const choiceClient = document.querySelector(".choice-client");
const choiceClientActive = document.querySelector(".popup-stock-choice-p");
const choiceClientExit = document.querySelector(".choice-client__content-exit");

choiceClientActive.addEventListener("click", () => {
  choiceClient.classList.add("choice-client-active")
})

choiceClientExit.addEventListener("click", () => {
  choiceClient.classList.remove("choice-client-active")
})

const clientItem = document.querySelectorAll(".choice-client__content-body-item");
const inputClient = document.querySelector(".input-client")
const inputClientId = document.querySelector(".input-client-id")

clientItem.forEach(el => {
  el.addEventListener("dblclick", (item) => {
    const name = item.target.querySelector(".choice-client__content-body-item-p").innerHTML
    const id = item.target.querySelector(".choice-client__content-body-item-id").value

    inputClient.value = name;
    inputClientId.value = id;

    choiceClient.classList.remove("choice-client-active")
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

upload("file-btn");


// POPUP TRANSPORT START
const blockPrices = document.querySelector(".popup-transport-price")
const ItemsNewPrice = document.querySelectorAll(".popup-transport-price-item")

const choiceClientPriceActive = document.querySelector(".input-price-check__btn");
choiceItemPrice(choiceClientPriceActive)


function choiceItemPrice (el) {
  
    el.addEventListener("click", (clickBtn) => {
      choiceClientPrice.classList.add("choice-client-price-active")

      btnItem = clickBtn
      
      const itemPrice = document.querySelectorAll(".choice-client-price__content-body-item")
      itemPrice.forEach(el => {
        el.addEventListener("dblclick", (item) => {
          let parent = btnItem.target.parentNode
          let input = parent.querySelector(".input-price-check")
          let inputId = parent.querySelector(".input-choice-price_id")

          let text = item.target.querySelector(".choice-client-price__content-body-item-p").innerHTML

          input.value = text
          inputId.value = item.target.querySelector(".choice-client-price__content-body-item-id").value
          choiceClientPrice.classList.remove("choice-client-price-active")
        })
      })

      el.addEventListener("dblclick", (item) => {
        const name = item.target.querySelector("p").innerHTML
        const id = item.target.querySelector("input").value
    
        inputTransport.value = name;
        inputTransportId.value = id;
    
        popupChoiceTransport.classList.remove("popup-choice-transport-active")
      })
    })
}

// Выбор платежа
const choiceClientPrice = document.querySelector(".choice-client-price");
const choiceClientPriceExit = document.querySelector(".choice-client-price__content-exit");

choiceClientPriceExit.addEventListener("click", () => {
  choiceClientPrice.classList.remove("choice-client-price-active")
})

// Создание транспорта
const popupCreateTransportBtnExit = document.querySelector(".popup__create-transport-btn-exit");
const createTransport = document.querySelector(".create-transport");
const popupCreateTransport = document.querySelector(".popup__create-transport");

createTransport.addEventListener("click", () => {
  popupCreateTransport.classList.add("popup__create-transport-active")
})

popupCreateTransportBtnExit.addEventListener("click", () => {
  popupCreateTransport.classList.remove("popup__create-transport-active")
})

// Попап выбора транспорта
const choiceTransport = document.querySelector(".choice-transport");
const popupChoiceTransport = document.querySelector(".popup-choice-transport");
const popupChoiceTransportContentExit = document.querySelector(".popup-choice-transport__content-exit");
const blockFilterTransport = document.querySelectorAll(".block-filter-transport");
const inputTransport = document.querySelector(".input-transport");
const inputTransportId = document.querySelector(".input-transport-id");

choiceTransport.addEventListener("click", () => {
  popupChoiceTransport.classList.add("popup-choice-transport-active")
})

popupChoiceTransportContentExit.addEventListener("click", () => {
  popupChoiceTransport.classList.remove("popup-choice-transport-active")
})

blockFilterTransport.forEach(el => {
  el.addEventListener("dblclick", (item) => {
    const name = item.target.querySelector("p").innerHTML
    const id = item.target.querySelector("input").value

    inputTransport.value = name;
    inputTransportId.value = id;

    popupChoiceTransport.classList.remove("popup-choice-transport-active")
  })
})

// Функция фильтрации
const filterPrice = document.querySelector(".filter-price");
const contentFilterPrice = document.querySelectorAll(".content-filter-price");
filterPrice.addEventListener("keyup", () => {
  filterItemPopup(filterPrice, contentFilterPrice)
})

const filterClient = document.querySelector(".filter-client");
const blockFilterClient = document.querySelectorAll(".block-filter-client");
filterClient.addEventListener("keyup", () => {
  filterItemPopup(filterClient, blockFilterClient)
})

const filterTransport = document.querySelector(".filter-transport");
filterTransport.addEventListener("keyup", () => {
  filterItemPopup(filterTransport, blockFilterTransport)
})

function filterItemPopup (input, blockItem) {
  let filter = String(input.value);

  if (filter == "") {
    for (let item of blockItem) {
      item.style.display = "flex"
    }
    return
  }

  for (let item of blockItem) {
    if (item.querySelector("p").textContent.indexOf(filter) > -1) {
      item.style.display = "flex"
    } else {
      item.style.display = "None"
    }
  }
}

const transportBtn = document.querySelector(".transport-btn");
const popupTransportExit = document.querySelector(".popup-transport-exit");
const popupTransport = document.querySelector(".popup-transport");

transportBtn.addEventListener("click", () => {
  popupTransport.classList.add("popup-transport-active")
})

popupTransportExit.addEventListener("click", () => {
  popupTransport.classList.remove("popup-transport-active")
})
// POPUP TRANSPORT END