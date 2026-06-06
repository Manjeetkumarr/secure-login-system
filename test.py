from app import app, db

with app.app_context():
    db.engine.connect()

print("MariaDB Connected Successfully")