
 window.onload = function() {
     
    fetchRequestTypeTrainCar()
    const block_button_type_train_car = document.querySelector('.block_button_type_train_car')

    block_button_type_train_car.addEventListener('click', function(event){
        if (event.target.closest('.button_type_train_car')){
            fetchRequestTypeTrainCar(event)  
        }
    })  
 };

