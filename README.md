# Savory Dish Dash

**Savory Dish Dash** is a command-line interface (CLI) application designed for restaurant owners and managers to efficiently manage their menus and dishes. This application allows users to create, view, update, and delete menus and dishes, providing a straightforward way to maintain restaurant offerings.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [User Guide](#user-guide)
- [Logging and Debugging](#logging-and-debugging)
- [Contributing](#contributing)
- [License](#license)
- [Future Enhancements](#future-enhancements)

## Features
- **Menu Management**: Create, view, and delete menus for various meal periods (e.g., Breakfast, Lunch, Dinner).
- **Dish Management**: Add, view, and delete dishes associated with specific menus, including descriptions and pricing.
- **Intuitive CLI**: Navigate the application easily through text prompts and options.
- **Error Handling**: The application provides feedback on invalid inputs and actions, ensuring a smooth user experience.
- **Logging**: Track user actions and errors with a logging feature for debugging and record-keeping.

## Technologies Used
- **Python**: The primary programming language for building the application.
- **SQLAlchemy**: Used for Object-Relational Mapping (ORM) to interact with the database.
- **Alembic**: A lightweight database migration tool for managing database schema changes.
- **Pipenv**: A dependency management tool that simplifies the installation of packages and creation of virtual environments.
- **Faker**: (Optional) Used for generating fake data for testing and seeding the database.

## Installation
To set up **Savory Dish Dash** locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2.  **Install dependencies**: Make sure you have `pipenv` installed. Then run:
    
    bash 
    `pipenv install
    
    pipenv shell` 
    
3.  **Set up the database**: Initialize the database and run migrations:
    
    bash    
    `alembic upgrade head` 
    
4.  **(Optional) Seed the database**: To populate the database with initial data, run:
    
    bash
     `python lib/db/seed.py` 
    

## Usage

To run the application, execute the following command in your terminal:

bash
`python lib/cli.py` 

### User Interaction

Once the application is running, you will be presented with a menu of options. Here’s a breakdown of the interactions:

1.  **Creating Menus**:
    
    -   Choose the option to create a new menu.
    -   Enter the name of the menu when prompted.
    -   Confirmation of successful creation will be displayed.
2.  **Viewing Menus**:
    
    -   Select the view option to list all existing menus.
    -   Menus will be displayed in a readable format.
3.  **Creating Dishes**:
    
    -   Choose the option to add a dish to a specific menu.
    -   Provide the dish name, description, and price when prompted.
4.  **Viewing Dishes**:
    
    -   Select the option to view dishes in a specific menu.
    -   Dishes will be listed along with their details.
5.  **Deleting Menus and Dishes**:
    
    -   Choose the delete option for menus or dishes.
    -   Confirm the deletion action when prompted.

## Database Schema

The application employs a relational database to manage menus and dishes. Below is a detailed overview of the database schema:

### Tables

#### Menus

-   **id**: Integer, primary key, auto-incremented identifier for each menu.
-   **name**: String (VARCHAR), unique name of the menu (e.g., Breakfast, Lunch).
-   **created_at**: DateTime, timestamp indicating when the menu was created.

#### Dishes

-   **id**: Integer, primary key, auto-incremented identifier for each dish.
-   **menu_id**: Integer, foreign key referencing the `Menus` table, indicating which menu the dish belongs to.
-   **name**: String (VARCHAR), name of the dish.
-   **description**: String (TEXT), detailed description of the dish.
-   **price**: Float, price of the dish in the local currency.

### Relationships

-   A **Menu** can have many **Dishes**, establishing a one-to-many relationship between the `Menus` and `Dishes` tables.

## User Guide

### Starting the Application

1.  Open your terminal.
2.  Navigate to the project directory.
3.  Activate the Pipenv shell with `pipenv shell`.
4.  Run the application using `python lib/cli.py`.

### Example Commands

-   To create a Breakfast menu:
    -   Select "Create Menu" and enter "Breakfast".
-   To add a dish to the Breakfast menu:
    -   Select "Add Dish", choose the Breakfast menu, and provide the dish details.

### Exiting the Application

To exit the application, simply follow the prompt provided in the CLI menu.

## Logging and Debugging

The application includes a logging feature to track user actions and capture errors. Logs are stored in `restaurant_management.log`. Here’s how to use it:

-   Any critical errors or issues encountered during runtime will be recorded in this log file.
-   This file can be helpful for debugging and monitoring the application's performance.

## Contributing

Contributions are welcome! If you'd like to contribute to **Savory Dish Dash**, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes and push the branch.
4.  Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.