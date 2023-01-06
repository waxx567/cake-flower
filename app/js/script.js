const btnHamburger = document.querySelector('#btnHamburger')
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElements = document.querySelectorAll('.has-fade');

btnHamburger.addEventListener('click', function(){
    console.log("click hamburger");

    if(header.classList.contains('open')) { // Close hamburger menu
        header.classList.remove('open');
        fadeElements.forEach.(function(element){
            element.classList.remove('fade-in');
            element.classList.add('fade-out');
        });
    }
    else { // Open hamburger menu
        header.classList.add('open');
        fadeElements.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
        });
    }
})
 