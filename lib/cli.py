# lib/cli.py

from sqlalchemy.orm import Session
from .db.database import engine, get_db
from .db.models import Menu
from db.models.dish import Dish
from helpers import create_menu, list_menus, create_dish, list_dishes, exit_program

def main():
    """Main function to run the CLI."""
    print("Welcome to the Restaurant Management CLI!")
    
    while True:
        print("\nPlease select an option:")
        print("1. Create a Menu")
        print("2. List Menus")
        print("3. Create a Dish")
        print("4. List Dishes")
        print("0. Exit the program")
        
        choice = input("> ")
        
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

if __name__ == "__main__":
    main()
