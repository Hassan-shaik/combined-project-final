from flask import Flask, jsonify, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opt_out.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class OptOut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)


def init_db():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/opt-out', methods=['POST'])
def opt_out():
    opt_out_record = OptOut.query.first()
    if opt_out_record:
        opt_out_record.count += 1
    else:
        opt_out_record = OptOut(count=1)
        db.session.add(opt_out_record)

    db.session.commit()
    return f"You have opted out of the food service. Total opt-outs: {opt_out_record.count}"


# Route for the management count
@app.route('/opt-out-count', methods=['GET'])
def get_opt_out_count():
    opt_out_record = OptOut.query.first()
    count = opt_out_record.count if opt_out_record else 0
    return jsonify({"opt_out_count": count})


# Reset opt-out count
@app.route('/reset', methods=['POST'])
def reset():
    opt_out_record = OptOut.query.first()
    if opt_out_record:
        opt_out_record.count = 0
        db.session.commit()
    return jsonify({"status": "success", "message": "Opt-out count reset."})


if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
