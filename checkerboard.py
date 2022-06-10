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

#     ### Create a new Flask project

# Have the root route render a template with a checkerboard on it

# Have the css in a separate stylesheet and link this to the template

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
# ###