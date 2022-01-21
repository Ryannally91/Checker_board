from flask import Flask, render_template, url_for


app = Flask(__name__)
#secret key to protect against cross-site forgery attacks, cookie modification

@app.route("/")
def checkboard_default():
    return render_template('layout.html', x = 8, y = 8, color1 ='red', color2 = 'black')

@app.route("/<int:x>")
def checkboard_x(x):
    return render_template('layout.html', x = x, y = 8, color1 ='red', color2 = 'black')

@app.route("/<int:x>/<int:y>")
def checkboard_x_y(x, y):
    return render_template('layout.html', x = x, y = y, color1 ='red', color2 = 'black')

@app.route("/<int:x>/<int:y>/<string:color1>")
def checkboard_x_y_c1(x, y, color1):
    return render_template('layout.html', x = x, y = y, color1 = color1, color2 = 'black')

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def checkboard_x_y_c1c2(x, y, color1, color2):
    return render_template('layout.html', x = x, y = y, color1 = color1, color2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 
