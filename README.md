# Configuration
a Django application that tracks track and field race results. The application contains the following templates:
Race, Athlete, and RaceResult

The athletics app is primarily designed to track race results and display those results to the public  
Users will need to log in to access results management, 
while visitors will be able to view race results offline.

1. Create views for authentication: Add views to allow users to log in, log out, and manage race results.
2. Configure permissions and restricted access: To ensure that only authenticated users can access results management, 
3. use the @login_required decorator on the corresponding views.
4. Create a superuser to manage the results: Use Django's createsuperuser command to create a superuser who can log in and manage race results.
# python manage.py createsuperuser

5. Create a group of users with access to results management 
 via the Django administration interface : Go to the "Groups" section and create a new group, for example, "Results Managers".
Add the desired users to this group.

6. Or via code
# Create the resultsmanagers group == "Results managers"

7. Create a custom decorator to check membership in the "Result Managers" group
# @group_required

# Assign users to group:
Add users to the "Results Managers" group via the Django admin panel.

Finalization:
You can add more features as you need:
such as adding users, forms for creating and editing races, athletes, and race results.

To find the right place to trigger sending emails to athletes who participated in a specific race:

Administration interface action: Ok
If an administrator needs to manually trigger the email sending process, 
you can add custom action in Django admin..

You define a custom action send_email_to_athletes that filters athletes by selected races and sends them emails.
This action is recorded in the RaceAdmin class and made available in the Django administration.


Form submission: OK
If there is a form on your site that, when submitted, should trigger the email sending process.

You create a SendEmailForm to select a race.
The send_email_view processes the form submission, filters athletes by selected race, and sends emails to them.
Templates send_email.html and email_sent.html provide the user interface for the form and confirmation page.

Automated task: Not yet implemented
If it is an automated task that needs to run periodically, 
consider using a task scheduler like Celery.

#  python3 -m venv env

#  source env/bin/activate

#  pip install django

#  pip freeze > requirements.txt

#  django-admin startproject athletics

#  cd athletics/
#  Configure Django to use a custom User model
#  python manage.py startapp authentication 
#  django-admin startapp races or python manage.py startapp races

# python manage.py makemigrations
# python manage.py migrate


# Envirements :

Links
* [https://github.com/m-dahmani/athletics.git]
* 
* https://www.linkedin.com/in/mohamed-d-a74627a9/


### → git clone git@github.com:m-dahmani/c.git

### → python3 -m venv env

### → source env/bin/activate

### → pip install -r requirements.txt 

### → python manage.py showmigrations

### → python manage.py migrate

### → python manage.py createsuperuser

#### → python manage.py runserver 0.0.0.0:8000









