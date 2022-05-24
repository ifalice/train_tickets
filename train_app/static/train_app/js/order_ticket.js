const train_block = document.querySelector('.train_block')
const order_button = document.querySelector('.order_button')


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


        }else if(event.target.classList.value.includes('active')){
            event.target.setAttribute('check', 'False')
            event.target.classList.remove('active')
            document.getElementById(`${number_seat}${number_train_car}`).remove()
            select_seats.splice(select_seats.indexOf(number_seat), 1) 
        }
        console.log(select_seats);
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




    
