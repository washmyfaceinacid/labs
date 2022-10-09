from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/api/v1/hello-world-2')
def index():
    return "Hello world! 4"

if __name__=="__main__":
    app.run(debug=True)