describe('Selectors for Cypress vs Selenium', () => {
  it('finds the text input field, enters and returns text', function () {
    cy.visit('/text-input-field/')
    // find the input field and enter data
    cy.get('input[name=username]').type('TEST TEXT')
    // check the value in the text box
    cy.get('input[name=username]').should('have.value', 'TEST TEXT')
  })

  it('finds the check boxes', function () {
    cy.visit('/check-button-test-3/')
    // find the check boxes 
    cy.get('input[name=vehicle]')
  })
})
