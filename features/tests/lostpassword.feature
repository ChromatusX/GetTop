Feature: Testing lost-password functionalities
  # Enter feature description here

  Scenario: User sees correct error message when inputting "a" and click reset
    Given Open lost password page
    Then Insert input a on lost password field
    And Click reset password button
    Then Verify lost password error message Invalid username or email.

  Scenario: User clicks reset password button without any input
    Given Open lost password page
    Then Insert input   on lost password field
    And Click reset password button
    Then Verify lost password error message Enter a username or email address.