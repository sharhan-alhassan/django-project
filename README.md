# django-project


**Note for git**
- git init 
- git remote -v 
- git remote add origin <url>
- git pull origin main --allow-unrelated-histories
- git add . 
- git commit -m "msg"
- git push origin main

# Run server 
1. python manage.py runserver OR
2. ./manage runserver

## NOTES:
### The path() function is passed 4 arguments
- Two required: route and view
- Two optional: kwargs and name

### python manage.py migrate: 
*This command looks at the INSTALLED_APPS in mysite/settings.py and creates any necessary Databases tables according to the Database settings*

## Creating models: 
Essentially create Database Layout with additional metadata
1. In this Poll app, we will create two models:
- Question model: Has a question and a publication date
2. Choice model: Has 2 fields
    - The text of the choice
    - A vote tally
3. Each Choice is associated with a Question 
All these are represented by Python Classes
## NB:
- The name of each Field instance 
(e.g. question_text or pub_date) is the field’s name, 
in machine-friendly format. You’ll use this value in 
your Python code, and your database will use it as 
the column name.

## Activating models
- Philosophy:
Django apps are “pluggable”: You can use an app in 
multiple projects, and you can distribute apps, 
because they don’t have to be tied to a given 
Django installation.
- To include the app in our project, we need to 
add a reference to its configuration class in the 
INSTALLED_APPS setting. The PollsConfig class is 
in the polls/apps.py file, so its dotted path 
is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file 
and add that dotted path to the INSTALLED_APPS setting

- python manage.py makemigrations polls : This tells 
Django you've made changes to your models(In this case we've
made our first Models)

- You can fine you human-readable and editable form of 
the Databae in polls/migrations/<filename> //0001_initial.py

- python manage.py sqlmigrate polls 001 (filename): This command gives 
human-readable form of what Database is going to be created 
from the model

## NB:
- The sqlmigrate command doesn’t actually run the migration 
on your database - instead, it prints it to the screen so that 
you can see what SQL Django thinks is required. It’s useful 
for checking what Django is going to do or if you have database 
administrators who require SQL scripts for changes.

- python manage.py check: This checks for any problems
in your project without making migrations or touching 
the Database

## NB:
Remember the three-step guide to making model changes:

1. Change your models (in models.py).
2. Run python manage.py makemigrations <app-name> to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.

## Playing with the python shell API
- python manage.py shell

- It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.

## Django Admin
- python manage.py createsuperuser //to create
username: admin
email: sharhanalhassan@gmail.com
password: mohammed

## Make the poll App modification in the admin
- We need to tell the Admin that Question objects have 
an admin interface.

## Views
- Each view is responsible for doing one of two things:
1. return an HttpResponse containing content for requested page
2. Or raising an exception such as Http404 

## NB: 
- Views can read records from Database or not
- It can use a template system such as Django's or third party python 
template system -or not 
1. in this poll application, we’ll have the following four views:

- Question “index” page – displays the latest few questions.
- Question “detail” page – displays a question text, with no results but with a form to vote.
- Question “results” page – displays results for a particular question.
- Vote action – handles voting for a particular choice in a particular question.

## TEMPLATES
- The render() function takes the following 
1. request object as first argument 
2. template name as second argument 
3. dictionary as its optional third argument 
'''