#!/bin/python3

from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():

    portugalTimeZone = pytz.timezone('Europe/Lisbon')
    portugalTime = datetime.now(portugalTimeZone).strftime('%Y-%m-%d %H:%M:%S')

    return render_template('index.html', time=portugalTime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)