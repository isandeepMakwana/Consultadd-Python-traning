from crypt import methods
import json
from dataclasses import dataclass
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MakW@1239@localhost/testdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@dataclass
class Employee(db.Model):
    id:int
    name:str
    dept:str
    manager:str
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    dept = db.Column(db.String(20), nullable=False)
    manager = db.Column(db.String(20), nullable=False)
@dataclass
class Department(db.Model):
    dept:str
    emp:Employee
    dept = db.Column(db.String(20), db.ForeignKey(Employee.dept),primary_key=True)
    emp = db.relationship(Employee)

# add and Get    
@app.route("/employee",methods=["GET","POST"])
def Emp():
    if request.method=='POST':
        data = request.get_json()
        name = data.get('name')
        id = data.get('id')
        dept=data.get('dept')
        manager=data.get('manager')
        new_Emp = Employee(id=id, name=name, dept=dept, manager=manager)
        new_Dept = Department(dept=dept, emp=new_Emp)
        try:
            db.session.add(new_Emp)
            db.session.add(new_Dept)
            db.session.commit()
            return f"your data is {name , id , dept , manager} is added."
        except:
            return "Issue adding in your Employee!!!"
    elif request.method=='GET':
        employees = Employee.query.order_by(Employee.id).all()
        return jsonify(employees)

@app.route("/department")
def Dep():
    data= Department.query.all()
    return jsonify(data)

#update
@app.route("/updateEmp/<int:id>" , methods=["PUT"])
def updEmp(id):
    emp = Employee.query.get_or_404(id)
    data = request.get_json()
    name = data.get('name')
    dept=data.get('dept')
    manager=data.get('manager')
    emp.name=name
    emp.dept=dept
    emp.manager=manager
    try:
        db.session.commit()
        return f"employee data updated ."
    except:
        return f"error update is not possible for this id.{id}"


@app.route("/delete/<int:id>" , methods=["DELETE"])
def delEmp(id):
    emp = Employee.query.get_or_404(id)
    emp_left= len(Employee.query.filter(Employee.dept == emp.dept).all())
    if(emp_left==1):
        dep_del = Department.query.get_or_404(emp.dept)
    try:
        if emp_left>1:
            db.session.delete(emp)
            db.session.commit()
            return "employee deleted Successfully ."
        else:
            db.session.delete(emp)
            db.session.delete(dep_del)
            db.session.commit()
            return "data deleted Successfully ."

    except:
        return "can't deleted data !!!"

# @app.route("/login/<name>")
# def loginFunction(name):
#     return f'welcom {name}'
#
# @app.route("/success",methods=["GET","POST"])
# def data():
#     if request.method=='POST':
#         return request.data
#     else:
#         return  f"method is {request.method} "

@app.route("/")
def hello():
    return "welcome to flask application"
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=9090)
