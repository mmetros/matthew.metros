from myproject import app
from flask import Flask, render_template

@app.route('/')
def index():
    heading = "How Are We Today?"
    return render_template('home.html', heading=heading)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
