let logo = ['acba.jpg', 'yuni.jpg', 'aeb.jpg', 'ameria.jpg', 'ararat.jpg', 'aydi.jpg', 'convers.jpg', 'vtb.jpg', ]
let nameB = ['<a href="https://www.google.com/maps/search/acba/@40.1793782,44.5199719,14z/data=!3m1!4b1">Ակբա բանկ</a>', '<a href="https://www.google.com/maps/search/yuni/@40.1794412,44.5199719,14z/data=!3m1!4b1">Յունի բանկ</a>', '<a href="https://www.google.com/maps/search/hay+econom/@40.1795041,44.5199719,14z/data=!3m1!4b1">ՀԱՅԷԿՈՆՈՄ ԲԱՆԿ</a>', '<a href="https://www.google.com/maps/search/ameria/@40.1795671,44.5199719,14z/data=!3m1!4b1">Ամերիա Բանկ</a>', '<a href="https://www.google.com/maps/search/Ararat+bank/@40.1550302,44.4618667,13.62z">Արարատ Բանկ</a>', '<a href="https://www.google.com/maps/search/id+bank/@40.1649505,44.4900192,13z">ԱյԴի Բանկ</a>', '<a href="https://www.google.com/maps/search/converse+bank/@40.1650711,44.4900192,13z/data=!3m1!4b1">Կոնվերս Բանկ</a>', '<a href="https://www.google.com/maps/search/vtb/@40.1651918,44.4900192,13z/data=!3m1!4b1">ՎՏԲ-Հայաստան Բանկ</a>']

let data = new Date

let day = data.getDate()
let mounth = data.getMonth()
let year = data.getFullYear()

function banks(){
    for(let i = 0; i < logo.length; i++){
        table.innerHTML += `
            <tbody>
                <tr>
                    <td class="bank" colspan='2'><div><img src='./img/bankLogo/${logo[i]}'>${nameB[i]}</div></td>
                    <td colspan='2' class='amsativ'>${day}.${mounth}.${year}</td>
                    <td class='arj' id='u${i}'></td>
                    <td class='arj' id ='us${i}'></td>
                    <td class='arj' id ='d${i}'></td>
                    <td class='arj' id ='dol${i}'></td>
                    <td class='arj' id ='r${i}'></td>
                    <td class='arj' id ='ru${i}'></td>
                    <td class='arj' id ='g${i}'></td>
                    <td class='arj' id ='gb${i}'></td>
                </tr>
            </tbody>
        `        
       
        
        
    }
}
banks()

function rate(){
    let url = './python/rate.json'

    fetch(url)
        .then(res => res.json())
        .then(data => {
            data.forEach((e,i) => {
                let u = document.getElementById(`u${i}`)
                let us = document.getElementById(`us${i}`)
                let d = document.getElementById(`d${i}`)
                let dol = document.getElementById(`dol${i}`)
                let r = document.getElementById(`r${i}`)
                let ru = document.getElementById(`ru${i}`)
                let g = document.getElementById(`g${i}`)
                let gb = document.getElementById(`gb${i}`)

                u.append(`${e.EUR[0]}`)
                us.append(`${e.EUR[1]}`)
                d.append(`${e.USD[0]}`)
                dol.append(`${e.USD[1]}`)
                r.append(`${e.RUB[0]}`)
                ru.append(`${e.RUB[1]}`)
                g.append(`${e.GBP[0]}`)
                gb.append(`${e.GBP[1]}`)
            })
        })

}
rate()


// function acba(){
//     let acba = '../python/json/acba.json'

//     fetch(acba)
//         .then(res => res.json())
//         .then(data => {
//             u0.innerText = data.EUR[0]
//             us0.innerText = data.EUR[1]
//             d0.innerText = data.USD[0]
//             do0.innerText = data.USD[1]
//             r0.innerText = data.RUB[0]
//             ru0.innerText = data.RUB[1]
//             g0.innerText = data.GBP[0]
//             gb0.innerText = data.GBP[1]
//         })
// }
// acba()

// function yuni(){
//     let yuni = '../python/json/yuni.json'

//     fetch(yuni)
//         .then(res => res.json())
//         .then(data => {
//             u1.innerText = data.EUR[0]
//             us1.innerText = data.EUR[1]
//             d1.innerText = data.USD[0]
//             do1.innerText = data.USD[1]
//             r1.innerText = data.RUB[0]
//             ru1.innerText = data.RUB[1]
//             g1.innerText = data.GBP[0]
//             gb1.innerText = data.GBP[1]
//         })
// }
// yuni()