# MatrixDeterminantCalculatorFlask

This is a simple Python Flask application to calculate the determinant of a 3x3 matrix. Pip-installable packages required are listed in `requirements.txt`.

This application is not perfect in that textboxes are not aligned to look like a 3x3 matrix; instead, it uses a## to denote the place; a13, for example, denotes the number at row 1 column 3.

The application will also print whether or not the matrix is invertible. It first calculates the determinant and then:

  if the determinant is 0:
    print not invertible
  else:
    print invertible
    
The application will play an error sound should a `ValueError` be raised, when an invalid character is put in the textboxes.
