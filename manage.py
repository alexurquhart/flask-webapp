from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
import asyncore, os, smtpd

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
def runserver():
    app.run(host=app.config['HOST'], port=app.config['PORT'])
    
@manager.command
def runmail():
    smtpd.DebuggingServer(('127.0.0.1', 2048), None)
    asyncore.loop()

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()