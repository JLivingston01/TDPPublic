"""Defining Linear Model Classes"""
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

    def fit(self, X, Y):
        """
        Fit a linear regression.

        Parameters
        ----------
        X : np.array or pd.DataFrame
            Matix or regression inputs.
        Y : pd.Series, np.array or pd.DataFrame
            Regression target.

        Returns
        -------
        Self

        """
        self.coef_ = np.linalg.pinv(X.T@X)@(X.T@Y)
        return self

    def predict(self, X):
        """
        Predict with fitted model

        Parameters
        ----------
        X : np.array or pd.DataFrame
            Matix or regression inputs.

        Returns
        -------
        np.array

        """
        return X@self.coef_
