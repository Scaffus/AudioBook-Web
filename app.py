from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
# db = SQLAlchemy(app)

@app.route('/')
def home():

    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug = True)