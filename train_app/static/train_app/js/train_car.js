
    const list_tickets = document.querySelector('.block-list_tickets')

    list_tickets.addEventListener('click', function(event){
        if (event.target.closest('.button_index_form')){
            const number_train = event.target.getAttribute('number_train')
            const type_train_car = event.target.getAttribute('type_train_car')
            const number_train_car = event.target.getAttribute('number_train_car')
            window.location.href = `http://127.0.0.1:8000/buy_ticket/?number_train_car=${number_train_car}&type_train_car=${type_train_car}&number_train=${number_train}`
        }
})



   




