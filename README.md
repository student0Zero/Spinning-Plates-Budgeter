# Spinning Plates Budgeter

This is a simple budget and expense tracking app built with Django. The app allows users to create budgets and track expenses against those budgets. The app is built with Django, HTML, CSS, and JavaScript. The app is deployed on Heroku and uses a Postgresql database.


![Spinnging-Plates-Budgeter Homepage](docs/project-images/homepage.png)

## Live website:
The app is live at <a href="https://spinning-plates-budgeter.herokuapp.com/" target="blank">Spinning Plates Budgeter</a>

Admin access with associated sign-in information can be accessed from <a href="https://spinning-plates-budgeter-015aa561b471.herokuapp.com/admin/" target="_blank">here</a>.

The Github repository for this project can be found <a href="https://github.com/student0Zero/Spinning-Plates-Budgeter" target="_blank">here</a>..

## Purpose of the project
The purpose of this project is to build a simple budgeting app that allows users to track expenses against budgets. The app is built with Django and uses a Postgresql database as a proof of concept project with the aim of demonstrating the authors ability to develop a CRUD project using Django, Postrgres, and a Bootstrap framework. The app is deployed on Heroku.
## Table of Contents
- [Spinning Plates Budgeter](#Spinning Plates Budgeter)
- [UX - User Experience](#UX - User Experience)
	- [User Stories](#User Stories)
	- [Design](#design)
		- [UX User Experience](#ux-user-experience)
		- [User Stories](#user-stories)
			- [Product Owner](#product-owner)
			- [Site Administrator](#site-administrator)
		- [Site Design](#site-design)
			- [Design Framework](#design-framework)
			- [Colour](#colour)
			- [Font](#font)
		- [Wireframes](#wireframes)
			- [Landing Page Wireframe](#landing-page-wireframe)
			- [Summary View Wireframe](#summary-view-wireframe)
			- [Expenses View Wireframe](#expenses-view-wireframe)
			- [Expenses Mobile View Wireframe](#expenses-mobile-view-wireframe)
			- [Income View Wireframe](#income-view-wireframe)
			- [Income Mobile View Wireframe](#income-mobile-view-wireframe)
		- [Site Screenshots](#site-screenshots)
			- [Landing Page Screenshot](#landing-page-screenshot)
			- [Summary View Screenshot](#summary-view-screenshot)
			- [Expenses View Screenshot](#expenses-view-screenshot)
			- [Income View Screenshot](#income-view-screenshot)
			- [Create Expense Screenshot](#create-expense-screenshot)
			- [Create Income Screenshot](#create-income-screenshot)
			- [edit Expense Screenshot](#edit-expense-screenshot)
			- [edit Income Screenshot](#edit-income-screenshot)
			- [Delete Expense Screenshot](#delete-expense-screenshot)
			- [Delete Income Screenshot](#delete-income-screenshot)
			- [User Registration Screenshot](#user-registration-screenshot)
			- [User Login Screenshot](#user-login-screenshot)
		- [Features](#features)
			- [Existing Features](#existing-features)
			- [Future Features](#future-features)
	- [Database Schema](#database-schema)
	- [Agile Methodology](#agile-methodology)
		- [MoSCoW Prioritization](#moscow-prioritization)
	- [Deployment](#deployment)
		- [Github](#github)
		- [Django](#django)
		- [PostgreSQL](#postgresql)
		- [Cloudinary](#cloudinary)
		- [Heroku](#heroku)
	- [Technologies Used](#technologies-used)
	- [Testing](#testing)
		- [Validator Testing](#validator-testing)
			- [HTML](#html)
				- [HTML Results](#html-results)
		- [CSS](#css)
		- [PEP8](#pep8)
		- [Python](#python)
	- [Manual Testing](#manual-testing)
	- [Automated Testing](#automated-testing)
- [Credits](#credits)
	- [Content](#content)

## UX User Experience

### User Stories

#### Product Owner:

- As a Product Owner, I want to see that my site is working properly on different devices, so users will have the best experience.
- As a Product Owner, I want to display a clear and intuitive navigation menu, so it will be easier for the User to navigate through the website.
- As a Product Owner, I want to provide users with a comprehensive overview of their financial situation, so they can make informed decisions about their spending and saving habits.

#### Site Administrator:

- As an Admin, I want to add/update/delete the information on the income and expenses pages, so the user can manage their finances effectively.
- As an Admin, I want to approve or disapprove user-generated content, so that I can filter out objectionable content.

#### Site User:

- As a User, I want to easily navigate through the website, so I would have a positive experience.
    - As a User, I want to know on which page I am, so it will be easier to navigate through the site.
    - As a User, I want to see a summary of my income and expenses, so I can understand my financial situation.
    - As a User, I want to add, edit, and delete my income and expenses, so I can keep my financial records up to date.
    - As a User, I want to register an account, so I can securely manage my financial data.
    - As a User, I want to see if I am logged in or not, so I will have a positive UX.

### Site Design

The design of Spinning Plates Budgeter is inspired by modern financial management tools such as YNAB. The goal is to create a clean, intuitive, and user-friendly interface that allows users to manage their finances with ease.

initial the site was created to mirror the look and feel of a prototype developed in a spreadsheet. The spreadsheet prototype helped understand the data required to transfer between views as well as the concept of the main page of the site.

![Initial Site Concept Design](docs/design-concept/Initial_Site_Concept.webp)

#### Design Framework

The framework of the site was built upon Bootstrap 5 Grid system with header and footer elements utilising MBD UI.

#### Colour

The primary colours used in the design were intended to be muted and utilised shades of grey, off-white, and blue. This was intentionally chosen to create a calming and professional atmosphere, in keeping with a finance based site/app.

#### Font

The site uses [Google Font](https://fonts.google.com/), "Roboto" as a default and "Sans serif" as a backup font.

### Wireframes

This section details the wireframes created for the project. The wireframes were created using Balsamiq and are intended to provide a visual representation of the site's layout and design.

#### Landing Page Wireframe

![Landing Page Wireframe](docs/design-concept/Landing_Page_Wireframe.png)

#### Summary View Wireframe

![Wireframe](docs/design-concept/Summary_Page_Wireframe.png)

#### Expenses View Wireframe

![Wireframe](docs/design-concept/Expenses_VIew_Wireframe.png)

#### Expenses Mobile View Wireframe

![Wireframe](docs/design-concept/Expenses_Mobile_View_Wireframe.png)

#### Income View Wireframe

![Wireframe](docs/design-concept/Income_View_Wireframe.png)

#### Income Mobile View Wireframe

![Wireframe](docs/design-concept/Income_Mobile_View_Wireframe.png)

### Site Screenshots

The following screenshots provide a visual representation of the site's layout and design.

#### Landing Page Screenshot

![Screenshot](docs/features/landingPageView.png)

#### Summary View Screenshot

![Screenshot](docs/features/summaryView.jpeg)

#### Expenses View Screenshot

![Screenshot](docs/features/expenseView.jpeg)

#### Income View Screenshot

![Screenshot](docs/features/incomeView.jpeg)

#### Create Expense Screenshot

![Screenshot](docs/features/create-expense.jpeg)

#### Create Income Screenshot

![Screenshot](docs/features/create-income.jpeg)

#### edit Expense Screenshot

![Screenshot](docs/features/editExpenseView.jpeg)

#### edit Income Screenshot

![Screenshot](docs/features/editIncomeView.jpeg)

#### Delete Expense Screenshot

![Screenshot](docs/features/deleteExpenseView.jpeg)

#### Delete Income Screenshot

![Screenshot](docs/features/deleteIncomeView.jpeg)

#### User Registration Screenshot

![Screenshot](docs/features/registerView.png)

#### User Login Screenshot

![Screenshot](docs/features/loginView.png)

#### User Logout Screenshot

![Screenshot](docs/features/logoutView.jpeg)

#### Admin Screenshot

![Screenshot](docs/features/adminView.jpeg)

## Features

This section details the existing and planned features for the site.

### Existing Features

The site has the following features:

- View Budget Summary
  - Provides an overview of the user's financial situation, including total income and total expenses.
  - Provides detailed reports on income and expenses, including charts and graphs for better visualization.
  - Allows the User to view expenses as a percentage of income
  - Allows the User to view chart in 4 different styles (line, pie, bar, doughnut)
- View Income Details
  - Allows users to add, edit, and delete income entries.
  - Allow the user to add a description to the income entry
  - Allow the user to add a date to the income entry
  - Allow the user to add a custom categories to the income entry or select from a predefined list.
  - Provides detailed reports on income and expenses, including charts and graphs for better visualization.
  - Allows users to see an aggregated total of income by income source
  - Allows the User to view chart in 4 different styles (line, pie, bar, doughnut)
  - Allows Users to Export table views to clipboard copy, print dialog, pdf, csv, Excel spreadsheet
- View Expenses Details
  - Allows users to add, edit, and delete expense entries.
  - Allow the user to add a description to the expense entry.
  - Allow the user to add a date to the expense entry.
  - Allow the user to add a custom categories to the expense entry or select from a predefined list.
  - Provides detailed reports on income and expenses, including charts and graphs for better visualization.
  - Allows users to see an aggregated total of expenses by category.
  - Allows the User to view chart in 4 different styles (line, pie, bar, doughnut).
  - Allows Users to Export table views to clipboard copy, print dialog, pdf, csv, Excel spreadsheet.
- User Authentication
  - Users can register, log in, and log out. Once authenticated, they can securely manage their financial data.
  - Restricts Users to viewing their own financial information.
- Responsive Design
  - The application is fully responsive and works seamlessly on different devices, including desktops, tablets, and mobile phones.

### Future Features

The planned future features for this project include:

- Adding the ability to repeat income/expenses to a user specified time frame (daily, weekly, monthly, yearly)
- Allow Users to archive their monthly data
- Extend views via accordion dropdown to collapse monthly income/expense details
- Extend views to include year
- incorporate income/expenses trends view
- Allow users to set budget goals and track their progress.
- Send notifications to users for important events, such as upcoming bills or low balances.
- Extend the functionality to incorporate the YNAB 'every dollar needs a job' approach to budgeting.
- Allow users to define their starting balance as part of the registration process, in addition to being able to edit it via the profile page.
- Allow users to update their preferences (currencies, budgeting approach, etc.)

## Database Schema

The Entity-Relationship Diagram (ERD) for Spinning Plates Budgeter showcases the connections between users, income, and expenses. This diagram is crucial in visualizing the relationships among various models within the PostgreSQL database.

The following diagram provides a visual representation of the initial database schema representative of the initial concept design.

![ERD Diagram](docs/erd/INITIAL-Spinning-Plates-Budgeter-ERD.jpeg)

The following ERD diagram was generated using PgAdmin and provides a visual representation of the database schema for the project.

![ERD Diagram](docs/erd/PgAdmin.pgerd_Spinning-Plates-Budgeter-ERD.png)

## Agile Methodology

I used my [Github Projects Board](https://github.com/users/student0Zero/projects/5) to plan and document all of my work. This helped me to organize tasks, track progress, and ensure timely completion of the project.

Kanban View:
![Project Board](docs/agile/projectBoard_1.png)

MoSCoW View:
![Project Board](docs/agile/projectBoard_2.png)

### MoSCoW Prioritization

The MoSCoW Prioritization method was used for Spinning Plates Budgeter project board, identifying and labeling my user stories as:

- **Must Haves:** the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
- **Should Haves:** the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves:** these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves:** the features or components that either no longer fit the project's brief or are of very low priority for this release.
## Deployment

### Github
To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. I used Gitpod as the IDE and generated a new workspace using it for the project.
6. Once the workspace is created, you can clone the repository to your local workspace using the following command in the terminal: `git clone.

### Django
1. Install Django and supporting libraries:
- `pip3 install 'django<4' gunicorn`
- `pip3 install dj_database_url psycopg2`
- `pip3 install dj3-cloudinary-storage`

2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the `pip3 freeze --local > requirements.txt` command in the terminal.

3. Create a new Django project in the terminal `django-admin startproject spinning-plates-budgeter .`

4. Create a new app eg. `python3 mangage.py startapp review`.

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

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: `web: gunicorn spinning-plates-budgeter.wsgi`

12. Make the necessary migrations again.

### PostgreSQL

The generation of a PostgreSQL database is required for this project. The database is hosted on Heroku and is linked to the project via the **DATABASE_URL** environment variable.

I used the following steps to set up the database:

- Install PostgreSQL: `pip3 install psycopg2-binary`
- create a new database using CI Database Maker, which once created will provide the following details which need to be added to the **env.py** file:
- database name
- database host
- database username
- database password
- database url

I transferred the database details to the **env.py** file and added the **DATABASE_URL** to the **settings.py** file.

In addition to PostgreSQL, I used PgAdmin to manage the database and create the ERD diagram for the project. The ERD diagram was then used to create the models for the project. PgAdmin can be downloaded from the [official website](https://www.pgadmin.org/). I installed it on a Windows machine and connected it to the PostgreSQL database hosted on Heroku.

### Cloudinary

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

### Heroku

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

## Technologies Used

The following technologies were used for this project:

- HTML5
- CSS
- asgiref: 3.8.1
- black: 24.10.0
- click: 8.1.7
- cloudinary: 1.41.0
- crispy-bootstrap5: 2024.10
- dj-database-url: 0.5.0
- dj3-cloudinary-storage: 0.0.6
- Django: 4.2.16
- django-allauth: 0.57.2
- django-crispy-forms: 2.3
- django-widget-tweaks: 1.5.0
- gunicorn: 20.1.0
- oauthlib: 3.2.2
- pathspec: 0.12.1
- psycopg: 3.2.3
- PyJWT: 2.10.0
- python3-openid: 3.2.0
- requests-oauthlib: 2.0.0
- sqlparse: 0.5.2
- urllib3: 1.26.20
- whitenoise: 6.5.0
- Github
- Github Projects
- Heroku

You can refer to the requirements.txt file for a full list of dependencies used in this project.

## Testing

### Validator Testing
I used the following validators to test the project:

#### HTML

It is not possible to use the W3C markup validator service ([HTML W3C Validator](https://validator.w3.org)) for HTML validation without customising the code, due to the errors generated as a result of [jinja syntax](https://documentation.bloomreach.com/engagement/docs/jinja-syntax). The following steps were used to customise the html code to prepare it for w3c validation:

1. from the live Heroku site use the browser console to 'view page source' and copy the html code.

2. paste the code into [validate by input](https://validator.w3.org/#validate_by_input) option.

##### HTML Results

Two of my html files failed validation due to the use of JavaScript configuration scripts used for the DataTable.js and Chart.js libraries. Specifically, the failures occurred in the view_expenses.html, view_income.html, and summary.html files. 

The errors (screenshots below) are due to duplicate id's for the chart names. The chart names are required by the configuration script to target the correct canvas element for the chart to be displayed. The errors are not critical and do not affect the functionality of the site.

view_expenses.html - Validation Error Screenshot
![expenses_validation_error](docs/testing/w3c_htmlChecker_expensesViewResult.png)

view_expenses.html - Validation Error details
![expenses_validation_error](docs/testing/w3c_htmlChecker_expensesViewDetails.png)

view_income.html - Validation Error Screenshot
![income_validation_error](docs/testing/w3c_htmlChecker_incomeViewDetails.png)

view_income.html - Validation Error Details Screen Shot
![income_validation_error](docs/testing/w3c_htmlChecker_incomeViewResult.png)


The remaining html files passed validation with no errors with validation results located within the project folder at docs/testing.

#### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. The css test passed with no errors. 

![css_results](docs/testing/w3c_cssChecker_base.css_Result.jpg)


#### PEP

black.py was used to ensure PEP8 compliance for all python code on the project.

#### Python

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. There were some issues with the line lengths in the views.py file which were corrected. The results can be found in the project folder at docs/testing/python-linter-results.

#### Lighthouse 

Mobile Site Tests

Desktop Site Tests


### Manual Testing

The table below provides details of manual testing performed on the sites functionality.

| **Feature**      | **Login** | **Logout** | **Register** | **Create** | **Update** | **Edit** | **Delete** |
| ---------------- | --------- | ---------- | ------------ | ---------- | ---------- | -------- | ---------- |
| landing_view     | Pass      | Pass       | Pass         | N/A        | N/A        | N/A      | N/A        |
| summary_view     | Pass      | Pass       | N/A          | N/A        | N/A        | N/A      | N/A        |
| expenses_view    | Pass      | Pass       | N/A          | Pass       | Pass       | Pass     | Pass       |
| income_view      | Pass      | Pass       | N/A          | Pass       | Pass       | Pass     | Pass       |
| Profile Dropdown | Pass      | Pass       | Pass         | N/A        | N/A        | N/A      | N/A        |

### Automated Testing

The table below provides details of automated testing performed on the site. test.py were created to test the CRUD functionality of the site. The tests were created using the Django test framework and were run using the command `python3 manage.py test`.


| **Feature**           | **Create Test User** | **Create** | **Edit** | **Delete** |
| --------------------- | ------------------- | ---------- | -------- | ---------- |
| expenses_view test.py | Pass                | Pass       | Pass     | Pass       |
| income_view test.py   | Pass                | Pass       | Pass     | Pass       |

## Credits

<hr>

The site concept was inspired by the iconic [YNAB](https://www.ynab.com/) and the money blog [MicahelSaves](https://michaelsaves.com/budgeting/google-sheets-budget-template/). The given the timescales and the complexity of coding a site similar to YNAB, I created a site which currently serves as a foundation upon which I can build towards achiving my origianl intent of replication the YNAB approach to budgeting.

The site site borrows its user authentication approach from the CI Blog walkthrough project.

### Content

- The CDN framework used for ready-made styling was [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/download/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- [Balsamiq](https://balsamiq.com/) used for wireframe.
- Github copilot was used to help debug the DataTable.js, Chart.js configuration files, as well as for debugging automated tests.
- Bootstrap 5 examples were used to help with the layout of the site. Specifically I used the [Pricing](https://getbootstrap.com/docs/5.3/examples/pricing/) example to help with the layout of the summary page, and [heroes](view-source:https://getbootstrap.com/docs/5.3/examples/heroes/) example to help with the layout of the home page.
