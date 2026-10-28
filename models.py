from database  import db

class Part(db.Model):
    __tablename__ = "parts"

    part_id     = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String)
    material    = db.Column(db.String)
    quantity    = db.Column(db.Integer)
    price       = db.Column(db.Float)

    def to_dict(self):
        return {
            "part_id": self.part_id,
            "name": self.name,
            "material": self.material,
            "quantity": self.quantity,
            "price":    self.price
        }

class Order(db.Model):
    __tablename__ = "orders"

    order_id        = db.Column(db.Integer, primary_key=True)
    part_id         = db.Column(db.Integer)
    quantity        = db.Column(db.Integer)
    status          = db.Column(db.String)
    date            = db.Column(db.String)

    def to_dict(self):
            return {
                "order_id": self.order_id,
                "part_id": self.part_id,
                "quantity": self.quantity,
                "status": self.status,
                "date": self.date,
            }

class Employee(db.Model):
    __tablename__ = "employees"

    employee_id     = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String)
    role            = db.Column(db.String)
    department      = db.Column(db.String)
    hire_date       = db.Column(db.String)

    def to_dict(self):
            return {
                "employee_id": self.employee_id,
                "name": self.name,
                "role": self.role,
                "department": self.department,
                "hire_date": self.hire_date
            }
