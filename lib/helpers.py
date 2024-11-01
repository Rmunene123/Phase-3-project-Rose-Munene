# lib/helpers.py

from sqlalchemy.orm import sessionmaker
from .db.models.menu import Menu
from .db.models.dish import Dish
from .db.database import engine  # Your database setup module

def create_menu():
    """Prompts user to create a new menu."""
    name = input("Enter menu name: ")
    menu = Menu(name=name)
    session = sessionmaker(bind=engine)()
    session.add(menu)
    session.commit()
    session.close()
    print(f"Menu '{name}' created.")

def list_menus():
    """Lists all menus in the database."""
    session = sessionmaker(bind=engine)()
    menus = session.query(Menu).all()
    for menu in menus:
        print(menu)
    session.close()

def create_dish():
    """Prompts user to create a new dish."""
    name = input("Enter dish name: ")
    price = int(input("Enter dish price: "))
    menu_id = int(input("Enter menu ID to associate with: "))
    dish = Dish(name=name, price=price, menu_id=menu_id)
    session = sessionmaker(bind=engine)()
    session.add(dish)
    session.commit()
    session.close()
    print(f"Dish '{name}' created.")

def list_dishes():
    """Lists all dishes in the database."""
    session = sessionmaker(bind=engine)()
    dishes = session.query(Dish).all()
    for dish in dishes:
        print(dish)
    session.close()

def exit_program():
    """Exits the application."""
    print("Goodbye!")
    exit()
