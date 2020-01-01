import init, User
from dbBase import *

db.create_all()

NUser = User.User("Crazykid080", "PasswordSHOULDBEAHASH")
db.session.add(NUser)
db.session.commit()