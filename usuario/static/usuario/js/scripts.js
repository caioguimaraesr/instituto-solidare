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

    if (formTitle) {
        formTitle.textContent = titles[step];
    }
}

if (nextBtn) {
    nextBtn.addEventListener("click", () => {
        if (currentStep < steps.length - 1) {
            currentStep++;
            showStep(currentStep);
        }
    });
}

if (prevBtn) {
    prevBtn.addEventListener("click", () => {
        if (currentStep > 0) {
            currentStep--;
            showStep(currentStep);
        }
    });
}

showStep(currentStep);

// CPF
const cpfInput = document.getElementById("CPF");

if (cpfInput) {
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
}

// Telefone
const telefoneInput = document.getElementById("telefone");

if (telefoneInput) {
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
}

// Portal do Professor
document.addEventListener('DOMContentLoaded', function () {
    const perguntaSelect = document.getElementById('pergunta');
    const pagination = document.querySelector('.pagination');
    const submitProfessor = document.getElementById('submit-professor');

    function verificarPergunta() {
        if (perguntaSelect && pagination && submitProfessor) {
            if (perguntaSelect.value === 'professor') {
                pagination.style.display = 'none';
                submitProfessor.style.display = 'block'; 
            } else {
                pagination.style.display = 'flex'; 
                submitProfessor.style.display = 'none'; 
            }
        }
    }

    verificarPergunta();

    if (perguntaSelect) {
        perguntaSelect.addEventListener('change', verificarPergunta);
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const selectPergunta = document.getElementById("pergunta");

    if (selectPergunta) {
        selectPergunta.addEventListener("change", function () {
            const isProfessor = selectPergunta.value === "professor";

            const etapasExtras = document.querySelectorAll(
                '.form-step:nth-of-type(2) input, .form-step:nth-of-type(2) select, ' +
                '.form-step:nth-of-type(3) input, .form-step:nth-of-type(3) select, ' +
                '.form-step:nth-of-type(4) input, .form-step:nth-of-type(4) select'
            );

            etapasExtras.forEach((campo) => {
                if (isProfessor) {
                    campo.removeAttribute("required");
                } else {
                    campo.setAttribute("required", "required");
                }
            });

            const botaoSubmitProfessor = document.getElementById("submit-professor");
            if (botaoSubmitProfessor) {
                if (isProfessor) {
                    botaoSubmitProfessor.style.display = "block";
                } else {
                    botaoSubmitProfessor.style.display = "none";
                }
            }
        });
    }
});