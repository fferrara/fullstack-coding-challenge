# Created by Flavio at 03/06/2017
Feature: User checks state of translations
  # Enter feature description here
  Unbabel translation service is asynchronous. So, the user wants to check the state of the translation jobs,
  which have been already translated, etc.

  Scenario: No translation jobs
    Given the translation list is empty
     When user visit the dashboard
     Then no translation is displayed

  Scenario: Some translation job
    Given the translation list is not empty
     When user visit the dashboard
     Then the translation jobs are displayed

  Scenario: Unfinished translation job
    Given the translation list is not empty
     When user visit the dashboard
     Then the unfinished translations are marked in yellow

  Scenario: Finished translation job
    Given the translation list is not empty
     When user visit the dashboard
     Then the finished translations are marked in green