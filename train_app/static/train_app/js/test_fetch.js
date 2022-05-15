
button = document.querySelector('.button')
button.addEventListener('click', function(){
    fetch('http://127.0.0.1:8000/test_fetch/',
{   
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        "X-Requested-With": "XMLHttpRequest",
        "HTTP_X_REQUESTED_WITH": "XMLHttpRequest"
    }
})
})

