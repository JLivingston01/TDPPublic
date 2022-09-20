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
        self.coef_ = None

    def fit(self,x,y):
        """
        Fit a linear regression.

        Parameters
        ----------
        x : np.array or pd.DataFrame
            Matix or regression inputs.
        y : pd.Series, np.array or pd.DataFrame
            Regression target.

        Returns
        -------
        Self

        """
        self.coef_ = np.linalg.pinv(x.T@x)@(x.T@y)
        return self

    def predict(self,x):
        """
        Predict with fitted model

        Parameters
        ----------
        x : np.array or pd.DataFrame
            Matix or regression inputs.

        Returns
        -------
        np.array

        """
        return x@self.coef_
