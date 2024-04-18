const BalanceSelect = document.querySelector(".balance-header-select");
const BalanceInput = document.querySelectorAll(".balance-header-input");

document.addEventListener("DOMContentLoaded", () => {
    BalanceSelect.addEventListener("click", () => {
        if (BalanceSelect.value == "Баланс контракта") {
            BalanceInput[1].classList.add("balance-header-input-name")
            BalanceInput[0].classList.remove("balance-header-input-name")
        }
        else {
            BalanceInput[0].classList.remove("balance-header-input-name")
            BalanceInput[1].classList.remove("balance-header-input-name")
        }
    })
    
})

const balanceItem = document.querySelectorAll(".balance-item");

for (let balance of balanceItem) {
    console.log(Number(balance.innerHTML.replace(/[^\,\-\d]/g, '').replace(/,/, '.')) <= -1);
    if (Number(balance.innerHTML.replace(/[^\,\-\d]/g, '').replace(/,/, '.')) <= -1) {
        balance.classList.add("balance-false")
    }
    else {
        balance.classList.add("balance-true")
    }
}
