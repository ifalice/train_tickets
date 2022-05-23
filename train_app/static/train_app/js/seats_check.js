const train_car = document.querySelector('.form_train_car')

train_car.addEventListener('click', function(event){
    if (event.target.closest('.seat')){
        if (event.target.getAttribute('check') == 'False'){
            event.target.setAttribute('check', 'True')
            event.target.classList.add('active')
        }else if(event.target.classList.value.includes('active')){
            event.target.setAttribute('check', 'False')
            event.target.classList.remove('active')
        }
        
        
        
    }
})
    
