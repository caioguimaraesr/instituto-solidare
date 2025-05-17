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

describe('teste de cadastro', () => {
    beforeEach(() => {
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
        cy.deleteAllCurso()
        cy.createCurso();
    });

    it('cadastro', () => {
        cy.visit('/auth/register/');
        cy.get('#username').type('usuario teste');
        cy.get('#email').type('teste@gmail.com');
        cy.get('#password').type('123');
        cy.get('#confirm_password').type('123');
        cy.get('#pergunta').select('Aluno');
        cy.get('.next-btn > .bx').click();
        cy.get('#first_name').type('teste');
        cy.get('#last_name').type('teste2');
        cy.get('#CPF').type('11111111111');
        cy.get('#telefone').type('11941500444');
        cy.get('#data_nascimento').type('2005-11-05');
        cy.get('#genero').select('Masculino');
        cy.get('.next-btn > .bx').click();
        cy.get('#CEP').type('54521150');
        cy.get('#endereco').type('rua do teste');
        cy.get('#numero').type('120');
        cy.get('#bairro').type('bairro do teste');
        cy.get('#estado').type('estado do teste');
        cy.get('#estado').type('estado do teste');
        cy.get('#cidade').type('cidade do teste');
        cy.get('.next-btn > .bx').click();
        cy.get('#escolaridade').select('Fundamental Completo');
        cy.get('#escola').type('escola teste');
        cy.get('#turno').select('Tarde');
        cy.get('#curso').select('Iniciação a Programação');
        cy.get('.form-step.active > .btn-2').click();
    });
    afterEach(() => {
        cy.deleteAllCurso();
        cy.deleteAllUsers();
        cy.deleteAllInformacoes();
    });   
});