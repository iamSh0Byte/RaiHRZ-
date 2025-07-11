from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'RAI HRZ Flask App Running'

if __name__ == '__main__':
    app.run(debug=True)