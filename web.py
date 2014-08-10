from ads import get_gcn, get_refereed
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/publications/')
def publications():
    
    get_refereed()
    get_gcn()
    
    return render_template('publications.html')

@app.route('/software/')
def software():
    return render_template('software.html')

@app.route('/cv/')
def cv():
    return render_template('cv.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
  app.run()
