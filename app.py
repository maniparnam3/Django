from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    gender = db.Column(db.String(500),nullable=False)
    dept = db.Column(db.String(100),nullable= False)
    year = db.Column(db.Integer,nullable= False)
    sem = db.Column(db.Integer,nullable= False)
    mail = db.Column(db.String(100),nullable= False)
    mobile = db.Column(db.String(10),nullable= False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id}-{self.name}"


@app.route('/',methods=['GET','POST'])
def stud():
    if request.method=='POST':
        name = request.form['name']
        gender = request.form['gender']
        dept = request.form['dept']
        year = request.form['year']
        sem = request.form['sem']
        mail = request.form['mail']
        mobile = request.form['mobile']
        stud = Student(name = name,gender= gender,dept = dept,year=year,sem=sem,mail=mail,mobile=mobile)
        db.session.add(stud)
        db.session.commit()
        
    allStudent = Student.query.all() 
    return render_template('index.html', allStudent=allStudent)

if __name__ == '__main__':
    app.run(debug=True)