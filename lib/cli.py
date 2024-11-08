# lib/cli.py
from sqlalchemy.orm import Session
from lib.db.database import engine, get_db
from lib.db.models import Menu, Dish
from lib.db.seed import init_db
from lib.helpers import create_menu, list_menus, create_dish, list_dishes, exit_program

def display_menu():
    """Display the main menu options."""
    print("\nRestaurant Management System")
    print("=" * 25)
    print("1. Create a Menu")
    print("2. List All Menus")
    print("3. Create a Dish")
    print("4. List All Dishes")
    print("0. Exit")
    print("=" * 25)

def handle_choice(choice):
    """Handle the user's menu choice."""
    try:
        if choice == "1":
            create_menu()
        elif choice == "2":
            list_menus()
        elif choice == "3":
            create_dish()
        elif choice == "4":
            list_dishes()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please try again.")

def main():
    """Main function to run the CLI application."""
    # Initialize the database tables
    init_db()
    
    print("Welcome to the Restaurant Management System!")
    
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (0-4): ")
            handle_choice(choice)
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit_program()
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(0)
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        exit(1)