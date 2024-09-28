from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def management():
    try:
        response = requests.get('http://localhost:5000/opt-out-count')  # Fetch opt-out count from main app
        data = response.json()
        count = data.get("opt_out_count", 0)
    except Exception as e:
        count = 0  # If there's an error, default count to 0
        print(f"Error fetching data: {e}")

    return render_template('management.html', opt_out_count=count)


@app.route('/reset', methods=['POST'])
def reset():
    try:
        response = requests.post('http://localhost:5000/reset')  # Send reset request to main app
        if response.ok:
            return redirect(url_for('management'))
    except Exception as e:
        print(f"Error resetting data: {e}")

    return redirect(url_for('management'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Management app runs on port 5001
