let wrapper_fields = document.querySelectorAll('.wrapper-fields')
let wrapper_field = document.querySelector('.wrapper-fields')

console.log(JSON.parse(localStorage.getItem('select_seats_obj')));  


wrapper_field.insertAdjacentHTML('afterend', 
`<div class="wrapper-fields">         
    <div class="wrapper-field_group">
        <div class="field-label">
            Name:
        </div>  
        <div class="field-field">
            <input type="text" name="name" required id="id_name">
        </div>                           
        <div class="field-help_text">       
        </div> 
    </div>                                                            
    <div class="wrapper-field_group">
        <div class="field-label">
            Surname:
        </div> 
        <div class="field-field">
            <input type="text" name="surname" required id="id_surname">
        </div>                           
        <div class="field-help_text">   
        </div> 
</div>`)

// wrapper_fields.forEach(element => {
//     let div_seat_and_train_car = document.createElement('div')
//     div_seat_and_train_car.textContent = ''
// })



let form_button_order_ticket = document.querySelector('.form_button_order_ticket')
let cookie_csrf_token = document.cookie.split(';')
let csrftoken

cookie_csrf_token.forEach(element => {
    let item = element.split('=') 
    if (item[0] == 'csrftoken'){
        csrftoken = item[1]
    }

});

form_button_order_ticket.addEventListener('click', function(event){

    fetch('fetch/', {
        method:'GET',
        body: localStorage.getItem('select_seats_obj'),
        mode: 'same-origin',
        headers:{
            'Content-type': 'application/json',
            "X-CSRFToken": csrftoken,
            
        }
    })    
    

})










