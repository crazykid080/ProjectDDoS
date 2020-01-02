import User
from dbBase import db
from init import app
import WebPage

db.create_all()

NUser = User.User("Crazykid080", "PasswordSHOULDBEAHASH")
db.session.add(NUser)
db.session.commit()

app.run(port=8000, debug=True)