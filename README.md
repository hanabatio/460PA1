# 460PA1
A Restaurant Review Database and WebApp <br>
Hana Batio - hbatio@bu.edu
Juan Santana - jsanta21@bu.edu

<h1>Project Specs:</h1>

Your web application should be able to connect to the database and retrieve data from <br>
it. You can use the tools you are most comfortable with. The image has preinstalled the <br>
PostgreSQL system and a web server. The final deliverable is expected to: <br>
  <p style="margin-left:10%; margin-right:10%;">
  • Have a web-based graphical interface that will facilitate the communication with <br>
  the database and the presentation of the contents. <br>
  • Have the functionality to insert and delete data from the database. Specifically: <br>
</p>
    <p style="margin-left:20%; margin-right:20%;">
    o Insert/delete/update a restaurant <br>
    o Insert/delete/update a user <br>
    o Insert/delete/update a review <br>
    o Insert/delete a checkin <br></p>
    <p style="margin-left:10%; margin-right:10%;">
  • Enable the interested user to ask arbitrary SQL queries. <br>
  • Have a web-based interface that will execute the queries of part 2 and visualize <br>
  the results. <br>
</p>
<h1>Functionality</h1>

To use our application, you must install python, flask, flask-sqlalchemy, and flask-wtforms. You must also create a postgre sql database using the provided CSV files (or files of the same format). <br>

<h1>Design Choices</h1>

We decided not to add functionality for deleting a Check-in as we did not think that it made logical sense given the set-up of our web app. As far as User Queries, we decided to only allow users to search for businesses within the app. An extension would be to add functionality for users to search for other users or reviews or businesses that they were interested in.