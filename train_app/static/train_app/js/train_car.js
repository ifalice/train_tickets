const button = document.querySelectorAll('.class_button')
const list_tickets = document.querySelector('.block-list_tickets')


list_tickets.addEventListener('click', function(event){
    if(event.target.closest('.class_button')){
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://127.0.0.1:8000/buy_ticket/');
        xhr.send();
    }
})

