const link = '/api/v1/checkslist/';

function getPost(link, pagin, ...arg) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', link);
  xhr.addEventListener('load', () => {
    const response = JSON.parse(xhr.responseText).reverse();
    pagin(response,
      arg[0],
      arg[1],
      arg[2],
      arg[3],
      arg[4],
      arg[5]);
  });

  

  xhr.addEventListener('error', () => {
    console.log('error')
  })

  xhr.send();
}

// Пагинация оплат
let pagCheck = document.querySelector(".tables-table");
let pagListCheck = document.querySelector(".tables-bottom-pag");

let notesOfPageCheck = 10;
getPost(link, 
        pagination, 
        pagCheck,
        pagListCheck,
        notesOfPageCheck,
        "pagination-li",
        "pag-client-li",
        "pag-client-deactive");

// Глобальная функция пагинации
function pagination(data, body, pagList, notesOfPage, ...selec) {
  while (pagList.firstChild) {
    pagList.removeChild(pagList.firstChild);
  }
  let pagLength = Math.ceil(data.length / notesOfPage);

  //Функция пагинации по страницам и активной страницы
  let showPage = (function () {
    let pagActive;
    return function (body, data, notesOfPage, item) {
      if (pagActive) {
        pagActive.classList.remove("pagination-li__active");
      }
      pagActive = item;
      item.classList.add("pagination-li__active");

      let pageNum = +item.innerHTML;
      let notesStart = (pageNum - 1) * notesOfPage;
      let notesEnd = notesStart + notesOfPage;

      let notes = data.slice(notesStart, notesEnd);

      body.innerHTML = "";
      for (let note of notes) {
        createCardCheck(note, body);
      }
    };
  })();

  // Функция отрисовки кнопко пагинации
  let pagBtns = (function () {
    oldLi = 0;
    return function (array, li) {
      let OldBefore;
      let NewAfter;

      if (
        li.innerHTML > 3 &&
        li.innerHTML < +array[array.length - 2].innerHTML &&
        +li.innerHTML >= oldLi
      ) {
        OldBefore = array[li.innerHTML - 3];
        OldBefore.classList.add("pag-client-deactive");

        NewAfter = array[li.innerHTML];
        NewAfter.classList.remove("pag-client-deactive");
        oldLi = +li.innerHTML;
      }

      if (+li.innerHTML < oldLi) {
        if (+li.innerHTML == 2 || +li.innerHTML == 1) {
          return;
        }
        OldBefore = array[li.innerHTML - 2];
        OldBefore.classList.remove("pag-client-deactive");

        NewAfter = array[+li.innerHTML + 1];
        NewAfter.classList.add("pag-client-deactive");
        oldLi = +li.innerHTML;
      }
    };
  })();

  //Создание кнопок при загрузке
  let createBtn = function (
    mainSelector,
    tableSelector,
    deactive,
    btnArray,
    listPagination
  ) {
    let fragmentLi = document.createDocumentFragment();
    for (let i = 1; i <= pagLength; i++) {
      let li;
      if (i <= 4) {
        li = document.createElement("li");
        li.classList.add(mainSelector, tableSelector);
        li.textContent = `${i}`;
        fragmentLi.appendChild(li);
      } else if (i == pagLength) {
        li = document.createElement("li");
        li.classList.add(mainSelector, tableSelector);
        li.textContent = pagLength;
        fragmentLi.appendChild(li);
      } else {
        li = document.createElement("li");
        li.classList.add(mainSelector, tableSelector, deactive);
        li.textContent = `${i}`;
        fragmentLi.appendChild(li);
      }

      btnArray.push(li);
    }

    listPagination.appendChild(fragmentLi);
  };

  let pagClientLis = [];
  let pagNewsLis = [];

  createBtn(selec[0], selec[1], selec[2], pagNewsLis, pagList);
  showPage(body, data, notesOfPage, pagNewsLis[0]);

  for (let li of pagNewsLis) {
    li.addEventListener("click", function (event) {
      showPage(body, data, notesOfPage, this);
      pagBtns(pagNewsLis, event.target);
    });
  }
}

// Функция создания карточек пагинации Оплат
function createCardCheck(item, perent) {
  let commission = ``;

  if (item.commissionPercent && item.commissionRUB && item.commissionUSD) {
    commission = `/ ${item.commissionPercent} + ${item.commissionUSD} * ${item.wellCommissionUSD} + ${item.commissionRUB}`
  }

  if (item.commissionPercent && item.commissionRUB) {
    commission = `/ ${item.commissionPercent} + ${item.commissionRUB}`
  }

  if (item.commissionPercent && item.commissionUSD) {
    commission = `/ ${item.commissionPercent} + ${item.commissionUSD} * ${item.wellCommissionUSD}`
  }

  if (item.commissionPercent) {
    commission = `/ ${item.commissionPercent}`
  }

  if (item.commissionUSD) {
    commission = `+ ${item.commissionUSD} * ${item.wellCommissionUSD}`
  }

  if (item.commissionRUB) {
    commission = `+ ${item.commissionRUB}`
  }

  const fragment = document.createDocumentFragment();
  let card = document.createElement("a");
  card.setAttribute("href", `payment/${item.id}`);
  card.setAttribute("target", "__blank");
  if (item.status) {
    card.classList.add("table-item", "table-item-active");
  } else {
    card.classList.add("table-item");
  }
    
  
  fragment.appendChild(card);

  let blockTop = document.createElement("div");
  blockTop.classList.add("table-item-top");
  card.appendChild(blockTop);

  block = document.createElement("div");
  block.setAttribute("title", "Дата выставления счета");
  block.classList.add("table-item-top__block");
  blockTop.appendChild(block);

  let tableP = document.createElement("p");
  tableP.classList.add("table-p", "string");
  tableP.textContent = `${item.date}`;
  block.appendChild(tableP);

  block = document.createElement("div");
  block.setAttribute("title", `Клиент: ${item.client_kod} ${item.client} - ${item.client_contract}`);
  block.classList.add("table-item-top__block");
  blockTop.appendChild(block);

  tableP = document.createElement("p");
  tableP.classList.add("table-p", "string", "table-span");
  tableP.textContent = `${item.client}`;
  block.appendChild(tableP);

  block = document.createElement("div");
  block.setAttribute("title", "Контракт");
  block.classList.add("table-item-top__block");
  blockTop.appendChild(block);

  tableP = document.createElement("p");
  tableP.classList.add("table-p", "string");
  tableP.textContent = `${item.ContractNumber}`;
  block.appendChild(tableP);

  let blockBottom = document.createElement("div");
  blockBottom.setAttribute("title", "Расчет счета");
  blockBottom.classList.add("table-item-bottom");
  card.appendChild(blockBottom);

  tableP = document.createElement("p");
  tableP.classList.add("table-p");
  blockBottom.appendChild(tableP);

  let span = document.createElement("span");
  span.classList.add("table-span", "string");
  span.textContent = `
  Оплата в ${item.currency}: 
  ${item.price}${item.wellCheck} * ${item.well} ${commission}`;
  tableP.appendChild(span);

  span = document.createElement("span");
  span.classList.add("table-span-product", "string");
  span.textContent = `Товар: ${item.product}`;
  tableP.appendChild(span);

  perent.appendChild(fragment);
}

// Фильтрация по оплатам
const cardContragent = document.querySelector('.tables-right')
const filterBtns = document.querySelectorAll(".filter-btn");

document.addEventListener("DOMContentLoaded", (e) => {
  getPost(link, response => {
      const cardBlock = document.querySelector(".tables-table");
      
      for (let btn of filterBtns) {
        btn.addEventListener("click", () => {
          while (cardBlock.firstChild) {
            cardBlock.removeChild(cardBlock.firstChild);
          }
          for (let btn of filterBtns) {
            btn.classList.remove("filter-btn-active")
          }
          
          
          switch(btn.innerHTML) {
            case "Все":
              btn.classList.add("filter-btn-active")
              getPost(link, pagination, pagCheck, pagListCheck, notesOfPageCheck, "pagination-li", "pag-client-li", "pag-client-deactive");
              break;
            case "Новые":
              btn.classList.add("filter-btn-active")
              for (let i = 0; i < response.length; i++) {
                let value = new Date(Date.now()-172800000)
                
                if (value <= new Date(response[i].date)) {
                  createCardCheck(response[i], cardBlock);
                }
              }
              break;
            case "В работе":
              btn.classList.add("filter-btn-active")
              for (let i = 0; i < response.length; i++) {
                let value = false
                
                if (value == response[i].status) {
                  createCardCheck(response[i], cardBlock);
                }
              }
              break;
            case "Долл":
              btn.classList.add("filter-btn-active")
              currencyFilter("Долл")
              break;
            case "Юа":
              btn.classList.add("filter-btn-active")
              currencyFilter("Юа")
              break;
            case "Евро":
              btn.classList.add("filter-btn-active")
              currencyFilter("Евро")
              break;
            case "Нал.юа":
              btn.classList.add("filter-btn-active")
              currencyFilter("Нал.юа")
              break;
            case "Фапьяо юа":
              btn.classList.add("filter-btn-active")
              currencyFilter("Фапьяо юа")
              break;
          }
          
        })
        
      }
      
      function currencyFilter (value) {
        for (let i = 0; i < response.length; i++) {
          let valueItem = value.toUpperCase();
          
          if (valueItem == response[i].currency.toUpperCase()) {
            createCardCheck(response[i], cardBlock);
          }
        }
      }
      
  })
});

const searchBtn = document.querySelector(".search-btn")

document.addEventListener("DOMContentLoaded", () => {
  searchBtn.addEventListener("click", (e) => {
    getPost(link, response => {
        const tableSelect = document.querySelector(".table-select").value;
        const filterInput = document.querySelector(".filter-input").value;
        const contractNumber = document.querySelector(".contractNumber").value.toUpperCase();
        
        const cardBlock = document.querySelector(".tables-table");
        while (cardBlock.firstChild) {
          cardBlock.removeChild(cardBlock.firstChild);
        }

        for (let btn of filterBtns) {
          btn.classList.remove("filter-btn-active")
        }
        if (filterInput == "" && contractNumber == "" ) {
          filterBtns[0].classList.add("filter-btn-active")
          getPost(link, 
                  pagination, 
                  pagCheck,
                  pagListCheck,
                  notesOfPageCheck,
                  "pagination-li",
                  "pag-client-li",
                  "pag-client-deactive");
          return;
        }
        
        collectionItemsFilter = []

        for (let i = 0; i < response.length; i++) {
          let itemKod = response[i].client_kod;
          let itemProduct = response[i].product;
          let itemPrice = response[i].price;
          let itemContractNumber = response[i].ContractNumber;

          switch(tableSelect) {
            case "Код клиента":
              if (contractNumber) {
                if (itemKod.toUpperCase().indexOf(filterInput.toUpperCase()) > -1 && itemContractNumber.toUpperCase().indexOf(contractNumber) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              } else {
                if (itemKod.toUpperCase().indexOf(filterInput.toUpperCase()) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              }
              break;
            case "Товар":
              if (contractNumber) {
                if (itemProduct.toUpperCase().indexOf(filterInput.toUpperCase()) > -1 && itemContractNumber.toUpperCase().indexOf(contractNumber) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              } else {
                if (itemProduct.toUpperCase().indexOf(filterInput.toUpperCase()) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              }
              break;
            case "Сумма в валюте":
              if (contractNumber) {
                if (String(itemPrice).toUpperCase().indexOf(filterInput) > -1 && itemContractNumber.toUpperCase().indexOf(contractNumber) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              } else {
                if (String(itemPrice).toUpperCase().indexOf(filterInput) > -1) {
                  createCardCheck(response[i], cardBlock);
                }
              }
              break;
          }
          
          
        }
    })
  });
}) 








