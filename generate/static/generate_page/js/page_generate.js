let qrSizes = document.getElementById('qrSizes')

window.addEventListener('load', () => {
    for (let i = 1; i <= 10; i++) {
        let option = document.createElement('option')
        let hw = i*100
        option.text = hw + ' x ' + hw

        option.value = hw
        qrSizes.append(option)

        console.log(99999999)

    }
        


})