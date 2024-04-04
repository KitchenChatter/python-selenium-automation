# Created by ryanowens at 4/4/24
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page
    When Search for 'ipad'
    Then Verify search results are shown

