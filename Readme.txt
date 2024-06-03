THANKS FOR LOOKING AT MY PROJECT !

USED PIPENV FOR THIS PROJECT 

CHECK notes.txt for user credentials 

AFTER CLONING PROJECT 

USE PIPENV COMMANDS TO ACTIVATE VIRTUAL ENVIRONMENT AND DEPENDENCIES
REMEMBER TO SELECT THE PROPER PYTHON INTERPRETER

pipenv shell

pipenv install 

Kindly configure personal database 

Does the web application use Django to serve static HTML content?

- http://127.0.0.1:8000/restaurant/

Has the learner committed the project to a Git repository?

- https://github.com/emwasid/LittleLemon-Capstone

Does the application connect the backend to a MySQL database?

- Kindly check settings.py , configure personal database systems 

Are the menu and table booking APIs implemented?

- Menu and Booking ApIs have been configured

MenuItem - http://127.0.0.1:8000/restaurant/menu-items

SingleMenuItem - http://127.0.0.1:8000/restaurant/menu-items/1

Authentication is required for Booking URL

Authentication details provided in a notes.txt file in the git repository

Booking - http://127.0.0.1:8000/restaurant/booking/tables/


Is the application set up with user registration and authentication?

Yes using djoser, 

View or add users must be authenticated - http://127.0.0.1:8000/auth/users/

Login - http://127.0.0.1:8000/auth/token/login 

Logout - http://127.0.0.1:8000/auth/token/logout


Does the application contain unit tests?

Unit tests are located in the restaurant app package folder named 

tests.py

Can the API be tested with the Insomnia REST client?

Yes it is using token authentication.