# lib/db/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.database import Base

class Menu(Base):
    __tablename__ = 'menus'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    items = relationship("MenuItem", back_populates="menu")

class MenuItem(Base):
    __tablename__ = 'menu_items'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menus.id'))

    menu = relationship("Menu", back_populates="items")
