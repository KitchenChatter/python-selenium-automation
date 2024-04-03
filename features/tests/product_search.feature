Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input doordash into search field
    And Click on search icon
    Then Product results for doordash are shown