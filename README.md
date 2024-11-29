# Spinning Plates Budgeter App

This is a simple budget and expense tracking app built with Django. The app allows users to create budgets and track expenses against those budgets. The app is built with Django, HTML, CSS, and JavaScript. The app is deployed on Heroku and uses a Postgresql database.

## Live Demo

The app is live at [Spinning Plates](https://spinning-plates-budgeter.herokuapp.com/)

![Spinning Plates Screenshot](PATH_TO_IMAGE)

## Purpose of the Project

The purpose of this project is to build a simple budgeting app that allows users to track expenses against budgets. The app is built with Django and uses a Postgresql database. The app is deployed on Heroku.

## Features

- Create budgets
- Track expenses against budgets
- View expenses by category
- View expenses by budget
- View expenses by date
- View expenses by category and date
- View charts of expenses by category
- View charts of expenses by budget
- View remaining budget amount

<hr>

## Table of Contents

- [Spinng Plates Budgeting App](#spinning-plates-budgeter-app)
  - [Purpose of the project](#purpose-of-the-project)
  - [Table of Contents](#table-of-contents)
- [UX/UI](#ux---user-expirience)
  - [User Stories](#user-stories)
  - [Design Inspiration](#design-inspiration)
  - [Wireframes](#wireframes)
  - [Final View](#final-view)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Features left to implement](#features-left-to-implement)
- [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
- [Agile Methodologies - Project Management](#agile-methodologies---project-management)
  - [MoSCoW Prioritization](#moscow-prioritization)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Heroku deployment](#heroku-deployment)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Validator testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python-validation)
    - [Lighthouse](#lighthouse)
    - [Wave](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
- [Credits](#credits)
  - [Content](#content)

---

# UX - User Expirience

## User Stories:

- Product Owner:

- Admin

- User

## Design Inspiration

# Task List

## Setup Environment

### Colour Scheme

### Font

## Wireframes

**Browser View:**

**Phone View:**

## Final View

**Desktop**

# Features

## Existing Features

**The Background Image**

**The Logo Image**

**Contact section**

**Navbar Menu**

**Logged in/logged out user message**

**Booking Model**

**Toast Messages**

**Menu Page**

**Review Page**

**Authorisation**

**The Footer**

## Features Left to Implement

# Database Schema - Entity Relationship Diagram

# Agile Methodologies - Project Management

## MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Freefido, identifying and labelling my:

- **Must Haves:** the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.

- **Should Haves:** the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.

- **Could Haves:** these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.

- **Won't Haves:** the features or components that either no longer fit the project's brief or are of very low priority for this release.
  ![Project Board](docs/agile/project-board.png)

## Django Project Setup

1. Install Django and supporting libraries:

- `pip3 install 'django<4' gunicorn`
- `pip3 install dj_database_url psycopg2`
- `pip3 install dj3-cloudinary-storage`

2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the `pip3 freeze --local > requirements.txt` command in the terminal.
3. Create a new Django project in the terminal `django-admin startproject hatanatata .`
4. Create a new app eg. `python3 mangage.py startapp review`
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'review',
6. Create a superuser for the project to allow Admin access and enter credentials: `python3 manage.py createsuperuser`
7. Migrate the changes with commands: `python3 manage.py migrate`
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- `import os`
- `os.environ["DATABASE_URL"]="<copiedURLfromCI>"`
- `os.environ["SECRET_KEY"]="my_super^secret@key"`

For adding to **settings.py**:

- `import os`
- `import dj_database_url`
- `if os.path.exists("env.py"):`
- `import env`
- `SECRET_KEY = os.environ.get('SECRET_KEY')` (actual key hidden within env.py)

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:

- Under `BASE_DIR` enter `TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)`
- Update `TEMPLATES = 'DIRS': [TEMPLATES_DIR]` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: `web: gunicorn hatanatata.wsgi`
12. Make the necessary migrations again.

## Cloudinary API

Cloudinary provides a cloud hosting solution for media storage. All uploaded images for the menu items are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace:

- Add Cloudinary libraries to INSTALLED_APPS in settings.py
- In the order:

```
   'cloudinary_storage',
   'django.contrib.staticfiles',
   'cloudinary',
```

- Add to **env.py** and link up with **settings.py**: `os.environ["CLOUDINARY_URL"]="cloudinary://...."`
- Set Cloudinary as storage for media and static files in settings.py:
- `STATIC_URL = '/static/'`

```
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌
```

## Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'.
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:

   - **CLOUDINARY_URL**: **cloudinary://....**
   - **DATABASE_URL**:**postgres://...**
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   - **PORT**:**8000**
   - **SECRET_KEY** and value

5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> `['herokuappname', ‘localhost’, ‘8000 port url’].`
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC** may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.

# Technologies Used

- HTML5
- CSS3
- Python
  - asgiref==3.8.1
  - gunicorn==20.1.0
  - psycopg==3.2.2
  - PyJWT==2.9.0
  - python3-openid==3.2.0
  - requests-oauthlib==2.0.0
  - sqlparse==0.5.1
  - urllib3==1.26.20
  - whitenoise==5.3.0
- Django
  - dj-database-url==0.5.0
  - Django==4.2.14
  - django-allauth==0.57.2
  - django-crispy-forms==2.3
  - dj3-cloudinary-storage==0.0.6
  - django-extensions==3.2.3
  - django-summernote==0.8.20.0
- Cloudinary
  - cloudinary==1.41.0
- Heroku
- GitHub
- GitHub Projects

# Testing

## Validator Testing

### HTML

<hr>

### CSS

<hr>

### JavaScript

<hr>

### Python Validation

<hr>

### LightHouse

### Wave Accessibility Evaluation

## Manual Testing

<hr>

# Credits

## Content

---

## DAILY LOG - REMOVE BEFORE DEPLOYMENT

### Setup Environment

1. install Django - [x]
2. create Django project (test django by runserver) - [x]
3. create Django app as home (test django by runserver) - [x]
4. create requirements.txt - [x]
5. create Procfile - [x]
6. install whitenoise - [x]
7. install gunicorn - [x]
7.1 setup gunicorn in Procfile - [x]
8. freeze requirements - [x]

### Setup Heroku

#### From Heroku Dashboard

1. create heroku app - [x]
2. disable collectstatic - [x]
3. Integrate with GitHub - [x]

#### From gitpod
1. add Heroku url host to allowed hosts in settings.py - [x]
2. update csrf origins for Heroku
3. git push changes

### Setup Environment Variables

1. update settings.py to use environment variables
   1.1 import os into settings.py file - [x]
   1.2 create env.py file in root directory - [x]
   1.3 hide SECRET_KEY in env.py - [x]
   1.4 setup up debug mode in environment variables - [x]
   1.5 create import if statement for env in settings - [x]

#### Deploy
1. from Heroku deploy branch - [x]

### Setup Database

1. install psycopg2 - [x]
2. install dj_database_url - [x]
3. freeze requirements.txt - [x]
4. import dj_database_url in settings.py - [x]
5. setup database in settings.py - [x]
6. setup database url in env.py - [x]
7. migrate database - [x]
8. create superuser - [x]

## Setup Postgres Database

### Terminal
1. create DB via CI Database Maker - [x]
2. install DB packages - [x]
3. freeze requirements - [x]

### update env.py
1. add import os to env.py - [x]
2. set environment variables - [x]

### update Heroku with pgsql
1 add secret key - [x]
2 add pg DATABASE_URL config var in Heroku - [x]

### update settings.py
1. import dj_database_url and path to env.py - [x]
2. remove sqlite3 settings - [x]
3. add Heroku url reference - [x]


## Setup Cloudinary

1. install cloudinary - [x]
2. setup cloudinary in settings.py - [x]
3. setup cloudinary in env.py - [x]
4. setup cloudinary in heroku config vars - [x]
5. create media, static and templates folders - [x]

## Test Initial Setup
1. create templates folder - [x]
2. create base.html - [x]
3. create templates/includes folder - [x]
4. create navbar.html in includes folder - [x]
5. create footer.html in includes folder - [x]
6. create static folder - [x]
7. create static/css folder - [x]
8. create static/images folder - [x]
9. create base.css in css folder - [x]
10. create home/templates/home folder - [x]
11. create home urls.py - [x]
12. link home views, urls - [x]
13.  

test render using sample html, css - [x]

### Setup Allauth

1. install allauth - [x]
   Terminal Command: pip install django-allauth

2. setup allauth in settings.py - [x]
   INSTALLED_APPS = [
   ...
   'allauth',
   'allauth.account',
   'allauth.socialaccount',
   ...
   ]

Authentication Backends
AUTHENTICATION_BACKENDS = [
...

# Needed to login by username in Django admin, regardless of `allauth`

    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

...
]

3. setup allauth in urls.py - [x]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('accounts/', include('allauth.urls')),
]

4. migrate allauth - [x]
   Terminal Command: py manage.py migrate

5. setup allauth in templates - []
6. setup allauth in env.py - []

### Setup Crispy Forms

1. install crispy forms
2. setup crispy forms in settings.py
3. setup crispy forms in templates

### Setup Summernote

1. install summernote
2. setup summernote in settings.py
3. setup summernote in templates

### Setup Whitenoise

1. install whitenoise
2. setup whitenoise in settings.py
3. setup whitenoise in wsgi.py

### Setup Static and Media Files

1. setup static and media files in settings.py - [ ]
2. setup static and media files in urls.py - [ ]
3. setup static and media files in templates - [ ]
4. setup static and media files in heroku config vars - [ ]

### Setup Django Extensions

1. install django extensions
2. setup django extensions in settings.py

### Basic Site Render - Navbar, Footer, Home Page

1. create navbar - [ ]
2. create footer - [ ]
3. create base - [ ]

### User Authentication

1. create user authentication - [ ]
2. create user profile - [ ]
3. create user profile update - [ ]
4. create user profile delete - [ ]
5. create authentication styling - [ ]
6. migrate user model - [ ]

### Budget Model

1. create budget model - [ ]
2. create budget form - [ ]
3. create budget view - [ ]
4. create budget update - [ ]
5. create budget delete - [ ]
6. migrate budget model - [ ]

### Expense Model

1. create expense model - [ ]
2. create expense form - [ ]
3. create expense view - [ ]
4. create expense update - [ ]
5. create expense delete - [ ]
6. migrate expense model - [ ]

### Category Model

1. create category model - [ ]
2. create category form - [ ]
3. create category view - [ ]
4. create category update - [ ]
5. create category delete - [ ]
6. migrate category model - [ ]

### Chart Model

1. create chart model - [x]
2. create chart form - [x]
3. create chart view - [x]
4. create chart update - [x]
5. create chart delete - [x]

### Table Model

1. create table model - [x]
2. create table form - [x]
3. create table view - [x]
4. create table update - [x]
5. create table delete - [x]
6. migrate table model - [x]

### Search Model

### Styling

1. create styling for all pages - [x]

### Views

1. create Fixed Expenses view - [x]
2. create Variable Expenses view - [x]
3. create Summary view - [x]

## Setup Export of Database Diagram from Django

1. install graphviz software - [x]
   (https://graphviz.org/download/)

2. install graphviz python library - [x]
   **Terminal Command:** pip install graphviz

3. install Django Extensions - [x]
   **Terminal Command:** pip install django-extensions

4. add Django Extensions to installed apps in settings.py - [x ]
   INSTALLED_APPS = [
   ...
   'django_extensions',
   ...
   ]

add the following code in the settings.py at the end.
GRAPH_MODELS = {
'all_applications': True,
'group_models': True,
}

5. install pygraphviz pydot - [x]
   **Terminal Command:** pip install pygraphviz pydot
   **Terminal Command:** py manage.py graph_models -a > erd.dot
   **Terminal Command:** py manage.py graph_models -a

6. Export database diagram - [ ]
   **Terminal Command:** py manage.py graph_models -a > erd.dot && py manage.py graph_models --pydot -a -g -o erd.png

7. freeze requirements.txt - [x]


## Contributions
### Dashboard HTML 
- is a bootstrap template example 
- "author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors"
- "generator" content="Hugo 0.122.0"