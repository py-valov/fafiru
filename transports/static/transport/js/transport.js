const transportBlockItems = document.querySelectorAll(".transport-block__items");
const itemWeight = ".transport-block__items-total-weight"
createTotal(transportBlockItems, itemWeight, "кг")

const itemVolume = ".transport-block__items-total-volume"
createTotal(transportBlockItems, itemVolume, "м3")

function createTotal(transport, link, symvol) {
    for (let a of transport) {
        total = 0
        item = a.querySelectorAll(link)
    
        for(let b of item) {
            total += Number(b.innerHTML.replace(/,/, '.'))
            a.removeChild(b)
        }
    
        console.log(total);
        let fragment = document.createDocumentFragment()
    
        let p = document.createElement("p")
        p.classList.add(link)
        p.textContent = String(total) + symvol
        a.appendChild(p)
    }
}
