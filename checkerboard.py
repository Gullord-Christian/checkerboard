from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/play')
def home():
    return render_template('index.html')  

@app.route('/play/<int:num>')
def xamount(num):
    return render_template("index2.html", num=num)

if __name__ == "__main__":
    app.run(debug = True)