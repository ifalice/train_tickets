const button = document.querySelector('.button')
const list_tickets = document.querySelector('.block-list_tickets')


// list_tickets.addEventListener('click', function(event){
//     if(event.target.closest('.class_button')){
//         const xhr = new XMLHttpRequest();
//         xhr.open('GET', 'http://127.0.0.1:8000/buy_ticket/');
//         xhr.send();
//     }
// })

list_tickets.addEventListener('click', function(event){
    if (event.target.closest('.button')){
        const number_train = event.target.getAttribute('number_train')
        const type_train_car = event.target.getAttribute('type_train_car')
        window.location.href = `http://127.0.0.1:8000/buy_ticket/?number_train=${number_train}&type_train_car=${type_train_car}`
    }
})


