
    const list_tickets = document.querySelector('.block-list_tickets')

    list_tickets.addEventListener('click', function(event){
        if (event.target.closest('.button_index_form')){
            const number_train = event.target.getAttribute('number_train')
            const type_train_car = event.target.getAttribute('type_train_car')
            const number_train_car = event.target.getAttribute('number_train_car')
            
           
            let button = event.target.closest('.button_index_form')
            let from_city = document.querySelector('#id_from_city').getAttribute('value')
            let to_city = document.querySelector('#id_to_city').getAttribute('value')
            let from_city_time = button.getAttribute('from_city_time')
            let to_city_time = button.getAttribute('to_city_time')
            let train_info = {
                'from_city':from_city,
                'to_city':to_city,
                'from_city_time':from_city_time,
                'to_city_time':to_city_time,
                'from_city':from_city,

            }
            
            localStorage.setItem('train_info', JSON.stringify(train_info))
            window.location.href = `http://127.0.0.1:8000/buy_ticket/?number_train_car=${number_train_car}&type_train_car=${type_train_car}&number_train=${number_train}`
        }
})



   




