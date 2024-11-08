# lib/db/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Menu(Base):
    __tablename__ = 'menus'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dishes = relationship("Dish", back_populates="menu")

    def __repr__(self):
        return f"Menu(id={self.id}, name='{self.name}')"

class Dish(Base):  # Changed from MenuItem to match your helpers.py
    __tablename__ = 'dishes'  # Changed from menu_items to match the class name
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    menu = relationship("Menu", back_populates="dishes")  # Changed items to dishes

    def __repr__(self):
        return f"Dish(id={self.id}, name='{self.name}', price={self.price})"