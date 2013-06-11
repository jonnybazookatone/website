import os
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/me')
def defsdaf():
    x = random.Random()
    context = {'val':x}
    return render_template('me.html',context)


if __name__ == "__main__":
  app.run()
