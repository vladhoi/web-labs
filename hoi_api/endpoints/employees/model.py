from app import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    father_name = db.Column(db.String(20))
    address = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(20))
    salary = db.Column(db.String(20))

    def __repr__(self):
        return '<Employee: {} {}>'.format(self.first_name, self.last_name)
