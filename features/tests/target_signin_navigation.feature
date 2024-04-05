# Created by ryan owens at 4/5/24
Feature: Navigate to Sign in navigation

  Scenario: Verify that a logged out user can navigate to Sign in
    Given Open Target main page
    Then  Click Sign in
    When  Open navigation menu, click Sign in
    Then  Verify Sign into your Target account