# Q-learn
QLEARN is an interactive quiz app designed to engage users in fun and educational trivia on general topics relating to various aspects of the world. 
Users can sign up, participate in quizzes on various topics, and view their scores and best time. 
The app will have performance metrics and progress reports which will help users track their learning journey.

## Objectives
The objectives of this project includes the following;
- ## BACKEND OBJECTIVE:
-  Integrating User Authentication using Django’s built in auth system.
-  Working with Django’s ORM (Object Relational Mapping).
-  Working with robust database systems (MySQL).
-  Working with RESTful framework in Django.
- ## FRONTEND OBJECTIVE:
-  Implementing a responsive web app using HTML, CSS, and SASS.
-  Navigating through Ui components like buttons, menus and screens
-  Creating a responsive design that adapts to all screen sizes
-  Implement accessibility features to ensure easy usability

# APP FEATURES
- User registration and authentication
- View Results 
- Take quiz on preferred topic

## URL ROUTES
* '/' - index page (home_page)
* '/quiz/<str:topic_name>/' - default topic_name is 'sports'. quizzes page (login required)
* '/quiz/login/' - login page
* '/quiz/register/' - register page
* '/quiz/<str:topic_name>/results' - result page (login required)
* '/quiz/<str:topic_name>/submit' - submit page (login required)

# AUTHORS
## BACKEND AND DEVOPS
- EMMANUEL KUFFOUR OSEI

## FRONTEND 
- EMMANUEL ASANTE