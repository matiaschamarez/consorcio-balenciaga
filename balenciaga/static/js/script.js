window.addEventListener("load", function() {
    if (window.location.hash) {
        window.location.href = window.location.pathname;
    }
});


const images = document.querySelectorAll('.background-image');

window.addEventListener('scroll', () => {
    const scroll = window.scrollY;
    const blur = `${scroll / 30}px`; // Ajusta el valor para el difuminado
    const opacity = 1 - (scroll / 1000); // Ajusta el valor para la opacidad

    images.forEach((image) => {
        image.style.filter = `blur(${blur})`;
        image.style.opacity = opacity;
    });
});


//inicia sesión
document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Aquí, puedes realizar una validación simple o enviar los datos al servidor para la autenticación
        if (username === "usuario" && password === "contraseña") {
            // Inicio de sesión exitoso
            alert("Inicio de sesión exitoso");
            // Puedes redirigir al usuario a otra página aquí
        } else {
            // Inicio de sesión fallido
            alert("Credenciales incorrectas. Inténtalo de nuevo.");
        }
    });
});
