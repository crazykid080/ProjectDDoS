import Exceptions
from dbBase import *

class User(db.Model):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	password = db.Column(db.String)
	funds = db.Column(db.Integer)
	
	
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