from sqlalchemy.orm import sessionmaker
from lib.db.database import engine, Base
from lib.db.models import Menu, Dish

def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")

def seed_data():
    """Seeds the database with initial data."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # First, initialize the database
        init_db()

        # Clear existing data (optional)
        session.query(Dish).delete()
        session.query(Menu).delete()
        session.commit()

        # Create sample menus and dishes
        breakfast_menu = Menu(name="Breakfast Menu")
        lunch_menu = Menu(name="Lunch Menu")
        dinner_menu = Menu(name="Dinner Menu")

        # Add menus first
        session.add_all([breakfast_menu, lunch_menu, dinner_menu])
        session.commit()

        # Create dishes with price as integers (in cents) or decimals
        dishes = [
            Dish(name="Pancakes", price=599, menu=breakfast_menu),
            Dish(name="Omelette", price=799, menu=breakfast_menu),
            Dish(name="French Toast", price=699, menu=breakfast_menu),
            
            Dish(name="Burger", price=999, menu=lunch_menu),
            Dish(name="Caesar Salad", price=899, menu=lunch_menu),
            Dish(name="Club Sandwich", price=899, menu=lunch_menu),
            
            Dish(name="Steak", price=2499, menu=dinner_menu),
            Dish(name="Grilled Salmon", price=2199, menu=dinner_menu),
            Dish(name="Pasta Primavera", price=1699, menu=dinner_menu)
        ]

        # Add all dishes
        session.add_all(dishes)
        session.commit()
        print("Database seeded successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {str(e)}")
        raise e
    finally:
        session.close()

if __name__ == "__main__":
    print("Starting database seeding...")
    seed_data()
    print("Finished seeding database!")