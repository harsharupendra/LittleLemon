# LittleLemon Project

## Project Description:
The **LittleLemon** project is a Django-based web application that provides APIs for managing restaurant bookings and menu items. The application is powered by Django REST Framework (DRF) and uses **Token Authentication** for user authentication. This project allows users to view, create, update, and delete booking and menu records and provides protected endpoints to secure user interactions.

## API Endpoints:
1. **User Endpoints** - **URL**: `/restaurant/users/` - **Method**: `GET` / `POST` - **Authentication**: Token Authentication - **Purpose**: Retrieve the list of users or create a new user. - **Headers**: Authorization: Token `<your_token>` - **Sample Request**: `POST /restaurant/users/ { "username": "newuser", "email": "newuser@example.com", "password": "password123" }` - **Sample Response**: `{ "url": "http://127.0.0.1:8000/restaurant/users/2/", "username": "newuser", "email": "newuser@example.com", "groups": [] }`

2. **Bookings Endpoints** - **URL**: `/restaurant/bookings/` - **Method**: `GET` / `POST` - **Authentication**: Token Authentication - **Purpose**: Retrieve the list of bookings or create a new booking. - **Headers**: Authorization: Token `<your_token>` - **Sample Request**: `POST /restaurant/bookings/ { "name": "John Doe", "no_of_guests": 4, "booking_date": "2024-10-20T18:30:00Z" }` - **Sample Response**: `{ "id": 1, "name": "John Doe", "no_of_guests": 4, "booking_date": "2024-10-20T18:30:00Z" }`

3. **Menu Endpoints** - **URL**: `/restaurant/menu/` - **Method**: `GET` / `POST` - **Authentication**: Token Authentication - **Purpose**: Retrieve the list of menu items or create a new menu item. - **Headers**: Authorization: Token `<your_token>` - **Sample Request**: `POST /restaurant/menu/ { "title": "Pizza", "price": 12.99, "inventory": 20 }` - **Sample Response**: `{ "id": 1, "title": "Pizza", "price": 12.99, "inventory": 20 }`

4. **Message Endpoint** - **URL**: `/restaurant/message/` - **Method**: `GET` - **Authentication**: Token Authentication - **Purpose**: A protected view that returns a custom message. - **Headers**: Authorization: Token `<your_token>` - **Sample Response**: `{ "message": "This view is protected" }`

5. **Token Authentication Endpoints** - **Login**: - **URL**: `/auth/token/login/` - **Method**: `POST` - **Purpose**: Log in using username and password to obtain a token. - **Body**: `{ "username": "Lemon", "password": "Lemon@123" }` - **Sample Response**: `{ "auth_token": "32620678b7c9af71e492924993d6d25fbd3359d6" }` - **Logout**: - **URL**: `/auth/token/logout/` - **Method**: `POST` - **Purpose**: Log out and invalidate the token. - **Headers**: Authorization: Token `<your_token>`

6. **API Token Auth Endpoint** (obtain a token) - **URL**: `/api-token-auth/` - **Method**: `POST` - **Purpose**: Obtain an authentication token by providing username and password. - **Body**: `{ "username": "Lemon", "password": "Lemon@123" }` - **Sample Response**: `{ "token": "32620678b7c9af71e492924993d6d25fbd3359d6" }`

7. **Djoser Authentication Endpoints** - **Register**: - **URL**: `/auth/users/` - **Method**: `POST` - **Purpose**: Register a new user. - **Body**: `{ "username": "newuser", "email": "newuser@example.com", "password": "password123" }` - **Login**: - **URL**: `/auth/token/login/` - **Method**: `POST` - **Body**: `{ "username": "Lemon", "password": "Lemon@123" }` - **Logout**: - **URL**: `/auth/token/logout/` - **Method**: `POST` - **Headers**: Authorization: Token `<your_token>`

## How to Run the Project: 1. Install dependencies: `pip install -r requirements.txt` 2. Run migrations: `python manage.py makemigrations` `python manage.py migrate` 3. Start the server: `python manage.py runserver`

## Testing APIs: - Use tools like **Postman**, **Insomnia**, or **cURL** to test the API endpoints. - You can also use the **DRF Browsable API** by navigating to the URLs in the browser.
