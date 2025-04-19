const steps = document.querySelectorAll(".form-step");
const nextBtn = document.querySelector(".next-btn");
const prevBtn = document.querySelector(".prev-btn");
const indicators = document.querySelectorAll(".step");
const formTitle = document.getElementById("form-title");

const titles = [
    "Cadastro",
    "Informações Pessoais",
    "Endereço",
    "Informações Pedagógicas",
];

let currentStep = 0;

function showStep(step) {
    steps.forEach((s, index) => {
        s.classList.toggle("active", index === step);
    });
    indicators.forEach((dot, index) => {
        dot.classList.toggle("active", index === step);
    });

    formTitle.textContent = titles[step];
}

// Navegação com ícones de seta
nextBtn.addEventListener("click", () => {
    if (currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
});

prevBtn.addEventListener("click", () => {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
});

showStep(currentStep);

// CPF
const cpfInput = document.getElementById("CPF");

cpfInput.addEventListener("input", function () {
    let value = this.value.replace(/\D/g, ""); 

    if (value.length > 11) {
        value = value.slice(0, 11);
    }

    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

    this.value = value;
});

// Telefone
const telefoneInput = document.getElementById("telefone");

telefoneInput.addEventListener("input", function () {
    let value = this.value.replace(/\D/g, "");

    if (value.length > 11) {
        value = value.slice(0, 11);
    }

    if (value.length <= 10) {
        value = value.replace(/^(\d{2})(\d{5})(\d{4})$/, "($1) $2-$3");
    } else {
        value = value.replace(/^(\d{2})(\d{5})(\d{4})$/, "($1) $2-$3"); 
    }

    this.value = value;
});
