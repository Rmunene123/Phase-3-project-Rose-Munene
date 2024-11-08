# lib/helpers.py
from sqlalchemy.orm import sessionmaker
from .db.models import Menu, Dish  
from .db.database import engine

Session = sessionmaker(bind=engine)

def create_menu():
    """Prompts user to create a new menu."""
    name = input("Enter menu name: ")
    menu = Menu(name=name)
    session = Session()
    try:
        session.add(menu)
        session.commit()
        print(f"Menu '{name}' created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating menu: {str(e)}")
    finally:
        session.close()

def list_menus():
    """Lists all menus in the database."""
    session = Session()
    try:
        menus = session.query(Menu).all()
        if not menus:
            print("No menus found.")
            return
        
        print("\nAvailable Menus:")
        print("=" * 20)
        for menu in menus:
            print(f"ID: {menu.id} - Name: {menu.name}")
        print("=" * 20)
    except Exception as e:
        print(f"Error listing menus: {str(e)}")
    finally:
        session.close()

def create_dish():
    """Prompts user to create a new dish."""
    try:
        name = input("Enter dish name: ")
        while True:
            try:
                price = float(input("Enter dish price: "))
                break
            except ValueError:
                print("Please enter a valid number for price.")
        
        # Show available menus
        list_menus()
        while True:
            try:
                menu_id = int(input("Enter menu ID to associate with: "))
                break
            except ValueError:
                print("Please enter a valid number for menu ID.")

        session = Session()
        # Verify menu exists
        menu = session.query(Menu).filter(Menu.id == menu_id).first()
        if not menu:
            print(f"Menu with ID {menu_id} not found.")
            return

        dish = Dish(name=name, price=price, menu_id=menu_id)
        session.add(dish)
        session.commit()
        print(f"Dish '{name}' created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating dish: {str(e)}")
    finally:
        session.close()

def list_dishes():
    """Lists all dishes in the database."""
    session = Session()
    try:
        dishes = session.query(Dish).all()
        if not dishes:
            print("No dishes found.")
            return
        
        print("\nAvailable Dishes:")
        print("=" * 40)
        for dish in dishes:
            menu_name = dish.menu.name if dish.menu else "No Menu"
            print(f"ID: {dish.id} - Name: {dish.name} - Price: ${dish.price:.2f} - Menu: {menu_name}")
        print("=" * 40)
    except Exception as e:
        print(f"Error listing dishes: {str(e)}")
    finally:
        session.close()

def exit_program():
    """Exits the application."""
    print("\nThank you for using the Restaurant Management System!")
    exit()