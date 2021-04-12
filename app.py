# This code is very basic and not optimized at all, just a draft
from flask import Flask, render_template, request, redirect, send_file
from txt2audio import NewBook
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
# db = SQLAlchemy(app)

@app.route('/')
def home():

    return render_template('index.html')

# Get the text content and the name, convert it to audio using my function NewBook and then opens a new pages with a link to download the file
@app.route('/post', methods=['GET', 'POST'])
def post():

    if request.method == 'POST':

        content = request.form['content']
        name    = request.form['name']
        voice   = request.form['voice']

        # Checking if the user actually submitted something
        if name == ' ' or content == ' ' or name == '' or content == '':
            
            return redirect('/')

        else:

            # [NOT THE MOST EFFICIENT I KNOW LOL] Every time someone creates a new book it deletes all the existing ones (avoid a 10tb folder x) )
            for file in os.listdir('audio-books/'):
                os.remove('audio-books/{}'.format(file))

            NewBook(content=content, name=name, voice=voice)

            # Send the user to the page where he can download the file
            return redirect('/file&name={}&voice={}&text={}'.format(name, voice, content))

# Page where the user can download his file
@app.route('/file&name=<string:name>&voice=<string:voice>&text=<string:text>')
def file(name, voice, text):

    for file in os.listdir('audio-books/'):
        if os.path.basename(file) == '{}.mp3'.format(name):

            return render_template('done.html', file=file, text=text, voice=voice)


    return redirect('/')

# This function send the desired file to the user
@app.route('/download/<filename>')
def download(filename):

    path = 'audio-books/{}'.format(filename)
    
    return send_file(path, as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug = True)