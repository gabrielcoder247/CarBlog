from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User, Blog, Email
from app import create_app,db
import unittest

app = create_app('production')
# app = create_app('development')

# Initializing extensions
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)    

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User, Blog = Blog, Email = Email )

@manager.command
def test():
    # Run the unit test   
       
    


    tests= unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.secret_key='12345'
    manager.run()

