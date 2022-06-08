
let cookie_csrf_token = document.cookie.split(';')

cookie_csrf_token.forEach(element => {
    let item = element.split('=') 
    if (item[0] == 'csrftoken'){
        csrftoken = item[1]
    }

});





function fetchRequestTypeTrainCar(event = null){
    
    let number_train
    let type_train_car
    let number_train_car
    if (event == null){
        let list_train_info = []
        document.location.search.replace('?','').split('&').forEach(element => {
            element.indexOf('=')
            list_train_info.push(element.slice(element.indexOf('=')+1, element.length)
            ) 
        });
        number_train = list_train_info[2]
        type_train_car = list_train_info[1] 
        number_train_car = list_train_info[0]    

        
    }else{
        number_train_car = event.target.getAttribute('number_train_car');  
        type_train_car = event.target.getAttribute('type_train_car');
        number_train = event.target.getAttribute('number_train');     
    }   
    
        
        
        fetch('get_true_seats/',{
            method:'POST',
            body: JSON.stringify({'number_train':number_train,'number_train_car': number_train_car,}),
            headers:{
                'Content-Type': 'application/json', 
                "X-CSRFToken": csrftoken,
            }
        }).then(request => {
            return request.json()
        }).then(data => {
            select_seats = data.list_number_select_seats
            seats = document.querySelectorAll('.seat')
            seats.forEach(element => {
                if (select_seats.includes(parseInt(element.getAttribute('number_seat')))){
                    element.setAttribute('check', 'True')
                    element.classList.add('true') 
                }else{
                    element.setAttribute('check', 'False')
                    element.classList.add('false') 
                }
            })    
        })

        



        fetch(`http://127.0.0.1:8000/get_data_train_car/?number_train=${number_train}&type_train_car=${type_train_car}&number_train_car=${number_train_car}`,{
            headers:{
                'Content-Type': 'application/json', 
            }
        }).then(response => {
            return response.json()
        }).then(data => {
            if(document.querySelector('.train-car')){
                document.querySelector('.train-car').remove()
            }
            
            let number_of_rows = data.type_train_car_data.number_of_rows
            let number_of_seats = data.type_train_car_data.number_of_seats
            let all_number_seats = 1
            let train_block = document.querySelector('.train_block')   
            let div_train_car = document.createElement('div')
            div_train_car.classList.add('train-car')
        
            train_block.prepend(div_train_car)

            
            

            for(i=0; i<number_of_rows; i++){
                let div_row = document.createElement('div')
                div_row.classList.add('row')
                div_row.setAttribute('number_train_car', number_train_car)
                div_train_car.append(div_row)
                for(seat=0; seat<number_of_seats; seat++){
                    let div_seat = document.createElement('div')           
                    
                    div_seat.setAttribute('number_seat', all_number_seats)
                    div_seat.classList.add('seat')
                    div_seat.textContent = `${all_number_seats++}`
                    div_row.append(div_seat)      
                }

            } 
    
            
    })    
        
    }
    
