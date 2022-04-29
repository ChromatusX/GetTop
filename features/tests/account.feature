Feature: Testing account functions
  # Enter feature description here

  Scenario: User attempt log in with empty password
    Given Open account page
    Then Input valid email test@gmail.com
    Then Click login button
    Then Verify expected error message Error: The password field is empty.

  Scenario: User attempt to log in with empty email
    Given Open account page
    Then Input password Aab12!314
    Then Click login button
    Then Verify expected error message Error: Username is required.
    
  Scenario: User attempt to log in with invalid credentials 
    Given Open account page
    Then Input valid email test@test.com
    Then Input password Aab123!test
    Then Click login button
    Then Verify expected error message Unknown email address. Check again or try your username.
