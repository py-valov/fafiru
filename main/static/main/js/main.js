// AJAX
const linkClient = '/api/v1/clientlist/'
const linkNews = '/api/v1/newslist/'
const linkOperations = '/api/v1/operationslist/'
const linkCheck = 'api/v1/nopaymentlist/'


const ContainerCheck = document.querySelector('.main-content__column-footer-table-body-card')
const CurrencyCards = document.querySelector('.main-content__column-footer-table-body-currency')

function forEachCheck (respon, activeBtn, cont) {
  let i = 1;
  let id = 0;
  for (res of respon) {
    if (activeBtn && i < 40) {
      const x = activeBtn.querySelector(".column-footer-table-body-currency-card-name").innerHTML

      for (r of res.opers) {
        if (r.name == 'Покупка' && r.typeCurrency == '¥' && x == 'Юа') {
          i++
          createCardCheck(res, cont)
        } else if (r.name == 'Покупка' && r.typeCurrency == '$' && x == 'Долл') {
          i++
          createCardCheck(res, cont)
        } else if (r.name == 'Покупка' && r.typeCurrency == '€' && x == 'Евро') {
          i++
          createCardCheck(res, cont)
        }
      }

      if (x == 'Не оплачен клиентом' && res.opers.length == 0) {
        i++
        createCardCheck(res, cont)
      }
      
    }
  } 
}


function getCheck (link, conteiner) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', link);
  xhr.addEventListener('load', () => {
    const responce = JSON.parse(xhr.responseText).reverse()
    let btnActive = CurrencyCards.querySelector(".currency-card-active")
    const btns = CurrencyCards.querySelectorAll(".column-footer-table-body-currency-card-btn") 
    forEachCheck(responce, btnActive, conteiner)

    btns.forEach((el) => {
      el.addEventListener("click", (btn) => {
        conteiner.innerHTML = " "
        btnActive.classList.remove("currency-card-active")
        btnActive = btn.target
        btnActive.classList.add("currency-card-active")

        forEachCheck(responce, btnActive, conteiner)
      })
    })

    // Фильтрация счетов
    const CheckPage = document.querySelector(".main-content__column-footer-table");

    CheckPage.addEventListener("keyup", () => {
      const input = document.querySelector(".search-input__payment");
      let filter = String(input.value.toUpperCase());
      while (ContainerCheck.firstChild) {
        ContainerCheck.removeChild(ContainerCheck.firstChild);
      }

      if (filter == "") {
        forEachCheck(responce, btnActive, conteiner)
        return;
      }

      const x = btnActive.querySelector(".column-footer-table-body-currency-card-name").innerHTML
      for (let i = 0; i < responce.length; i++) {
        let dateCheck = new Date(responce[i].date)
        let dateView = dateCheck.getDate() + '.' + (addZero(dateCheck.getMonth() + 1)) + '.' + dateCheck.getFullYear()
        function addZero(num) {
          if (num >= 0 && num <= 9) {
            return '0' + num;
          } else {
            return num;
          }
        }
        if (responce[i].currency == x) {
          let itemClient = responce[i].client;
          let itemDate = String(dateView);
          let itemPrice = String(responce[i].price);
          let itemProduct = responce[i].product;
          let itemContract = responce[i].ContractNumber;

          if (
            itemClient.toUpperCase().indexOf(filter) > -1 ||
            itemDate.indexOf(filter) > -1 ||
            itemPrice.indexOf(filter) > -1 ||
            itemProduct.toUpperCase().indexOf(filter) > -1 ||
            itemContract.toUpperCase().indexOf(filter) > -1 
          ) {
            createCardCheck(responce[i], conteiner)
          }
        }
      }
    })            
  })

  xhr.addEventListener('error', () => {
    console.log('error')
  })

  xhr.send();
}

getCheck(linkCheck, ContainerCheck);

const btnsCurrency = document.querySelectorAll(".column-footer-table-body-currency-card-btn")

function getOpirations(link, cont) {
  const xhrOper = new XMLHttpRequest();
  xhrOper.open('GET', link);
  xhrOper.addEventListener('load', () => {
    const response = JSON.parse(xhrOper.responseText)
    summUSD = 0;
    summCNY = 0;
    summEUR = 0;
    summCashCNY = 0;
    summFapiaoCNY = 0;
    for (res of response) {
      if (res.typeCurrency == "¥"){
        if (res.name == "Покупка" || res.name == "Возврат") {
          summCNY += res.admissionCurrency;
        } else if (res.name == "Оплата" || res.name == "Продажа") {
          summCNY -= res.nursingCurrency
        }
      }

      if (res.typeCurrency == "$"){
        if (res.name == "Покупка" || res.name == "Возврат") {
          summUSD += res.admissionCurrency;
        } else if (res.name == "Оплата" || res.name == "Продажа") {
          summUSD -= res.nursingCurrency
        }
      }

      if (res.typeCurrency == "€"){
        if (res.name == "Покупка" || res.name == "Возврат") {
          summEUR += res.admissionCurrency;
        } else if (res.name == "Оплата" || res.name == "Продажа") {
          summEUR -= res.nursingCurrency
        }
      }
    }

    cont.forEach(el => {
      switch(el.firstElementChild.innerHTML) {
        case "Юа":
          summ = document.createElement("p")
          summ.classList.add("column-footer-table-body-currency-card-summ")
          summ.textContent = `Сумма: ${summCNY.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}¥`
          el.appendChild(summ)
          break;
        case "Долл":
          summ = document.createElement("p")
          summ.classList.add("column-footer-table-body-currency-card-summ")
          summ.textContent = `Сумма: ${summUSD.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}$`
          el.appendChild(summ)
          break;
        case "Евро":
          summ = document.createElement("p")
          summ.classList.add("column-footer-table-body-currency-card-summ")
          summ.textContent = `Сумма: ${summEUR.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}€`
          el.appendChild(summ)
          break;
      }
    })
  });

  xhrOper.addEventListener('error', () => {
    console.log('error')
  })

  xhrOper.send();
}

getOpirations(linkOperations, btnsCurrency)

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

// Открытие окна добавления клиента/контрагента
const popupCreate = document.querySelector(".popup-create");
const popupOpen = document.querySelector(".popup_open");
const exitBtn = document.querySelector(".exit_btn");
const popupCreateActive = "popup-create__active";

if (popupOpen) {
  popupOpen.addEventListener("click", () => {
    popupCreate.classList.add(`${popupCreateActive}`);
  });

  exitBtn.addEventListener("click", () => {
    popupCreate.classList.remove(`${popupCreateActive}`);
  });
}
// Открытие окна добавления новости
const popupNewsCreate = document.querySelector(".popup-news-create");
const popupNewsOpen = document.querySelector(".popup-news__open");
const exitNewsBtn = document.querySelector(".exit-news__btn");

if (popupNewsOpen) {
  popupNewsOpen.addEventListener("click", () => {
    popupNewsCreate.classList.add(`${popupCreateActive}`);
  });

  exitNewsBtn.addEventListener("click", () => {
    popupNewsCreate.classList.remove(`${popupCreateActive}`);
  });
}
// Пагинация клиентов
let pagClient = document.querySelector(".pag-client-body");
let pagListClient = document.querySelector(".pag-list-client");
let notesOfPageClient = 5;

getPost(linkClient, 
      pagination, 
      pagClient,
      pagListClient,
      notesOfPageClient,
      "pagination-li",
      "pag-client-li",
      "pag-client-deactive");

// Пагинация новостей
let pagNews = document.querySelector(".pag-news-body");
let pagListNews = document.querySelector(".pag-list-news");

let notesOfPageNews = 5;

getPost(linkNews, 
        pagination, 
        pagNews,
        pagListNews,
        notesOfPageNews,
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
      if (body.classList[1] == "pag-news-body") {
        for (let note of notes) {
          createCardNews(note);
        }
      } else {
        for (let note of notes) {
          createCardClient(note);
        }
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

  if (body.classList == "pag-news-body") {
    createBtn(selec[0], selec[1], selec[2], pagNewsLis, pagList);
    showPage(body, data, notesOfPage, pagNewsLis[0]);

    for (let li of pagNewsLis) {
      li.addEventListener("click", function (event) {
        showPage(body, data, notesOfPage, this);
        pagBtns(pagNewsLis, event.target);
      });
    }
  } else {
    createBtn(selec[0], selec[1], selec[2], pagClientLis, pagList);
    showPage(body, data, notesOfPage, pagClientLis[0]);

    for (let li of pagClientLis) {
      li.addEventListener("click", function (event) {
        showPage(body, data, notesOfPage, this);
        pagBtns(pagClientLis, event.target);
      });
    }
  }

  //
}

// Функция создания карточек пагинации Клиентов
function createCardClient(item) {
  const fragment = document.createDocumentFragment();
  let card = document.createElement("a");
  card.setAttribute("href", `client-page/${item.id}`);
  card.classList.add("main-content__column-body-table-body-card");
  fragment.appendChild(card);

  let itemTop = document.createElement("div");
  itemTop.classList.add("card-client__items");
  card.appendChild(itemTop);

  let itemName = document.createElement("p");
  itemName.classList.add("card-client__items-info", "info-bold", "string");
  itemName.textContent = `${item.kod} ${item.name}`;
  itemTop.appendChild(itemName);

  let itemContract = document.createElement("p");
  itemContract.classList.add("card-client__items-info");
  itemContract.textContent = `Договор:${item.contract}`;
  itemTop.appendChild(itemContract);

  let itemBottom = document.createElement("div");
  itemBottom.classList.add("card-client__items");
  card.appendChild(itemBottom);

  let itemProduct = document.createElement("p");
  itemProduct.classList.add("card-client__items-info", "string");
  itemProduct.textContent = `Товар:${item.product}`;
  itemBottom.appendChild(itemProduct);

  pagClient.appendChild(fragment);
}

// Функция создания карточек пагинации Новостей
function createCardNews(item) {
  const fragment = document.createDocumentFragment();
  let card = document.createElement("div");
  card.classList.add(
    "main-content__column-body-table-body-card",
    "news-card",
    "search-news"
  );
  fragment.appendChild(card);

  let cardContent = document.createElement("div");
  cardContent.classList.add("card-news__items");
  card.appendChild(cardContent);

  let itemTop = document.createElement("div");
  itemTop.classList.add("card-news__items-block");
  cardContent.appendChild(itemTop);

  let itemStatus = document.createElement("div");
  itemStatus.classList.add("card-news__items-category");
  itemTop.appendChild(itemStatus);

  let itemStatusP = document.createElement("p");
  itemStatusP.classList.add("card-news__items-category-p");
  itemStatusP.textContent = `${item.category}`;
  itemStatus.appendChild(itemStatusP);

  let itemDate = document.createElement("div");
  itemDate.classList.add("card-news__items-date");
  itemTop.appendChild(itemDate);

  let itemDateP = document.createElement("p");
  itemDateP.classList.add("card-news__items-date-p");
  let date = new Date(item.date)
  let dateView = date.getDate() + '.' + (addZero(date.getMonth() + 1)) + '.' + date.getFullYear()
  function addZero(num) {
    if (num >= 0 && num <= 9) {
      return '0' + num;
    } else {
      return num;
    }
  }
  itemDateP.textContent = `${dateView}`;
  itemDate.appendChild(itemDateP);

  let itemBottom = document.createElement("div");
  itemBottom.classList.add("card-news__items-block");
  cardContent.appendChild(itemBottom);

  let itemCOntent = document.createElement("div");
  itemCOntent.classList.add("card-news__items-info-p");
  itemBottom.appendChild(itemCOntent);

  let itemContentP = document.createElement("p");
  itemContentP.classList.add("card-news__items-info-p", "string");
  itemContentP.textContent = `${item.content}`;
  itemCOntent.appendChild(itemContentP);

  pagNews.appendChild(fragment);

  // Добавление фона для новостей
  const cardNewsItems = document.querySelectorAll(".news-card");

  cardNewsItems.forEach((el) => {
    const category = el.querySelector(".card-news__items-category-p");

    switch (category.innerHTML) {
      case "Таможня":
        el.classList.add("news__border-customs");
        break;
      case "Важное":
        el.classList.add("news__border-error");
        break;
      case "Оповещение":
        el.classList.add("news__border-info");
        break;
    }
  });
}

const cardContragent = document.querySelector('.card-contragent')

// Созлание карточек счетов
function createCardCheck(check, container) {
  const fragment = document.createDocumentFragment();
  let card = document.createElement("a");
  card.setAttribute("href", `/finance/payment/${check.id}`);
  card.classList.add(
    "column-footer-table-body-card-item"
  );
  fragment.appendChild(card);

  let cardHead = document.createElement("div");
  cardHead.classList.add("column-footer-table-body-card-item-head")
  card.appendChild(cardHead)

  let cardHeadInfoLeft = document.createElement("div");
  cardHeadInfoLeft.classList.add("column-footer-table-body-card-item-head-info")
  cardHead.appendChild(cardHeadInfoLeft)

  let cardHeadInfoP = document.createElement("p");
  cardHeadInfoP.classList.add("column-footer-table-body-card-item-head-p", "string")
  let date = new Date(check.date)
  let dateView = date.getDate() + '.' + (addZero(date.getMonth() + 1)) + '.' + date.getFullYear()
  function addZero(num) {
	if (num >= 0 && num <= 9) {
		return '0' + num;
	} else {
		return num;
	}
}
  cardHeadInfoP.textContent = `${dateView} | ${check.client}`
  cardHeadInfoLeft.appendChild(cardHeadInfoP)

  let cardHeadInfoRigth = document.createElement("div");
  cardHeadInfoRigth.classList.add("column-footer-table-body-card-item-head-info")
  cardHead.appendChild(cardHeadInfoRigth)

  cardHeadInfoP = document.createElement("p");
  cardHeadInfoP.classList.add("column-footer-table-body-card-item-head-p")
  cardHeadInfoP.textContent = `
  ${check.client_contract} | ${StatusView(check.status)}`
  function StatusView (status) {
    if (status) {
      card.classList.add("check-card-positive")
      return "Оплачено"
    } else {
      return "Не оплачено"
    }
  }
  cardHeadInfoRigth.appendChild(cardHeadInfoP)

  let cardBody = document.createElement("div");
  cardBody.classList.add("column-footer-table-body-card-item-body")
  card.appendChild(cardBody)

  let CardBodyInfo = document.createElement("div")
  CardBodyInfo.classList.add("column-footer-table-body-card-item-body-info", "column-footer-table-body-card-item-body-info-ritgh")
  cardBody.appendChild(CardBodyInfo)

  let CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  let CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Сумма счета:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.textContent = ` ${check.price.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}${check.wellCheck}`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)
  
  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Курс счета:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.textContent = ` ${check.well}`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Комиссия:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.textContent = ` ${commissionView(check.commissionPercent, check.commissionUSD, check.commissionRUB, check.wellCommissionUSD)}`
  function commissionView (percent, usd, rub, well) {
    if (percent && usd && rub) {
      return `${percent} + ${usd}$ * ${well} + ${rub}`
    } else if (percent && usd) {
      return `${percent} + ${usd}$ * ${well}`
    } else if (percent && rub) {
      return `${percent} + ${rub}`
    } else if (usd && rub) {
      return `${usd}$ * ${well} + ${rub}`
    } else if (percent) {
      return `${percent}`
    } else if (usd) {
      return `${usd}$ * ${well}`
    } else if (rub) {
      return `${rub}`
    }
  }
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Валюта:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  let textCNY = 0;
  let textUSD = 0;
  let textEUR = 0;
  for (r of check.opers) {
    if (r.name == "Покупка" && r.typeCurrency == "¥" || r.name == "Возврат" && r.typeCurrency == "¥") {
      textCNY += r.admissionCurrency
    }
    else if (r.name == "Оплата" && r.typeCurrency == "¥") {
      textCNY -= r.nursingCurrency
    }
    else if (r.name == "Покупка" && r.typeCurrency == "$" || r.name == "Возврат" && r.typeCurrency == "$") {
      textUSD += r.admissionCurrency
    }
    else if (r.name == "Оплата" && r.typeCurrency == "$") {
      textUSD -= r.nursingCurrency
    }
    else if (r.name == "Покупка" && r.typeCurrency == "€" || r.name == "Возврат" && r.typeCurrency == "€") {
      textEUR += r.admissionCurrency
    }
    else if (r.name == "Оплата" && r.typeCurrency == "€") {
      textEUR -= r.nursingCurrency
    }
  }
  CardBodyInfoSpan.textContent = ` ${textCNY.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}¥ | ${textUSD.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}$ | ${textEUR.toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}€`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  CardBodyInfo = document.createElement("div")
  CardBodyInfo.classList.add("column-footer-table-body-card-item-body-info")
  cardBody.appendChild(CardBodyInfo)

  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Сумма счета:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.textContent = ` ${(commission(check.price, check.well, check.commissionPercent, check.commissionUSD, check.commissionRUB, check.wellCommissionUSD)).toFixed(2).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ')}₽`
  function commission (price, wellCh, percent, usd, rub, well) {
    if (percent && usd && rub) {
      return price * wellCh / percent + usd * well + rub
    } else if (percent && usd) {
      return price * wellCh / percent + usd * well
    } else if (percent && rub) {
      return price * wellCh / percent + rub
    } else if (usd && rub) {
      return price * wellCh + usd * well + rub
    } else if (percent) {
      return price * wellCh / percent
    } else if (usd) {
      return price * wellCh + usd * well
    } else if (rub) {
      return price * wellCh + rub
    } else {
      return 0,00
    }
  }
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Оплата в ${check.currency}`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  CardBodyInfoP = document.createElement("p")
  CardBodyInfoP.classList.add("column-footer-table-body-card-item-body-p")
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.classList.add("bold")
  CardBodyInfoSpan.textContent = `Контракт:`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfoSpan = document.createElement("span")
  CardBodyInfoSpan.textContent = ` ${check.ContractNumber}`
  CardBodyInfoP.appendChild(CardBodyInfoSpan)
  CardBodyInfo.appendChild(CardBodyInfoP)

  let cardFooter = document.createElement("div");
  cardFooter.classList.add("column-footer-table-body-card-item-footer")
  card.appendChild(cardFooter)

  let CardFooterInfoP = document.createElement("p")
  CardFooterInfoP.classList.add("column-footer-table-body-card-item-body-p", "string")
  CardFooterInfoP.textContent = `Товар: ${check.product}`
  cardFooter.appendChild(CardFooterInfoP)

  container.appendChild(fragment)
}



// Фильтрация по клиентам
cardContragent.addEventListener("keyup", (e) => {
  getPost(linkClient, response => {
      const input = document.querySelector(".search-input__client");
      let filter = input.value.toUpperCase();
      const cardBlock = document.querySelector(".pag-client-body");
      while (cardBlock.firstChild) {
        cardBlock.removeChild(cardBlock.firstChild);
      }

      if (filter == "") {
        getPost(linkClient, 
                pagination, 
                pagClient,
                pagListClient,
                notesOfPageClient,
                "pagination-li",
                "pag-client-li",
                "pag-client-deactive");
        return;
      }
      
      for (let i = 0; i < response.length; i++) {
        let itemName = response[i].name;
        let itemKod = response[i].kod;

        if (
          itemName.toUpperCase().indexOf(filter) > -1 ||
          itemKod.toUpperCase().indexOf(filter) > -1
        ) {
          createCardClient(response[i]);
        }
      }
  })
});


const cardNewstable = document.querySelector('.card-news')

// Фильтрация по новостям
cardNewstable.addEventListener("keyup", (e) => {
      getPost(linkNews, response => {
        const input = document.querySelector(".search-input__news");
        let filter = input.value.toUpperCase();
        const cardBlock = document.querySelector(".pag-news-body");
        while (cardBlock.firstChild) {
          cardBlock.removeChild(cardBlock.firstChild);
        }

        if (filter == "") {
          getPost(linkNews, 
                  pagination, 
                  pagNews,
                  pagListNews,
                  notesOfPageNews,
                  "pagination-li",
                  "pag-client-li",
                  "pag-client-deactive");
          return;
        }

        for (let i = 0; i < response.length; i++) {
          let itemStatus = response[i].category;
          let itemDate = response[i].date;
          let itemContent = response[i].content;

          if (
            itemStatus.toUpperCase().indexOf(filter) > -1 ||
            itemDate.toUpperCase().indexOf(filter) > -1 ||
            itemContent.toUpperCase().indexOf(filter) > -1
          ) {
            createCardNews(response[i]);
          }
        }
      })
});

