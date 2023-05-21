import winsound, numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/determinant', methods = ['POST'])
def determinant():
  try:
      a11 = float(request.form['a11'])
      a12 = float(request.form['a12'])
      a13 = float(request.form['a13'])
      a21 = float(request.form['a21'])
      a22 = float(request.form['a22'])
      a23 = float(request.form['a23'])
      a31 = float(request.form['a31'])
      a32 = float(request.form['a32'])
      a33 = float(request.form['a33'])
      matrix = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
      determinant = round(np.linalg.det(matrix), 1)
      is_invertible = determinant != 0
      return render_template('index.html', determinant=determinant, invertible=is_invertible)
   except ValueError:
      winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
      return render_template('index.html', error='Invalid input')
    
if __name__ == "__main__":
  app.run(debug = True)
