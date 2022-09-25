from distutils.log import debug
from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_me')
def who_i_am():
    return render_template('aboutme.html')

@app.route('/my_projects')
def my_projects():
    return render_template('myprojects.html')

@app.route('/what_im_searching')
def what_im_searching():
    return render_template('whatimsearching.html')



if __name__ == '__main__':
    app.run(debug = True, port = 3030) 