
var sections = document.querySelectorAll('section');
var navlinks = document.querySelectorAll('header nav a');
var icon = document.querySelector('#menu-icon');
var navbar = document.querySelector('.navbar');
var header = document.querySelector('header');


/* ================================== Toggle inavbar icon ================================== */

icon.addEventListener('click', function() {
    icon.classList.toggle('ti-times');
    navbar.classList.toggle('active');
});



/* ================================== Scroll sections active ================================== */
window.addEventListener('scroll', function () {

    sections.forEach(function (section) {
        var top = window.scrollY;
        var offset = (section.offsetTop - 150);
        var height = section.offsetHeight;
        var id = section.getAttribute('id');
        if (top >= offset && top < offset + height) {
            navlinks.forEach(function (link) {
                link.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        }
    });


    /* ================================== Sticky navbar ================================== */
    header.classList.toggle('sticky', window.scrollY > 100);

    /* ================================== Remove toggle icon and navbar when click nav bar link (scroll) ================================== */
    icon.classList.remove('ti-times');
    navbar.classList.remove('active');
});

    /* ================================== Scroll reveal using scrollrevealjs  ================================== */
    ScrollReveal({ reset: true, distance: '80px', duration: 2000, delay: 200 });
    ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
    ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', { origin: 'bottom' });
    ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });

    /* ================================== Typing animation using typed.js  ================================== */
    const typed =  new Typed('.multiple-text', { strings: ['Ami', 'Confident', 'Assistant','Compagnon'], typeSpeed: 100, backSpeed: 100, backDelay: 1000, loop: true })