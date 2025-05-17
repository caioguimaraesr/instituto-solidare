Cypress.Commands.add('login', (username, password) => {
    cy.visit('/auth/login/');
    cy.get('#username').type(username)
    cy.get('#password').type(password);
    cy.get('.btn-2').click();
});

Cypress.Commands.add('createUser', (username, email, password, confirm_password, pergunta, first_name, last_name, cpf, telefone, data_nascimento, genero, endereco, numero, bairro, estado, cidade, escolaridade, escola, turno, curso ) => {
    cy.visit('/auth/register/');
    cy.get('#username').type(username);
    cy.get('#email').type(email);
    cy.get('#password').type(password);
    cy.get('#confirm_password').type(confirm_password);
    cy.get('#pergunta').select(pergunta);
    cy.get('.next-btn > .bx').click();
    cy.get('#first_name').type(first_name);
    cy.get('#last_name').type(last_name);
    cy.get('#CPF').type(cpf);
    cy.get('#telefone').type(telefone);
    cy.get('#data_nascimento').type(data_nascimento);
    cy.get('#genero').select(genero);
    cy.get('.next-btn > .bx').click();
    cy.get('#CEP').type('54521150');
    cy.get('#endereco').type(endereco);
    cy.get('#numero').type(numero);
    cy.get('#bairro').type(bairro);
    cy.get('#estado').type(estado);
    cy.get('#cidade').type(cidade);
    cy.get('.next-btn > .bx').click();
    cy.get('#escolaridade').select(escolaridade);
    cy.get('#escola').type(escola);
    cy.get('#turno').select(turno);
    cy.get('#curso').select(curso);
    cy.get('.form-step.active > .btn-2').click();
});

Cypress.Commands.add('createSuperUser', (username, email, password, confirm_password, pergunta, senha_professor) => {
    cy.visit('/auth/register/');
    cy.get('#username').type(username);
    cy.get('#email').type(email);
    cy.get('#password').type(password);
    cy.get('#confirm_password').type(confirm_password);
    cy.get('#pergunta').select(pergunta);
    cy.get('#cod_seguranca').type(senha_professor)
    cy.get('#submit-professor').click();
});

Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete_user.py', { failOnNonZeroExit: false });
});

Cypress.Commands.add('deleteAllInformacoes', () => {
    cy.exec('python delete_informacoes.py', { failOnNonZeroExit: false });
});

describe('aba de aviso', () => {
    beforeEach(() => {
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
        Cypress.on('uncaught:exception', (err, runnable) => {
            if (err.message.includes('document.getElementById') || 
                err.message.includes('null') ||
                err.message.includes('undefined')) {
            return false
            }
            return true
        })
    });

    it('adicionar aviso', () => {
        cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor', 'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"] > .sidebar-title').click();
        cy.get(':nth-child(5) > a').click();
        cy.get('#abrirModal').click();
        cy.get('#titulo').type('Titulo teste');
        cy.get('#mensagem').type('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae distinctio eos id sed officia doloremque at illum totam amet error facere eum dicta inventore doloribus in vero sequi voluptatem, magnam essequissdeleniti reprehenderit.');
        cy.get('#prioridade').select('Importante');
        cy.get('.btn-salvar').click();
    });

    it('editar aviso', () => {
        cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor', 'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"] > .sidebar-title').click();
        cy.get(':nth-child(5) > a').click();
        cy.get('#abrirModal').click();
        cy.get('#titulo').type('Titulo teste');
        cy.get('#mensagem').type('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae distinctio eos id sed officia doloremque at illum totam amet error facere eum dicta inventore doloribus in vero sequi voluptatem, magnam esse quis saepe deleniti reprehenderit.');
        cy.get('#prioridade').select('Importante');
        cy.get('.btn-salvar').click();
        
        cy.get('.editar-btn > .bx').click();
        cy.get('#titulo').clear().type('Alterando o titulo teste');
        cy.get('#mensagem').clear().type('Alterando a descrição teste');
        cy.get('#prioridade').select('Normal');
        cy.get('.btn-salvar').click();
    });

    it('deletar aviso', () => {
        cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor', 'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"] > .sidebar-title').click();
        cy.get(':nth-child(5) > a').click();
        cy.get('#abrirModal').click();
        cy.get('#titulo').type('Titulo teste');
        cy.get('#mensagem').type('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae distinctio eos id sed officia doloremque at illum totam amet error facere eum dicta inventore doloribus in vero sequi voluptatem, magnam esse quis saepe deleniti reprehenderit.');
        cy.get('#prioridade').select('Importante');
        cy.get('.btn-salvar').click();

        cy.get('.bx.bx-x').click();
    });
    
    afterEach(() => {
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
    });   
});