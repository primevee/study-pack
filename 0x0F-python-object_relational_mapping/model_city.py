#!/usr/bin/python3
""" cities in state """
import sys
from model_state import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class City(Base):
    """ City class """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
