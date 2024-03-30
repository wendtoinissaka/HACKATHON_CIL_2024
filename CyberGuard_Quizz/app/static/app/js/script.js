
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


   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Fonction pour écrire et effacer le texte
    function writeAndEraseText() {
        var textElement = document.getElementById("dynamic-text");
        var text = "Donnez vie à vos rêves, louez !";
        var speed = 100; // Vitesse d'écriture en millisecondes
        var eraseSpeed = 50; // Vitesse d'effacement en millisecondes

        // Écrire le texte
        var i = 0;
        var timer = setInterval(function() {
            textElement.innerHTML += text.charAt(i);
            i++;
            if (i > text.length) {
                clearInterval(timer);
                setTimeout(function() {
                    eraseText();
                }, 1000); // Temps avant d'effacer le texte
            }
        }, speed);

        // Effacer le texte
        function eraseText() {
            var timer2 = setInterval(function() {
                var currentText = textElement.innerHTML;
                textElement.innerHTML = currentText.slice(0, -1);
                if (currentText.length === 0) {
                    clearInterval(timer2);
                    setTimeout(function() {
                        writeAndEraseText(); // Répéter le processus
                    }, 1000); // Temps avant de réécrire le texte
                }
            }, eraseSpeed);
        }
    }

    // Appeler la fonction au chargement de la page
    window.onload = function() {
        writeAndEraseText();
    };






/*
<script>
  // Fonction pour écrire et effacer le texte
function writeAndEraseText() {
    var textElement = document.getElementById("dynamic-text");
    var text = "Louez sans stress, avec CAPADATA.";
<!--    var text = "Vivez l'aventure, on s'occupe du reste.";-->
<!--    var text = "Donnez vie à vos rêves, louez !";-->
    var speed = 100; // Vitesse d'écriture en millisecondes
    var eraseSpeed = 50; // Vitesse d'effacement en millisecondes
    var isWriting = false;

    // Écrire le texte
    function writeText() {
        isWriting = true;
        for (var i = 0; i < text.length; i++) {
            (function(i) {
                setTimeout(function() {
                    textElement.innerHTML += text.charAt(i);
                }, i * speed);
            })(i);
        }
        isWriting = false;
        setTimeout(function() {
            eraseText();
        }, text.length * speed); // Temps avant d'effacer le texte
    }

    // Effacer le texte
    function eraseText() {
        if (!isWriting) {
            var timer2 = setInterval(function() {
                var currentText = textElement.innerHTML;
                textElement.innerHTML = currentText.slice(0, -1);
                if (currentText.length === 0) {
                    clearInterval(timer2);
                    setTimeout(function() {
                        writeText(); // Répéter le processus
                    }, 1000); // Temps avant de réécrire le texte
                }
            }, eraseSpeed);
        }
    }

    // Débuter l'écriture du texte
    writeText();
}

// Appeler la fonction au chargement de la page
window.onload = function() {
    writeAndEraseText();
};

    // Appeler la fonction au chargement de la page
    window.onload = function() {
        writeAndEraseText();
    };

</script>*/



        //menu responsive code JS

var menu_toggle = document.querySelector('.menu_toggle');
var menu = document.querySelector('.menu');
var menu_toggle_span = document.querySelector('.menu_toggle span');

menu_toggle.onclick = function(){
    menu_toggle.classList.toggle('active');
    menu_toggle_span.classList.toggle('active');
    menu.classList.toggle('responsive') ;
}


<script>
        let currentIndex = 0;
        const slides = document.querySelectorAll('.carousel li');
        const totalSlides = slides.length;

        function moveSlide(direction) {
          currentIndex = (currentIndex + direction + totalSlides) % totalSlides;
          updateCarousel();
        }

        function updateCarousel() {
          const offset = -currentIndex * 100 + '%';
          document.querySelector('.carousel ul').style.transform = `translateX(${offset})`;
        }

        // Automatic carousel slide
        setInterval(function() {
          moveSlide(1);
        }, 3000);


      </script>
