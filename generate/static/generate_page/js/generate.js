let basicColor = document.querySelector('b-color') 
let gradientColor = document.querySelector('g-color')
console.log('hello')
gradientColor.addEventListener('click', () => {
    let gradientColor2 = document.createElement('input')
    gradientColor2.type = 'color'
    document.body.appendChild(gradientColor2)
    console.log('gradient')
})

basicColor.addEventListener('click', () => {
    document.body.removeChild(gradientColor2)
    console.log('basic')
})

// let qrSizes = document.getElementById('qrSizes')

// window.addEventListener('load', () => {
//     for (let i = 1; i <= 10; i++) {
//         let option = document.createElement('option')
//         let hw = i*100
//         option.text = hw + ' x ' + hw

//         option.value = hw
//         qrSizes.append(option)

//         console.log(99999999)

//     }
// })

