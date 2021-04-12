https://nevermisslist.herokuapp.com/

# Never Miss List
<p>Never Miss List is a user friendly todo list application. Meant to be simple enough for anyone to use,
regardless of age, experience, and background
Give the user the ability to create an event with a description and due date.
Once the date is passed the item will be automatically removed</p>

<h3>Mission</h3>
<p>Our mission is to provide the most user friendly todo list application
Which anyone can use for FREE
A tool that even my forgetful and not so technically sound parents can use</p>

## Local Installation
To install this on your own machine, follow these instructions:
- ```git clone``` the repository
- initialize the virtual environment and activate it:
  - note: *you can set this up with another name, such as ``.venv``*
```bash
$ python3 -m venv .env
$ source .env/bin/activate
```
- install the requirements:
```bash
$ pip install -r requirements.txt
```
- create your (postgres) database:
```bash
$ createdb <DB Name>
```
- run migrations:
```bash
$ python manage.py migrate
```
- boot up your local server!
```bash
$ python manage.py runserver
```

<h2>Technologies Used</h2>
<ul>
<li>HTML</li>
<li>CSS</li>
<li>materialize css</li>
<li>Python</li>
<li>Django</li>
<li>materialize css</li>
<li>Postgres</li>
<li>Heroku</li>
<li>Javascript</li>
</ul>

<h2>Features</h2>
<ul>
<li>As a user I would like to sign up and sign in </li>
<li>As a user I would have a profile after user created</li>
<li>As a user I would to edit profile information</li>
<li>As a user I would like to have a personal todo list on profile</li>
<li>As a user I would like to create an event with title, description, time, and date</li>
<li>As a user I would like to edit an event </li>
<li>As a user I would like to delete an event from list</li>
<li>As a user I would to be able to change my password</li>
<li>As a user I would have events ordered by upcoming date</li>
</ul>

<h2>Homepage</h2>
<img width="1438" alt="Screen Shot 2021-04-11 at 8 08 01 PM" src="https://user-images.githubusercontent.com/46904236/114335463-ab87ac00-9b01-11eb-879f-ed1d59a3d2e8.png">

<h2>Profile Page</h2>
<img width="1431" alt="Screen Shot 2021-04-11 at 8 10 33 PM" src="https://user-images.githubusercontent.com/46904236/114335614-00c3bd80-9b02-11eb-94da-243c58432877.png">

<h2>Future Features</h2>
<ul>
<li>As a user I would add profile pic </li>
<li>As a user I would to have a default profile pic</li>
<li>As a user I would have an email confirmation </li>
<li>As a user I would to add pretty urls</li>
<li>As a user I would to have an email validation and password validation </li>
</ul>
