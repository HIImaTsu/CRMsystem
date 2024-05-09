## continental - CRM-system for hotel

1. A graphical CRM system for automating work when making reservations and rooms. This project allows the hotel's internal staff to make advance reservations, as well as monitor the arrival, departure and stay of the guest, tracking the payment. Thanks to the system, each department of the hotel (for example, the booking department, the housekeeping service, the reception desk) can be assembled in one system and make reports on the data stored in the database. A simple interface and intuitive functionality will ensure the convenience and flexibility of working with this system.


2. You can check the performance of our website via the address: http://13.51.5.143/
3. Logins to log in:
   
- user1: adilet
pass: 12345678abc

- user2: almir
pass: abc12345678

4. If you have any questions, please contact me at 200103319@stu.sdu.edu.kz

# FRONT-END

bookingpage.html:
   - This file is responsible for the room reservation page. Here users can view available rooms, add new bookings, edit existing bookings and cancel them if necessary.
     
reservationpage.html:
   - This file is responsible for the page for creating a new reservation. Here users can specify information about guests, select dates of stay, specify the price of rooms and other booking details.

nightauditpage.html:
   - This file is responsible for the overnight audit page at the hotel. Here, administrators can view data on current bookings, income, available rooms and other information necessary to analyze the operation of the hotel.

accountpage.html:
   - This file is responsible for the user account management page. Here users can edit their personal data, change passwords and manage other settings of their account.

Functionality
- Room Reservations: Users can view available rooms, add new bookings, edit and cancel them.
- Create a new reservation: Users can specify information about guests, dates of stay and other details to create a new reservation.
- Night audit: Administrators can view data on current bookings, income and other statistics to manage the operation of the hotel.
- Account Management: Users can edit personal data, change passwords and manage their account settings.

  # BACK-END

  Structure: 2 applications. 
- The first application, Continental, was created by Django himself for the configurations and settings of our project and subsequent work with the server. 
- The second application, Hotel, is already the main content of the functionality of the entire project, it was decided not to share the part with the login for easier work with the application itself. Directories with project templates and static files, and pictures, scripts and styles are created inside it.
- New folders were created inside the static and templates directories to store files in them, this was created so that when the project was uploaded and the project was deployed on the hosting, static files and templates of different applications would not mix and there would be an understanding of which applications the files belong to (if additional applications are created in the future). 
- serializers.py – It is necessary to convert data from models to json format for some scripts and functions to work (mainly for the armor placement page).
- urls.py - a file with routes for processing specified requests to the server
- views.py - MTV pattern (Models, Views, Templates) - views that are responsible for how the page requested by the user should look like 
- models.py - a file with data tables, an important part of the CRM system
- forms. py file for working with forms
   
