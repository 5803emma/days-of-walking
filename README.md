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

* The home page is landing page for the application and the text in between the font awesome icons in the top left hand corner of the app contains a link to the home template. 
* The app contains a data table which displays records from a MongoDB Atlas database. 
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
Manual tests were carried out to verify that all links and routes were operational.  A variety of different browsers were utilised.

### Code was Run Through the Following Validators

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.


## Deployment

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/deevdz/milestone-project-3](https://github.com/deevdz/milestone-project-3)

The site is deployed to Heroku and can be found [here]

Following steps were taken to deploy the website:
1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in Cloud 9.
3. Flask was installed in the Workspace.
4. Heroku accout was created
5. Git repository was created, commited and pushed to. 
6. Heroku app was created and pushed to.
7. Config Vars were added to Heroku
8. Flsak-Pymongo and dnspython were installed and linked.
9. Database connection was privatised using gitignore env.py
10. Debug set to False


## Addressing User Stories

#### As a new user of the application, I would like to understand how to navigate the application, it should be intuitive.

Upon landing on the home page, the user is greeted with a familiar navbar and a large banner of welcoming text.  On the same page, the Data Table is immediately accessible to the user.  There is an explanation on the home page that the user can view and edit a walk by clicking on any of the buttons corresponding to Walk Names in the data table.  Navigation comes from the Navigation Bar at the top of the page. The Logo, when clicked, will redirect the user back to the home page. The rest of the Nav Bar items are clearly labelled and they redirect the user to a seperate page of their choosing.

#### As a new user of the application, I would like to understand how to create my own record of a walking route.

"Add a Walk" on the app navbar directs the user to a form where they can create a record of a walking route.  This link is visible on all site pages.


#### As a new user of the application, I want to easily find information about walking routes in Ireland.

The data table on the home page provides information about walking routes in the database.  The Read Reviews section also provides more information about walks.

#### As a new user of the application, I would like to write a review about a walking route to inform other users about my experience of the walk

"Review Walk" is an item on the navbar which directs the user to a form where they can leave a review about a walk in the database. Once the review is submitted, the user can view what they have posted to the database on the "Read Reviews" page. Other users can also view this page.

