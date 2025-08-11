describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://matheusmontanari.github.io/botao-enviar/')
    cy.get('button').click()
    cy.get('#mensagem').contains('Enviado com sucesso!')
  })
})