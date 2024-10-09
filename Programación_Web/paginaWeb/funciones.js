// Función para manejar el scroll del header
function handleHeaderScroll() {
    const header = document.querySelector('header');
    const scrollTrigger = 100; // Ajusta este valor según necesites

    window.addEventListener('scroll', () => {
        if (window.scrollY >= scrollTrigger) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// Función para el slider de testimonios
function testimonialSlider() {
    const slider = document.querySelector('.testimonios-slider');
    const testimonios = slider.querySelectorAll('.testimonio');
    let currentIndex = 0;

    function showTestimonio(index) {
        testimonios.forEach((testimonio, i) => {
            testimonio.style.transform = `translateX(${100 * (i - index)}%)`;
        });
    }

    function nextTestimonio() {
        currentIndex = (currentIndex + 1) % testimonios.length;
        showTestimonio(currentIndex);
    }

    setInterval(nextTestimonio, 5000); // Cambia de testimonio cada 5 segundos
}

// Función para animación de contador
function animateCounter(element, target, duration) {
    let start = 0;
    const increment = target / (duration / 16); // 60 FPS

    function updateCounter() {
        start += increment;
        element.textContent = Math.floor(start);

        if (start < target) {
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    }

    updateCounter();
}

// Función para validar el formulario de contacto
function validateContactForm() {
    const form = document.querySelector('.contacto-form');
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const nombre = form.querySelector('input[name="nombre"]').value;
        const email = form.querySelector('input[name="email"]').value;
        const mensaje = form.querySelector('textarea[name="mensaje"]').value;
        
        if (nombre.trim() === '' || email.trim() === '' || mensaje.trim() === '') {
            alert('Por favor, completa todos los campos obligatorios.');
            return;
        }
        
        if (!isValidEmail(email)) {
            alert('Por favor, introduce un email válido.');
            return;
        }
        
        // Aquí puedes agregar el código para enviar el formulario
        alert('Formulario enviado con éxito!');
        form.reset();
    });
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Función para inicializar todas las funcionalidades
function initApp() {
    handleHeaderScroll();
    testimonialSlider();
    validateContactForm();
    
    // Ejemplo de uso de animateCounter
    const clientesElement = document.getElementById('clientes-count');
    animateCounter(clientesElement, 1000, 2000); // Anima hasta 1000 en 2 segundos
    
    initSlider();
}

// Inicializar la aplicación cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', initApp);

function initSlider() {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.slider-btn.prev');
    const nextBtn = document.querySelector('.slider-btn.next');
    let currentIndex = 0;
    const slideInterval = 15000; // Cambiado a 15 segundos (15000 ms)

    function showSlide(index) {
        slider.style.transform = `translateX(-${index * 100}%)`;
        updateAriaAttributes(index);
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    function updateAriaAttributes(index) {
        slides.forEach((slide, i) => {
            slide.setAttribute('aria-hidden', i !== index);
            slide.tabIndex = i === index ? 0 : -1;
        });
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    slides.forEach(slide => {
        slide.addEventListener('click', () => {
            const targetSection = document.getElementById(slide.dataset.section);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Navegación por teclado
    slider.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            nextSlide();
        } else if (e.key === 'ArrowLeft') {
            prevSlide();
        }
    });

    // Inicializar
    showSlide(currentIndex);
    let autoSlideInterval = setInterval(nextSlide, slideInterval);

    // Detener la rotación automática cuando el usuario interactúa con el slider
    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, slideInterval);
    }

    slider.addEventListener('mouseenter', stopAutoSlide);
    slider.addEventListener('mouseleave', startAutoSlide);
    prevBtn.addEventListener('click', () => {
        stopAutoSlide();
        setTimeout(startAutoSlide, slideInterval);
    });
    nextBtn.addEventListener('click', () => {
        stopAutoSlide();
        setTimeout(startAutoSlide, slideInterval);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const contenido = document.getElementById('contenido');

    slider.addEventListener('click', function(e) {
        if (e.target.classList.contains('slide')) {
            const pagina = e.target.getAttribute('data-page');
            cargarPagina(pagina);
        }
    });

    function cargarPagina(url) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                contenido.innerHTML = data;
            })
            .catch(error => console.error('Error:', error));
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const dotsContainer = document.querySelector('.slider-dots');
    let currentSlide = 0;

    // Crear puntos indicadores
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.dot');

    function goToSlide(n) {
        slider.style.transform = `translateX(-${n * 33.333}%)`; // Ajustado para 3 slides
        currentSlide = n;
        updateDots();
        
        // Mover el foco al nuevo slide
        slides[n].querySelector('.slide-content').focus();
    }

    function updateDots() {
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentSlide);
        });
    }

    function nextSlide() {
        goToSlide(currentSlide >= 2 ? 0 : currentSlide + 1); // Ajustado para 3 slides
    }

    function prevSlide() {
        goToSlide(currentSlide <= 0 ? 2 : currentSlide - 1); // Ajustado para 3 slides
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    // Cambio automático de diapositivas cada 5 segundos
    setInterval(nextSlide, 5000);

    // Inicializar
    updateDots();
});

document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
  
    slides.forEach(slide => {
        const img = new Image();
        img.src = slide.dataset.backgroundImage;
        img.onload = () => {
            slide.style.backgroundImage = `url(${img.src})`;
        };
    });

    // ... resto del código del slider ...
});

document.addEventListener('DOMContentLoaded', function() {
    // Navegación por teclado
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') {
            prevSlide();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
        }
    });

    // Hacer que los puntos sean focusables y navegables
    dots.forEach((dot, index) => {
        dot.setAttribute('tabindex', '0');
        dot.setAttribute('role', 'tab');
        dot.setAttribute('aria-label', `Ir al slide ${index + 1}`);
        dot.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                goToSlide(index);
            }
        });
    });

    // ... resto del código ...
});

let autoSlideInterval;

function startAutoSlide() {
    autoSlideInterval = setInterval(nextSlide, 5000);
}

function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

document.querySelector('.slider-container').addEventListener('focusin', stopAutoSlide);
document.querySelector('.slider-container').addEventListener('focusout', startAutoSlide);

startAutoSlide(); // Iniciar la rotación automática