from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/publications/')
def publications():
    return render_template('publications.html')

@app.route('/software/')
def software():
    return render_template('software.html')

if __name__ == "__main__":
  app.run()
