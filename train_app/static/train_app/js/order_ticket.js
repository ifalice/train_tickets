
let form_post_order_ticket = document.querySelector('.form_post_order_ticket')
let data = JSON.parse(localStorage.getItem('select_seats_obj'))
let form_button_order_ticket = document.querySelector('.form_button_order_ticket')
let cookie_csrf_token = document.cookie.split(';')
let csrftoken



for (const number_train in data) {
    for (const number_train_car in data[number_train]) {
        console.log(number_train_car);
        for (const iterator of data[number_train][number_train_car]) {
            form_post_order_ticket.insertAdjacentHTML('afterbegin', 
            `<div class="wrapper-fields">         
                <div class="wrapper-field_group">
                    <div class="field-label">
                        Name:
                    </div>  
                    <div class="field-field">
                        <input type="text" name="name" required id="id_name" class="input_name">
                    </div>                           
                    <div class="field-help_text">       
                    </div> 
                </div>                                                            
                <div class="wrapper-field_group">
                    <div class="field-label">
                        Surname:
                    </div> 
                    <div class="field-field">
                        <input type="text" name="surname" required id="id_surname" class="input_surname">
                    </div>                           
                    <div class="field-help_text">   
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
        console.log(event.target.closest('.input_name').value);
        
    }
})






cookie_csrf_token.forEach(element => {
    let item = element.split('=') 
    if (item[0] == 'csrftoken'){
        csrftoken = item[1]
    }

});

form_button_order_ticket.addEventListener('click', function(event){

    input_name.forEach(element => {
        all_name.push(element.value)
    })
    input_surname.forEach(element => {
        all_surname.push(element.value)
    })
    data['all_name'] = all_name
    data['all_surname'] = all_surname   


    fetch('', {
        method:'POST',
        body: JSON.stringify(data),
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
    

})








