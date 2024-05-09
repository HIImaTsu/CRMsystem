# CRM System for Hotel Management

## Project Description
This graphical CRM system automates processes related to booking and room management. It allows the hotel's internal staff to make advance reservations, monitor guest arrivals, departures, and stays, and track payments. The system integrates various hotel departments (such as booking, housekeeping, and reception) into a single system, enabling data-driven reporting. Its simple interface and intuitive functionality ensure ease and flexibility of use.

## Website Performance Check
You can check the performance of our website at: [http://13.51.5.143/](http://13.51.5.143/)

## Installation and Setup

### 1. Cloning the Repository
Clone the repository to your computer:
```bash
git clone https://github.com/HIImaTsu/CRMsystem.git
cd CRMsystem
```

### 2. Setting Up the Virtual Environment
- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  ```bash
  venv\Scripts\activate
  ```

### 3. Installing Dependencies
Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 4. Running the Server
Navigate to the `CRMsystem\continental` directory and start the server:
```bash
python manage.py runserver
```

## Login Credentials
- **User 1:**
  - Username: adilet
  - Password: 12345678abc

- **User 2:**
  - Username: almir
  - Password: abc12345678

## Contact
If you have any questions, please contact me at [200103319@stu.sdu.edu.kz](mailto:200103319@stu.sdu.edu.kz)

This text can be copied directly into your README.md file. It includes all the necessary instructions and is formatted for ease of use and clarity, specifically tailored for users on Windows operating systems.

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
   
