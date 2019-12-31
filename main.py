import User, Servers, WebPage
from dbBase import *

NUser = User.User("Crazykid080", "PasswordSHOULDBEAHASH")
engine.add(NUser)
engine.commit()