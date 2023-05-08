from flask import Flask, render_template
from disk_analyzer import disk_test
import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/disk-status.html')
def disk_analyzer():
    disk_test()
    with open('veriler.json', 'r') as f:
        veriler = json.load(f)
    return render_template('disk-status.html', veriler=veriler)


if __name__ == '__main__':
    app.run(debug=True)
