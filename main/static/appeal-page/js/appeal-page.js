const appealItems = document.querySelectorAll(".appeal-table-body__item")
const appealBtn = document.querySelectorAll(".appeal-category-btn")



let categoryes = (function () {
  let activeBtn = document.querySelector(".appeal-category-btn-active");
  
  return function(items, btns) {
    btns.forEach(el => {
      el.addEventListener("click", (elClick) => {
        switch(el.innerHTML) {
          case "Все":
            activeBtn.classList.remove("appeal-category-btn-active")
            activeBtn = el
            activeBtn.classList.add("appeal-category-btn-active")
            displayNone(items, el.innerHTML)
            break;

          case "Склад":
            activeBtn.classList.remove("appeal-category-btn-active")
            activeBtn = elClick.target
            activeBtn.classList.add("appeal-category-btn-active")
            displayNone(items, el.innerHTML)
            break;

          case "Счета":
            activeBtn.classList.remove("appeal-category-btn-active")
            activeBtn = elClick.target
            activeBtn.classList.add("appeal-category-btn-active")
            displayNone(items, el.innerHTML)
            break;

          case "Расчет товара":
            activeBtn.classList.remove("appeal-category-btn-active")
            activeBtn = el
            activeBtn.classList.add("appeal-category-btn-active")
            displayNone(items, el.innerHTML)
            break;

          case "Доставка":
            activeBtn.classList.remove("appeal-category-btn-active")
            activeBtn = el
            activeBtn.classList.add("appeal-category-btn-active")
            displayNone(items, el.innerHTML)
            break;
        }
      })
    })
  }
  
  
})();

function displayNone (arr, element) {
  arr.forEach(item => {
      item.style.display = "block"
  })
  
  if (element == "Все") {
    return
  }

  arr.forEach(item => {
    if (item.childNodes[1].innerHTML.indexOf(element) == -1) {
      item.style.display = "none"
    }
  })
}

categoryes(appealItems, appealBtn)

