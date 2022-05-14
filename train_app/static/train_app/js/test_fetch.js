fetch('http://127.0.0.1:8000/test_fetch/',
{
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => {
    console.log(response.json());
}).then(data => {
    console.log(data);
})