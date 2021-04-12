from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import desc
import txt2audio


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
# db = SQLAlchemy(app)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():

    if request.method == 'POST':

        content = request.form['content']
        name    = request.form['name']

        book = txt2audio.NewBook(content=content, name=name)

        return redirect('/file&name=<str:name>')


@app.route('/file&name=<str>')
def file():

    return render_template('done.html')

if __name__ == '__main__':
    app.run(debug = True)