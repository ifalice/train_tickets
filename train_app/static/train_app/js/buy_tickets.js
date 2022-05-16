window.onload = function() {
    const block_button_type_train_car = document.querySelector('.block_button_type_train_car')
 
    block_button_type_train_car.addEventListener('click', function(event){
        
        if (event.target.closest('.button_type_train_car')){ 
            document.querySelector('.train-car').remove()
         
            const number_train_car = event.target.getAttribute('number_train_car');  
            const type_train_car = event.target.getAttribute('type_train_car');
            const number_train = event.target.getAttribute('number_train') 
            fetch(`http://127.0.0.1:8000/get_data_train_car/?number_train=${number_train}&type_train_car=${type_train_car}&number_train_car=${number_train_car}`,{
                headers:{
                    'Content-Type': 'application/json', 
                }
            }).then(response => {            
                return response.json()
            }).then(data => {
                let number_of_rows = data.type_train_car_data.number_of_rows
                let number_of_seats = data.type_train_car_data.number_of_seats
            
                let div_train_car = document.createElement('div')
                div_train_car.classList.add('train-car')
                block_button_type_train_car.after(div_train_car)
    
                for(i=0; i<number_of_rows; i++){
                    let div_row = document.createElement('div')
                    div_row.classList.add('row')
                    div_train_car.append(div_row)
                    for(seat=0; seat<number_of_seats; seat++){
                        let div_seat = document.createElement('div')
                        div_seat.classList.add('seat')
                        div_row.append(div_seat)      
                    }

                }          
                console.log(data);    
                console.log(data.type_train_car_data.number_of_rows);
            })  
        }
    })
   


    
 };



