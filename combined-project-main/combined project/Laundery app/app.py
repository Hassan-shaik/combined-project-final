from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    room = db.Column(db.String(10), nullable=False)
    tower = db.Column(db.String(10), nullable=False)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()  # Fetch all students to display
    return render_template('index.html', students=students)  # Serve the HTML page

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(
        name=data['name'],
        mobile=data['mobile'],
        room=data['room'],
        tower=data['tower']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"}), 201

@app.route('/reset_database', methods=['POST'])
def reset_database():
    db.session.query(Student).delete()  # Delete all entries
    db.session.commit()
    return jsonify({"message": "Database reset successfully!"}), 200

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        "name": student.name,
        "mobile": student.mobile,
        "room": student.room,
        "tower": student.tower
    } for student in students]), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
