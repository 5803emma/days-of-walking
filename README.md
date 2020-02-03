# Code Institute - Milestone 3 Project - Data Centric Development

# Out and About - Walks in Ireland 

* This web application allows visitors to create, read, update and delete database records about different walking routes around Ireland. 
* The intention is to grow the database of walking routes through user interaction with the application.  
* Visitors can also post their own reviews of existing walking routes on the database.

## UX

The app has been designed with all types of users in mind.  
* Expert walkers and hikers might be keen to contribute their knowledge of both popular and lesser known routes to the database, thereby growing the app database and populating the collections.  
* Other users might be curious about what types of walking routes are in their locality, and they may visit the app to read the database entries and the route reviews.  
* Some visitors may use the app to post reviews about existing walking routes, providing a layer of subjective date for visitors.  
* Hopefully, the app is informative, responsive and easy to navigate for all users.  

### User Stories:
As a new user of the application, I would like to be able to:
* understand how to navigate the application, it should be intuitive.
* understand how to create my own record of a walking route.
* easily find information about walking routes in Ireland.
* easily update information about a walking route if I believe it to be incorrect or obsolete.
* write a review about a walking route to inform other users about my experience of the walk.

### Wireframes: 
Wireframes were created in MS Paint and can be found in the static/wireframes folder of this repository.


## Features
* Users can create, read, update and delete records of walking routes around Ireland.  
* Users can add and edit pertinent details of a walk; the name of the route, it's location, the length of the walk, whether it is easy, moderate or difficult, and the type(s) of terrain a walker is likely to encounter.
* Users can review walks that exist in the database.

### Potential Future Features
* User registration and login functions to encourage participation and engagement.
* User authentication to add a layer of security against malicious or spam posts.
* Float option instead of string input for length of walk to increase accuracy and consistency of data production.
* Url image upload option for users to post images of the routes.

### Layout

* The home page is landing page for the application. 
* It contains a data table which displays records from a MongoDB Atlas database. 
* The Bootstrap Jumbotron contains text which explains the information in the table, and how the user can go about making changes to the database.
* There are links in the right hand navigation bar to other destinations on the app.  
** The About section contains a brief paragraph of information about walking in Ireland.  
** The Add a Walk link brings the user to a page where they can create a record of a walking route.  
** The Review Walk link brings the user to a page where they can review a walking route.  
** The Read Reviews link brings them to a page of reviews which have been posted by other users. 

### Existing Features
* Navigation Bar - The top left link contains the application title and in every instance it will return the user to the landing page containing the database of walks. On the right hand side of the navbar the user can click on page links and navigate to About, Add Walk, Review Walk and View Reviews. 

* Create Walk - In the navigation menu, users are invited to populate the required fields and add their walk to the database. If they choose to submit their walk, they then are redirected to the home page where they can view the entry that they have submitted.

* Edit Walk - In the data table rows, the names of walking routes are buttons.  The welcome text in the Jumbotron explains that clicking on a Walk Name button will bring the user to the record of that particular walk.  The record is form which displays the attributes of the selected walk. The user can make changes to the record and submit the form which then updates the database record. There is also a red delete button at the bottom of the form.  Using this, the user can delete the walk from the database.  If the user selects the delete option, a Bootstrap modal appears to query if they are sure that they want to delete the record.  The user can then confirm that they wish to delete the record, or say no and return to the edit page.

* Review Walk - Users can review walks that are already in the database via this link and submit their review on a particular walk to the database via a form.  If the walk is not in the database, the user will not be able to review that walk, without adding a record of same. User reviews are displayed on the View Reviews page and the review is saved in a collection.

## Technologies Used

The following technologies were used in this project:
* HTML
* CSS
* Javascript
 * [Python](https://www.python.org/)
 * [Flask](http://flask.pocoo.org/)
 * [Mongodb](https://www.mongodb.com/)
 * [Bootstrap](https://getbootstrap.com/)
 * [Jquery](https://code.jquery.com/jquery-3.2.1.js)
 * [Font Awesome library](https://fontawesome.com/)
 * [Google Fonts](https://fonts.google.com/)

## Testing

### User Testing

Chrome developer tools, android phone and iphone, ipad and android tablets were used to test the appearance of website on mobile/tablet screen size.  
Manual tests were carried out to verify that all links and routes were operational


## Deployment

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/deevdz/milestone-project-3](https://github.com/deevdz/milestone-project-3)

Heroku App Location is as follows [https://deevdz-milestone-3.herokuapp.com/](https://deevdz-milestone-3.herokuapp.com/)

Following steps were taken to deploy the website:
1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in Cloud 9. In this workspace: Flask was installed - `sudo pip install flask`.
3. Setup app.py file and imported flask and os - `from flask import Flask. import os`
4. Created an instance of flask - `app = flask(__name__)`
5. Tested the connection as proof of concept. `CLI - show collections` (prove connection)
6. Inside the app run() function set the host, ip and debug=true
7. Create a new Heroku App - unique name and EU Server
8. In cloud 9 login to Heroku through CLI to confirm existance of app. `CLI: heroku login. CLI: heroku apps`.
9. Create a git repository in cloud9. CLI: git init. `CLI: git add . CLI: git commit -m "Initial Commit"`
10. Connect cloud9 to Heroku. Use code found on Heroku. `CLI - $heroku git remote -a deevdz-milestone-3`
11. Create requirements.txt file - `CLI: sudo pip3 freeze --local > requirements.txt`
12. Create Procfile - `echo web:python app.py>Procfile`
13. Add and Commit to Git Repository
14. Push to Heroku using code supplied by Heroku
15. `CLI - heroku ps:scale web=1` Command to tell Heroku to run the app
16. Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI
17. Get Flask to talk to MongoDB - `CLI: sudo pip3 install flask-pymongo` `CLI: sudo pip3 install dnspython`
18. Add extra libraries to app.py - `from flask_pymongo import Pymongo` `from bson.objectid import ObjectID`
19. Add DB connection code to app.py - edit bashrc file to keep details private.
20. Test connection to DB again to confirm it's working
21. Confirm that the cloud9 runner is set to python 3
22. Connect GitHub repository to Heroku using code provided by heroku and github.
23. Set Debug to False

Credits
-----------------------------------------
**Content**

All site recipes and images are sourced from [BBC Food](https://www.bbc.com/food/recipes) and [Pinterest](https://www.pinterest.ie/).

#### Manual User testing:
This was the primary method of testing the application. People were asked to visit the website on a variety of devices, and to enter information to the database. This feedback was very uselful to determine any bugs that may have been present. I also tested the app manually myself on a varietly of browsers. 


### Below are the list of Internet Browsers that were used to test the display of the website:

1. Google Chrome (Version 77.0)
    * Chrome Lighthouse was used to audit the website.
2. Mozilla Firefox (Version 69.0)
3. Microsoft Edge (Version 44.1)
4. Internet Explorer 11 (Version 11.8)

Manual testing was carried out using the above browsers. No bugs or desplay issues could be identified. 

### Below are the list of websites I used to test the HTML, CSS and JS code:

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.
3. [CSS Lint](http://csslint.net/) CSS Lint is an open source CSS code quality tool I used.

#### Meeting the needs of the user stories (as described in the UX section of this README file)

#### As a new User to the web application, I want to be able to understand how to navigate around the web application.

Upon landing on the home page, the user is greeted with a jumbotron welcome text, imediately followed below by the subject of the application: The Data Table. The user doesn't have to go searching for it, as it's right there.  There is an explanation on the home page that the user can view and edit a walk by clicking on any of the buttons corresponding to Walk Names in the data table.

Navigation comes from the Navigation Bar at the top of the page. The Logo, when clicked, will redirect the user back to the home page. The rest of the Nav Bar items are positioned on the right hand side. They visually tell the user exactly what they can do. Each item, when clicked, redirects the user to a seperate page where the desired action can occur.

#### As a new User to the web application, I want to be able to add additional information to the river database...

Under "Add a new River" on the Nav Bar, the user will be redirected to a new page where the user can add a new document to the collection in the database.


#### As a new User to the web application, I want to be able to update a particular river's information if I believe it to be inaccurate, incorrect or outdated.

On the data-table displayed on the home page, there is a blue button in the first row. As explained on the welcome message on the top of the home page, when this button is clicked for that particular river, the user is redirected to a new page, where a pre-polulated form is, and the user can edit and make changes to this river record. At this point, there is also an option to delete the document entirely from the collection, in the form of a red button at the bottom of the form.

#### As a new User to the web application, I want to leave a review about a particular river, which is both informative and allows me to broadcast my own opinion.

"Review a River" is an item on the Nav Bar. Once clicked, the user is brought to a new page, where, via a form, they can leave a review about a particular river in the database. Once the review is submitted, the user can view what they have posted to the database on the "Read Reviews" page. Other users can also view this page, providing insight and knowledge from other users.


## Deployment

### Local Deployment

This project was developed using the AWS Cloud 9 IDE.  It was pushed to Github and deployed to Heroku.

The GitHub Repository can be found here: https://github.com/haydal810/Milestone-Project-3
The live application can be viewed here: https://kerry-rivers-ms3.herokuapp.com/

To deploy this project on your own IDE, folow the steps below:

 Firstly, ensure of the following:
    - You have an IDE, such as VS Code
    - The following must be installed locally on your computer:
            - git
            - PIP
            - Python 3
            - Flask
            - A MongoDB Atlas account

Instructions for Installation:

1.  Make your own folder and navigate to it on the terminal. Then enter the following in the terminal:

```
$ git clone https://github.com/haydal810/Milestone-Project-3.git
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
2.  To run the app locally:

```
$ python -m flask run
```

### Heroku Deployment

The code was also pushed from git to heroku for live deployment: https://www.heroku.com/ 

To Deploy using Heroku Git, use git in the command line:

1.  Install the Heroku CLI. If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

2.  Clone the repository. Use Git to clone the projects source code to your local machine.

```
$ heroku git:clone -a kerry-rivers-ms3
$ cd kerry-rivers-ms3
```
3.  create your requirements.txt file

```
$ pip freeze --local > requirements.txt

```
4.  create your procfile file

```
$ echo web: python app.py > Procfile

```

5.  Deploy your changes. Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "commit message"
$ git push heroku master
```
6.  In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7.  Set the following config vars:

```
IP : 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
```
To get your MONGO_URI read the MongoDB Atlas documentation: [HERE](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click on the button "Open App".