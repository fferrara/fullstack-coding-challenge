# Created by Flavio at 03/06/2017
Feature: Raquernews shows Hackernews posts
  # Enter feature description here
  Raquernews is a multilingual version of Hackernews, showing the top 10 most voted news and their comments.
  The news titles are translated in Brazilian Portuguese and Italian.

  Scenario: No news
    Given the news list is empty
     When user visit the homepage
     Then no post is displayed

  Scenario: 10 news are displayed
    Given the news list contain at least 10 news
     When user visit the homepage
     Then 10 news are displayed

  Scenario: news titles are translated to italian
    Given the news list contain at least 10 news
     When user visit the homepage in italian
     Then the news titles are in italian

  Scenario: news titles are translated to brazilian portuguese
    Given the news list contain at least 10 news
     When user visit the homepage in pt-br
     Then the news titles are in pt-br