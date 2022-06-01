
let form_post_order_ticket = document.querySelector('.form_post_order_ticket')
let data = JSON.parse(localStorage.getItem('select_seats_obj'))
let form_button_order_ticket = document.querySelector('.form_button_order_ticket')
let cookie_csrf_token = document.cookie.split(';')
let csrftoken



for (const number_train in data) {
    for (const number_train_car in data[number_train]) {
        for (const iterator of data[number_train][number_train_car]) {
            form_post_order_ticket.insertAdjacentHTML('afterbegin', 
            `<div class="wrapper-fields">         
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
                <p>${number_train}</p>  
                <p>${number_train_car}</p>
                <p>${iterator}</p>
                
            `)
        }
    }
}








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






form_button_order_ticket.addEventListener('click', function(event){
    if(valide_all_fields()){
        all_passenger = {}
        wrapper_fields_form = document.querySelectorAll('.wrapper-fields')
        let num = 1
        wrapper_fields_form.forEach(element => {
            
            passenger = {}
            
            passenger['name'] = element.children[0].children[1].firstElementChild.value
            passenger['surname'] = element.children[1].children[1].firstElementChild.value
            passenger['number_train'] = element.children[2].innerText
            passenger['number_train_car'] = element.children[3].innerText
            passenger['number_seats'] = element.children[4].innerText

            
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
    
    

})








