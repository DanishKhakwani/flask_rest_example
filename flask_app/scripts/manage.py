from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_app.app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('migrate', MigrateCommand)

if __name__ == "__main__":
    manager.run()
