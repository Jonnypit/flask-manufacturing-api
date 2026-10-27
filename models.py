from database  import db

class Part(db.Model):
    __tablename__ = "parts"

    part_id     = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String)
    material    = db.Column(db.String)
    quantity    = db.Column(db.Integer)
    price       = db.Column(db.Float)

class Order(db.Model):
    __tablename__ = "orders"

    order_id        = db.Column(db.Integer, primary_key=True)
    part_id         = db.Column(db.Integer)
    quantity        = db.Column(db.Integer)
    status          = db.Column(db.String)
    date            = db.Column(db.String)

class Employee(db.Model):
    __tablename__ = "employees"

    employee_id     = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String)
    role            = db.Column(db.String)
    department      = db.Column(db.String)
    hire_date       = db.Column(db.String)
