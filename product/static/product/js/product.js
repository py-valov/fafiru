const popupStock = document.querySelector(".popup-stock");
const createCardBtn = document.querySelector(".create-card");
const exitCardBtn = document.querySelector(".btn-exit");

if (createCardBtn) {
  createCardBtn.addEventListener("click", () => {
    popupStock.classList.add("popup-active")
  })

  exitCardBtn.addEventListener("click", () => {
    popupStock.classList.remove("popup-active")
  })
}
const choiceClient = document.querySelector(".choice-client");
const choiceClientActive = document.querySelector(".popup-stock-choice-p");
const choiceClientExit = document.querySelector(".choice-client__content-exit");

if (choiceClientActive) {
  choiceClientActive.addEventListener("click", () => {
    choiceClient.classList.add("choice-client-active")
  })

  choiceClientExit.addEventListener("click", () => {
    choiceClient.classList.remove("choice-client-active")
  })
}

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


// Селект
const typeFilter = document.querySelector(".type-filter");
const searchInputProduct = document.querySelector(".search-input-product");
const searchSelectProduct = document.querySelector(".search-select-product");
const filterProductInput = document.querySelector(".filter-product-input");

const productsLink = '/api/v1/productslist/';

searchSelectProduct.style.display = "None"

typeFilter.addEventListener("click", () => {
  if (typeFilter.value == "Транспорт") {
    searchInputProduct.style.display = "None"
    searchSelectProduct.style.display = "Block"
  } else {
    searchInputProduct.style.display = "Block"
    searchSelectProduct.style.display = "None"
  }
})


// Фильтер Попап
const choiceClientContentFilterItem = document.querySelector(".choice-client__content-filter-item");
const choiceClientContentBodyItem = document.querySelectorAll(".choice-client__content-body-item");

choiceClientContentFilterItem.addEventListener("keyup", () => {
  let filter = String(choiceClientContentFilterItem.value);

  if (filter == "") {
    for (let item of choiceClientContentBodyItem) {
      item.style.display = "flex"
    }
    return
  }

  for (let item of choiceClientContentBodyItem) {
    if (item.querySelector(".choice-client__content-body-item-p").textContent.indexOf(filter) > -1) {
      console.log(item.querySelector(".choice-client__content-body-item-p").textContent)
      item.style.display = "flex"
    } else {
      item.style.display = "None"
    }
  }
})

