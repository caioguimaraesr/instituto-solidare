function marcarTodos(estado) {
    const checkboxes = document.querySelectorAll('table input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.checked = estado;
    });
    atualizarContador();
}

function atualizarContador() {
    const checkboxes = document.querySelectorAll('table input[type="checkbox"]');
    const presentes = Array.from(checkboxes).filter(cb => cb.checked).length;
    const faltas = checkboxes.length - presentes;
    
    document.getElementById('contador-presentes').textContent = presentes;
    document.getElementById('contador-faltas').textContent = faltas;
}

document.addEventListener('DOMContentLoaded', atualizarContador);

document.querySelectorAll('table input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', atualizarContador);
});