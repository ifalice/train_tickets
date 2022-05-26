

const train_block = document.querySelector('.train_block')
const order_button = document.querySelector('.order_button')

let select_seats_obj = {}
let select_seats = []
train_block.addEventListener('click', function(event){
    let number_seat = event.target.getAttribute('number_seat') 
    let number_train_car = document.querySelector('.row').getAttribute('number_train_car')
    if (event.target.closest('.seat')){
        if (event.target.getAttribute('check') == 'False'){

            event.target.setAttribute('check', 'True')
            event.target.classList.add('active')
            select_seats.push(number_seat)
            train_block.append(create_select_seat_card(number_seat,number_train_car))
            if (!select_seats_obj.hasOwnProperty(number_train_car)){
                select_seats_obj[number_train_car] = [number_seat]
                console.log(select_seats_obj);   
            }else{
                select_seats_obj[number_train_car].push(number_seat)
                console.log(select_seats_obj);
            }


        }else if(event.target.classList.value.includes('active')){
            event.target.setAttribute('check', 'False')
            event.target.classList.remove('active')
            document.getElementById(`${number_seat}${number_train_car}`).remove()
            select_seats.splice(select_seats.indexOf(number_seat), 1) 
            select_seats_obj[number_train_car].splice(select_seats_obj[number_train_car].indexOf(number_seat), 1)
        }
        
    }
})

create_select_seat_card = function(number_of_seat, number_train_car){
    card_select_seat = document.createElement('div')
    card_select_seat.classList.add('card_select_seat')
    card_select_seat.setAttribute('number_of_seat', number_of_seat)
    card_select_seat.setAttribute('number_train_car', number_train_car)
    card_select_seat.setAttribute('id', number_of_seat+number_train_car)
    card_select_seat.insertAdjacentHTML('afterbegin', 
    `<p>Number seat: ${number_of_seat}</p>
    <p>Number train car: ${number_train_car}</p>    
    `);
    

    return card_select_seat
}



let cookie_csrf_token = document.cookie.split(';')
let csrftoken

cookie_csrf_token.forEach(element => {
    let item = element.split('=') 
    if (item[0] == 'csrftoken'){
        csrftoken = item[1]
    }

});

order_button.addEventListener('click', function(event){
    window.location.href = 'http://127.0.0.1:8000/buy_ticket/order_ticket/'
    fetch('order_ticket/', {
        method:'POST',
        body: JSON.stringify(select_seats_obj),
        mode: 'same-origin',
        headers:{
            'Content-type': 'application/json',
            "X-CSRFToken": csrftoken,
            
        }
    })    
    

})










