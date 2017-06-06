This is my solution for the Unbabel Fullstack Challenge.

# Installation

Tested with Python 3.6

Just clone the repository. 

The recommended way is to create a virtual environment. On Linux/Mac

    virtualenv fferrara-challenge
    cd fferrara-challenge
    source bin/activate
    pip install -r requirements.txt

To run the application:

    python -u run.py

# Design choices

The application is self-contained, so it doesn't need any system setup. 
It uses a Python scheduler to schedule repeating tasks. 
In a production environment, it would be probably better to use a system scheduler like `cron`.

For the same reason, pending Unbabel translations are checked using a polling approach: 
a GET call each minute until the translated text is available. 
In production, it is recommended to provide a POST endpoint, reachable from the Internet, and use the `callback_url` parameter to pass the URL to Unbabel.

-------

To improve scalability, all network API calls are non-blocking. The Unbabel translation process is asynchronous as well. 
To handle all the asynchronicity and maintain low coupling between components, I adopted a reactive programming approach using [RxPy](https://github.com/ReactiveX/RxPY). 
It decouples the different components that communicate through streams.

## Possible improvements

- Improve tests coverage. Testing asynchronous code can be quite difficult.
- Better memory management to ensure all the threads are cleaned up properly.
- Using an ODM library.
- Better error managements.

# Unbabel Fullstack Challenge

Hey :smile:

Welcome to our Fullstack Challenge repository. This README will guide you on how to participate in this challenge.

In case you are doing this to apply for our open positions for a Fullstack Developer make sure you first check the available jobs at [https://unbabel.com/jobs](https://unbabel.com/jobs)

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.

**FYI:** Please understand that this challenge is not decisive if you are applying to work at [Unbabel](https://unbabel.com/jobs). There are no right and wrong answers. This is just an opportunity for us both to work together and get to know each other in a more technical way.

## Challenge


#### Build a multilingual Hackernews.

Create a multilingual clone of the Hackernews website, showing just the top 10 most voted news and their comments. 
This website must be kept updated with the original hackernews website (every 10 minutes).

Translations must be done using the Unbabel API in sandbox mode. (Ask whoever has been in contact with you about the credentials)

Build a dashboard to check the status of all translations.


#### Requirements
* Use Flask web framework
* Use Bootstrap
* For MongoDB
* Create a scalable application. 
* Only use Unbabel's Translation API on sandbox mode
* Have the news titles translated to 2 languages
* Have unit tests


#### Notes
* We dont really care much about css but please dont make our eyes suffer. 
* Page load time shouldnt exceed 2 secs 


#### Resources
* Unbabel's API: http://developers.unbabel.com/
* Hackernews API: https://github.com/HackerNews/API

