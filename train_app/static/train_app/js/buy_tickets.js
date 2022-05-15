window.onload = function() {
    const block_button_type_train_car = document.querySelector('.block_button_type_train_car')
 
    block_button_type_train_car.addEventListener('click', function(event){
        if (event.target.closest('.button_type_train_car')){ 
            const number_train_car = event.target.getAttribute('number_train_car');  
            const type_train_car = event.target.getAttribute('type_train_car');
            const number_train = event.target.getAttribute('number_train') 
            window.location.href = `http://127.0.0.1:8000/buy_ticket/?number_train=${number_train}&type_train_car=${type_train_car}`
            console.log(number_train_car, type_train_car);
            
            
        }
    })
    let div = document.createElement('div')
    let div_train_car = document.createElement('div')
    div_train_car.classList.add('train-car')
    block_button_type_train_car.after(div_train_car)
    div_train_car.append(div)
    div_train_car.remove()

    

    console.log(data);
    
 };



fetch('http://127.0.0.1:8000/buy_ticket/?number_train=d20&type_train_car=cupe',
 {
     method: "GET",
     headers: {
        "x-requested-with": "XMLHttpRequest"    
     }
 })

 fetch('/buy_ticket/?number_train=d20&type_train_car=cupe', {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest"
    },

  });