from flask import Flask
from dotenv import load_dotenv
from database import db
from routes import parts, orders, employees
import os

load_dotenv()

app =Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)

app.register_blueprint(parts.bp)
app.register_blueprint(orders.bp)
app.register_blueprint(employees.bp)




with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    

