

     
fetchRequestTypeTrainCar()
const block_button_type_train_car = document.querySelector('.block_button_type_train_car')

block_button_type_train_car.addEventListener('click', function(event){
    if (event.target.closest('.button_type_train_car')){
        fetchRequestTypeTrainCar(event)  
        
    }   
})  




const train_block = document.querySelector('.train_block')
const number_train = train_block.getAttribute('number_train')
const order_button = document.querySelector('.order_button')

let select_seats_obj = {}
train_block.addEventListener('click', function(event){
    let number_seat = event.target.getAttribute('number_seat') 
    let number_train_car = document.querySelector('.row').getAttribute('number_train_car')
    if (event.target.closest('.seat')){
        if (event.target.getAttribute('check') == 'False'){

            event.target.setAttribute('check', 'True')
            event.target.classList.add('active')
            train_block.append(create_select_seat_card(number_train, number_seat,number_train_car))
            if (!select_seats_obj.hasOwnProperty(number_train)){
                select_seats_obj[number_train] = {}
               
            }
            if (!select_seats_obj[number_train].hasOwnProperty(number_train_car)){
                select_seats_obj[number_train][number_train_car] = [number_seat]
                console.log(select_seats_obj);    
                console.log(1);    
            }else{
                select_seats_obj[number_train][number_train_car].push(number_seat)
                console.log(select_seats_obj);
                console.log(select_seats_obj['d20']);
            }
            


        }else if(event.target.classList.value.includes('active')){
            event.target.setAttribute('check', 'False')
            event.target.classList.remove('active')
            document.getElementById(`${number_seat}${number_train_car}`).remove()
            select_seats_obj[number_train][number_train_car].splice(select_seats_obj[number_train][number_train_car].indexOf(number_seat), 1)
        }
        
    }
})

create_select_seat_card = function(number_train, number_of_seat, number_train_car){
    card_select_seat = document.createElement('div')
    card_select_seat.classList.add('card_select_seat')
    card_select_seat.setAttribute('number_of_seat', number_of_seat)
    card_select_seat.setAttribute('number_train_car', number_train_car)
    card_select_seat.setAttribute('id', number_of_seat+number_train_car)
    card_select_seat.insertAdjacentHTML('afterbegin', 
    `<p>Number seat: ${number_of_seat}</p>
    <p>Number train car: ${number_train_car}</p>    
    <p>Number train : ${number_train}</p>    
    `);
    

    return card_select_seat
}

let select_seats_json = JSON.stringify(select_seats_obj)
order_button.addEventListener('click', function(event){
    localStorage.setItem('select_seats_obj', JSON.stringify(select_seats_obj))
    window.location.href = 'order_ticket/'
})    
