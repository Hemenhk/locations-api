# Locations

[Return to the README.md file](https://github.com/Hemenhk/locations-api/blob/main/README.md)  

![Locations mockup images](assets/readme/api%20home%20page.png)

Locations API is an application based on Django Rest Framework. It is the back-end portion of my final project for Code Institute.

To visit each section of the API use these urls:

* /profiles/

* /posts/

* /ratings/

* /reviews/

* /dj-rest-auth/user


Visit the deployed application [here](https://locations-api.herokuapp.com/).

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
   1. [Strategy](#strategy)
      1. [Project Goals](#project-goals)
      2. [User Goals](#user-goals)
      3. [Strategy](#strategy)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
   1. [Languages Used](#languages-used)
   2. [Libraries and Frameworks](#libraries-and-frameworks)
   4. [Database Management](#database-management)
    1. [Database Model](#database-model)
   6. [Cloud Storage](#cloud-storage)
   7. [Tools and Programs](#tools-and-programs)
5. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/Hemenhk/locations/blob/main/TESTING.md)
6. [Deployment](#deployment)
    1. [How To Use This Project](#how-to-use-this-project)  
    2. [Deployment to Heroku](#deployment-to-heroku)   
7. [Credits](#credits)
    1. [Media](#media)  
    2. [Code](#code)   
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Strategy

#### Project Goals

- The goal of this project was to provide the user with a functional API, that could properly communicate with the user.

#### User Goals

- As a user I want to be able to view all posts and individual ones.

- As a user I want to be able to view all profiles and individual ones.

- As a user I want to be able to view all ratings and individual ones.

- As a user I want to be able to view all reviews and individual ones.

- As a superuser, I want full CRUD functionality in the Django Rest Framework when developing the API.

### Strategy

To achieve the user goals, I wish to implement the following features:

* An URL for users to view all posts and by id

* An URL for users to view all profiles and by id

* An URL for users to view all ratings and by id

* An URL for users to view all reviews and by id

## Features

* Full CRUD (Create, Read, Update and Delete) functionality for the superuser to take part of when developing this app. This has been achieved by creating forms for the superuser to fill and submit when accessing the API through Django Rest Framework. The superuser can add, read, update and delete posts, profiles, ratings and reviews.


## Technologies Used

### Languages Used

- [Python](https://www.python.org/)

### Libraries and Frameworks

- [Django](https://www.djangoproject.com/) was used to build the app.

- [Django Rest Framework](https://www.django-rest-framework.org/) was used to build the API.

- [Django Allauth](https://django-allauth.readthedocs.io/) was used for authentication, registration and account management.

- [Django Rest Auth](https://dj-rest-auth.readthedocs.io/) was also used for registration and authentication.

- [Corsheaders](https://pypi.org/project/django-cors-headers/) was to access the API from the front end during and after development.

- [Google Fonts](https://fonts.google.com) was used to import fonts to the HTML file, and used throughout the project.

- [Font Awesome](https://fontawesome.com) was used to add icons to various links.

### Database Management

#### Database Model

The databse model was designed using [drawsql](https://drawsql.app/) The type of databases being used are SQLite3 during development, and [PostgreSQL](https://www.postgresql.org/).

![Locations Database Model](src/assets/readme/database.png)

- [SQLite](https://www.sqlite.com/index.html) database was used as the database during the development.

- [ElephantSQL - Postgres](https://www.elephantsql.com/) database was used in production, based on Postgres and provided by ElephantSQL.

### Cloud Storage

- [Cloudinary](https://cloudinary.com/) was used to store static and media files.

### Tools and Programs

- [Git](https://git-scm.com)

- [GitPod](https://gitpod.io/)

- [GitHub](https://github.com/)

- [Heroku](https://heroku.com)

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used during development to debug the app.

- [W3C Markup Validator](https://validator.w3.org/) was used to validate custom CSS code.

- [Favicon.io](https://favicon.io) was used to add a custom favicon.

## Testing

The testing documentation for this project can be found [here](https://github.com/Hemenhk/locations-api/blob/main/TESTING.md)

## Deployment

The project was deployed using [GitPod](https://gitpod.io/). All code was commited to [Git](https://git-scm.com) and then pushed on to [GitHub](https://github.com/) using the terminal in [GitPod](https://gitpod.io/). The application is deployed on Heroku.

### How To Use This Project

To use this project, one can either fork or clone the repository.

#### Forking

By forking this repository you copy the original to view and make changes to the code, without affecting the original repository by following these steps:

1. Log into your GitHub account.
2. Navigate to the repository and in the upper-right corner, click on "Fork".
3. In the "Create a new fork" page, press the "Create fork" button.
4. To edit the code, click on the "Gitpod" button to launch your own workspace.
5. Changes in the new repository can be merged with the original via a pull request.

#### Clone GitHub Repository

By cloning the GitHub repository, you can create a local copy of the original on your own system. To clone this repository follow these steps:

1. Log into your GitHub account.
2. Navigate to the repository and click the dropdown on the "Code" button..
3. To clone using HTTPS, copy the code provided in the field.
4. Open Git Bash and change the current directory to the location where you wish the cloned directory to be made.
5. Type git clone, then paste the URL that you copied.
6. Press Enter, and your local clone is created.

### Deployment To Heroku

This project is deployed using Heroku, with all static files being uploaded to Cloudinary. These are the steps to deploy to Heroku:

1. Log in to your Heroku account.
2. Press "Create new app", and select the desired app name and the region of which you are located, then press "Create app".
3. Press the "Deploy" tab and click on "GitHub" in the "Deployment method" field.
4. In the "Connect to GitHub" section select your profile and search for the repository. When the repository appears, click on "Connect".
5. Go to "Settings" and scroll down to "Config Vars", and click "Reveal Config Vars".
6. Here fill in the following key & values:
    1. ALLOWED_HOST = https://locations-p5.herokuapp.com/.
    2. CLIENT_ORIGIN = https://locations-p5.herokuapp.com.
    3. CLIENT_ORIGIN_DEV = https://3000-hemenhk-locations-52paoqmtok9.ws-eu83.gitpod.io/ (this value may change during the developing process).
    4. CLOUDINART_URL = cloudinary://(the value beyond is private).
    5. DATABASE_URL = postgres://(the value beyond is private).
    7. SECRET_KEY = (this value is private).
7. After all config vars have been filled make sure "Buildpacks" is set to "heroku/python".
8. Make your way to "Deploy" and scroll down to "Manual deploy".
9. Press "Deploy branch" and when the build is finished, open the app.

## Credits

### Code

- The code from Code Institute's "Django Rest Framework" project was used as the main reference, from which this project was built, and was of great help.

## Known Bugs

**Testing User Adding Post**

An issue arose when writing automated testing to see if the user could add posts. The terminal would not allow the status code to be 201 (Created), instead threw a 400 (Bad Request)

This issue was resolved by adding the necessary models and meta fields in the API used for this project. After which the fields were returned prepopulated with the original posts input.

## Acknowledgements

- My family for showing me support during the development of this project.

- My mentor, Marcel, for providing invaluable knowledge and feedback during out meetings. His perspective has been immensely useful, and without his help, some code may not have made an appearence.

- Code Institute for providing me with the material to build this project, and the Slack community for their help and positive comments.
