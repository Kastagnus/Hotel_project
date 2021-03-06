from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from app.commands.populate import Populate



manager = Manager(create_app())
manager.add_command("db", MigrateCommand)
manager.add_command("populate", Populate)