document.addEventListener("DOMContentLoaded", function() {
    console.log("ISO 9001 - App cargada correctamente");

    // Agregar lógica para manejar eventos en la interfaz
    const botones = document.querySelectorAll("button");
    botones.forEach(boton => {
        boton.addEventListener("click", function() {
            alert(`Botón ${boton.textContent} presionado`);
        });
    });

    const inputs = document.querySelectorAll("input");
    inputs.forEach(input => {
        input.addEventListener("change", function() {
            console.log(`Input cambiado: ${input.name} = ${input.value}`);
        });
    });
});
