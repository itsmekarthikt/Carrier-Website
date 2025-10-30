from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
   return "Hello, World!"

@app.route('/home')
def home():
   return "Hello, Worlds!"


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)