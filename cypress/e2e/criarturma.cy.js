Cypress.Commands.add('createCurso', () => {
    cy.exec('python create_curso.py', { failOnNonZeroExit: false });
});

Cypress.Commands.add('deleteAllCurso', () => {
    cy.exec('python delete_curso.py', { failOnNonZeroExit: false });
});

Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete_user.py', { failOnNonZeroExit: false });
});

Cypress.Commands.add('deleteAllInformacoes', () => {
    cy.exec('python delete_informacoes.py', { failOnNonZeroExit: false });
});
Cypress.Commands.add('createAluno', () => {
    cy.exec('python create_aluno.py', { failOnNonZeroExit: false });
});
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
describe('', () => {
    beforeEach(() => {
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
        cy.deleteAllCurso();
        cy.createAluno();
        
        Cypress.on('uncaught:exception', (err, runnable) => {
            // Ignora erros de elementos não encontrados
            if (err.message.includes('document.getElementById') || 
                err.message.includes('null') ||
                err.message.includes('undefined')) {
            return false
            }
            return true
        })
    });

    it('criar tuma', () => {
        cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor',      'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"]').click();
        cy.get('section > :nth-child(1) > a').click();
        cy.get('.btn-criar-turma').click();
        cy.get('#nome').type('Turma teste');
        cy.get('#curso').select('Iniciação a Programação');
        cy.get('#data_inicio').type('2025-05-17');
        cy.get('#data_fim').type('2029-05-17');
        cy.get('.select2-search').type('Rafael Ferraz');
        cy.get('.select2-results__option').contains('Rafael Ferraz').click();
        cy.get('.botao_criar-turma').click();
    });

    it('ver aluno', () => {
       cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor',      'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"]').click();
        cy.get('section > :nth-child(1) > a').click();
        cy.get('.btn-criar-turma').click();
        cy.get('#nome').type('Turma teste');
        cy.get('#curso').select('Iniciação a Programação');
        cy.get('#data_inicio').type('2025-05-17');
        cy.get('#data_fim').type('2029-05-17');
        cy.get('.select2-search').type('Rafael Ferraz');
        cy.get('.select2-results__option').contains('Rafael Ferraz').click();
        cy.get('.botao_criar-turma').click();
        
        cy.contains('a', 'Ver Alunos').click();

    });

     it('editar turma', () => {
       cy.createSuperUser('usuarioteste', 'usuarioteste@gmail.com', '123', '123', 'Gestor',      'instituto-solidare');
        cy.login('usuarioteste', '123');
        cy.get('[href="/portal_professor/"]').click();
        cy.get('section > :nth-child(1) > a').click();
        cy.get('.btn-criar-turma').click();
        cy.get('#nome').type('Turma teste');
        cy.get('#curso').select('Iniciação a Programação');
        cy.get('#data_inicio').type('2025-05-17');
        cy.get('#data_fim').type('2029-05-17');
        cy.get('.select2-search').type('Rafael Ferraz');
        cy.get('.select2-results__option').contains('Rafael Ferraz').click();
        cy.get('.botao_criar-turma').click();
        
        cy.contains('a', 'Editar turma').click();
        cy.get('#nome').clear().type('Editando o nome da turma teste');
        cy.get('#data_inicio').clear().type('2022-10-17');
        cy.get('#data_fim').clear().type('2026-10-17');
        cy.get('.botao_criar-turma').click();
        

    });
    





    afterEach(() => {
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
    });   
});