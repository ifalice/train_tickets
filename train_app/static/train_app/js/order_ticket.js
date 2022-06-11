
let form_post_order_ticket = document.querySelector('.form_post_order_ticket')
let data = JSON.parse(localStorage.getItem('select_seats_obj'))
let train_info = JSON.parse(localStorage.getItem('train_info'))
let form_button_order_ticket = document.querySelector('.form_button_order_ticket')
let cookie_csrf_token = document.cookie.split(';')
let csrftoken



for (const number_train in data) {
    for (const number_train_car in data[number_train]) {
        for (const number_seats of data[number_train][number_train_car]) {
            let number_and_type_train_car = number_train_car.split('-')
            
            form_post_order_ticket.insertAdjacentHTML('afterbegin', 
            `<div class="wrapper-fields" number_train="${number_train}" number_train_car="${number_and_type_train_car[0]}" number_seats="${number_seats}" type_train_car="${number_and_type_train_car[1]}">         
                <div class="wrapper-field_group">
                    <div class="field-label">
                        Name:
                    </div>  
                    <div class="field-field">
                        <input type="text" name="name" required id="id_name" class="input_name inp" invalid="true">
                    </div>                           
            
                </div>                                                            
                <div class="wrapper-field_group">
                    <div class="field-label">
                        Surname:
                    </div> 
                    <div class="field-field">
                        <input type="text" name="surname" required id="id_surname" class="input_surname inp" invalid="true">
                    </div>                           
                   
            </div>
            <div class="train_info_form_style" >
                <p>Number train: ${number_train}</p>  
                <p>Number train car: ${number_and_type_train_car[0]}</p>
                <p>Type train car: ${number_and_type_train_car[1]}</p>
                <p>Number seats: ${number_seats}</p>
                <p>Train path: ${train_info['from_city']} - ${train_info['to_city']}</p>
                <p>From city: ${train_info['from_city_time']}</p>
                <p>Leave city: ${train_info['leave_city_time']}</p>
                <p>To city: ${train_info['to_city_time']}</p>
            </div>    
                
            `)
        }
    }
}

console.log(data);






let input_name = document.querySelectorAll('.input_name')
let input_surname = document.querySelectorAll('.input_surname')
let all_name = []
let all_surname = []


form_post_order_ticket.addEventListener('focusout', function(event){
    if (event.target.closest('.input_name')){
        valid_fields(event.target.closest('.input_name'))           
    }else if(event.target.closest('.input_surname')){
        valid_fields(event.target.closest('.input_surname'))   
    }
})



let valid_fields = function(field){ 
    if (!field.value){ 
        field.setAttribute('invalid', 'true')
        if(!field.nextElementSibling){
            req_field_div = document.createElement('div')
            req_field_div.classList.add('required_field','field-help_text')
            req_field_div.textContent = 'Required field'    
            field.after(req_field_div)
        }
        
    }else{
        field.removeAttribute('invalid')
        if(field.nextElementSibling){
            field.nextElementSibling.remove()
            
            
        }
    
    }
}
  

let valide_all_fields = function(){
    let all_fields = document.querySelectorAll('.inp')
    let valid = []
    all_fields.forEach(element => {
        if(element.getAttribute('invalid')){
            valid.push(false)
            valid_fields(element) 
        }else{
            valid.pop()
        } 

    })
    if(valid.length > 0){
        return false   
    }else{
        return true  
    }
}



cookie_csrf_token.forEach(element => {
    let item = element.split('=') 
    if (item[0] == 'csrftoken'){
        csrftoken = item[1]
    }

});




let request_tickets_info = function(event){
    if(valide_all_fields()){
        form_button_order_ticket.removeEventListener('click', request_tickets_info)
        all_passenger = {}
        wrapper_fields_form = document.querySelectorAll('.wrapper-fields')
        let num = 1
        wrapper_fields_form.forEach(element => {
            
            passenger = {}
            
            passenger['name'] = element.children[0].children[1].firstElementChild.value
            passenger['surname'] = element.children[1].children[1].firstElementChild.value
            passenger['number_train'] = element.getAttribute('number_train')
            passenger['number_train_car'] = element.getAttribute('number_train_car')
            passenger['number_seats'] = element.getAttribute('number_seats')
            passenger['type_train_car'] = element.getAttribute('type_train_car')
            passenger['from_city'] = train_info['from_city']
            passenger['from_city_time'] = train_info['from_city_time']
            passenger['to_city'] = train_info['to_city']
            passenger['to_city_time'] = train_info['to_city_time']
            passenger['leave_city_time'] = train_info['leave_city_time']
            
            

            
            all_passenger[num++] = passenger
        })


    
        fetch('', {
            method:'POST',
            body: JSON.stringify(all_passenger),
            mode: 'same-origin',
            headers:{
                'Content-type': 'application/json',
                "X-CSRFToken": csrftoken,
                
            }
        }).then(response => {
            return response.json()
            
        }).then(data => {
            console.log(data);
        })   
    }
    
}

form_button_order_ticket.addEventListener('click', request_tickets_info)








