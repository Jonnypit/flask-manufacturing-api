from flask import Flask
from database import db
from routes import parts, orders, employees

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manufacturing.db"

db.init_app(app)

app.register_blueprint(parts.bp)
app.register_blueprint(orders.bp)
app.register_blueprint(employees.bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    

