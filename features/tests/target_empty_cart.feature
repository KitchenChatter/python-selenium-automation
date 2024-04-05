# Created by ryanowens at 4/4/24
Feature: "Your cart is empty

  Scenario: Verify user cart is empty
    Given Open Target main page
    Then Search for 'Click on cart icon'
    Then Verify "Your cart is empty"

