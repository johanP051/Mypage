from json.tool import main
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/abril")
def abril():
    return render_template("abril.html")


@app.route('/agosto')
def agosto():
    return render_template('agosto.html')

@app.route('/diciembre')
def diciembre():
    return render_template('diciembre.html')



#debug mode
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)