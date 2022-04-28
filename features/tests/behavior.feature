
Feature: Search for valid and invalid items
   Enter feature description here

  Scenario: Searching for invalid items
      Given Open GetTop Page
      Then Hover search icon
      Then Search for item Oranges
      Then Verify message

  Scenario: Searching for valid items
      Given Open GetTop Page
      Then Hover search icon
      Then Search for item Macbook
      Then Verify item Macbook

  Scenario: Searching for valid items
      Given Open GetTop Page
      Then Hover search icon
      Then Search for item iPhone
      Then Verify item iPhone