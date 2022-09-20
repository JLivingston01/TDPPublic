import numpy as np

class LinearRegression:
    """
    Analytical Linear Regression

    LinearRegression fits a linear model with coefficients coef_ minimizing
    the residual sum of squares. Coefficients are calculated analytically with
    a pseudo-inversion of X^t@X in this implementation.

    No parameters are set in this implementation. If an intercept is desired,
    include an intercept in any x matrix used for fit and predict.
    """
    def __init__(self):
        return None

    def fit(self,x,y):
        self.coef_ = np.linalg.pinv(x.T@x)@(x.T@y)
        return self

    def predict(self,x):
        return x@self.coef_