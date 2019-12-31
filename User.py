import sqlalchemy as db
import Exceptions
from dbBase import *
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)
	
	def checkPassword(self, attempt):
		if(self.password != attempt):
			return False
		else:
			return True
	
	def __init__(self, name=None, password=None):
		if(name == None or password == None):
			raise Exceptions.IllegalArgumentError
		self.name = name
		self.password = password