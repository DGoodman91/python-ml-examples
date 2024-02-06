#
# using sklearn to generate a linear regression model based on multiple independent variables
#

import os
import pandas
from sklearn import linear_model

dataframe = pandas.read_csv(os.path.join(os.path.dirname(
    __file__), '..', 'data', 'simple-multiple-regression.csv'))

# independent variables
X = dataframe[['Volume', 'Weight']]

# dependent variable
y = dataframe['CO2']

# similar to
model = linear_model.LinearRegression()
model.fit(X, y)

# check the model's coefficients with
print(model.coef_)

# we can now use the model to predict other values
print(model.predict([[1100, 800]]))
