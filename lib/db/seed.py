# lib/db/seed.py

from sqlalchemy.orm import sessionmaker
from .models.menu import Menu
from .models.dish import Dish
from ..database import engine

def seed_data():
    """Seeds the database with initial data."""
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create sample menus and dishes
    menu1 = Menu(name="Breakfast Menu")
    dish1 = Dish(name="Pancakes", price=5, menu=menu1)
    dish2 = Dish(name="Omelette", price=7, menu=menu1)

    session.add(menu1)
    session.add(dish1)
    session.add(dish2)

    menu2 = Menu(name="Lunch Menu")
    dish3 = Dish(name="Burger", price=10, menu=menu2)
    session.add(menu2)
    session.add(dish3)

    session.commit()
    session.close()
    print("Database seeded!")

if __name__ == "__main__":
    seed_data()
