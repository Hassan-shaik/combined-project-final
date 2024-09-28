from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lost_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            image TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('findit.html')  # Serve the original HTML form

@app.route('/report', methods=['POST'])
def report_lost_item():
    name = request.form['yourName']
    description = request.form['itemDescription']
    contact = request.form['contactInfo']
    image = request.files['itemImage']

    # Save the uploaded image
    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # Insert item into the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lost_items (name, description, image, contact)
            VALUES (?, ?, ?, ?)
        ''', (name, description, image.filename, contact))
        conn.commit()
        conn.close()

        return redirect(url_for('list_items'))

    return 'Error: Missing fields'

@app.route('/list', methods=['GET'])
def list_items():
    # Fetch lost items from the database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT name, description, image, contact FROM lost_items')
    items = cursor.fetchall()
    conn.close()

    return render_template('lost_items.html', items=items)

if __name__ == '__main__':
    app.run(port=5000)
