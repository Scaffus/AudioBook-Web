from flask import Flask, render_template, request, redirect
from flask.helpers import send_file
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import desc
from txt2audio import NewBook
import os


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

        book = NewBook(content=content, name=name)

        return redirect('/file&name={}'.format(name))


@app.route('/file&name=<string:name>')
def file(name):

    for file in os.listdir('audio-books/'):
        if os.path.basename(file) == '{}.mp3'.format(name):

            return render_template('done.html', file=file)


    return redirect('/')


@app.route('/download/<filename>')
def download_and_remove(filename):

    path = 'audio-books/{}'.format(filename)

    
    return send_file(path, as_attachment=True) and redirect('/delete/{}'.format(filename))
    

@app.route('/delete/<filename>')
def delete_file(filename):
    
    path = 'audio-books/{}'.format(filename)
    os.remove(path)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)