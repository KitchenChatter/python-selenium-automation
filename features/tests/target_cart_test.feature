# Created by ryan owens at 4/4/24
Feature: Cart tests

  Scenario: Verify user cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

