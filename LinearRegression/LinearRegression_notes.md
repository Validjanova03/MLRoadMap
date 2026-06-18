Linear Regression - One of the simplest ML Algorithm
* Goal: Predict a continuous value using a straight line
* Examples:
  - Hourse Price
  - Salary
  - Rent
  - Temperature
* Core Formula:  y = wx + b
  y = predict
  x = input feature
  w = slope(How much y changes when x increases by 1) 
  b = intercept (Starting value when x = 0)

  How to remember w and b ?
  Think of taxi:
  Price = 2 * Distance + 5
  w = 2, Means: Every extra kilometer adds 2$
  b = 5, Means: Starting fee is 5$ 
RULE:
w = Growth rate
b = Starting value 

Goal of Linear Regression:
Find the best values of w and b so predictions are as accurate as possible

Prediction:
Suppose: y = 7x + 3
x = 10 ,  y = 7(10) + 3 = 73
Prediction = 73

What is Error?
Error tells us how wrong the prediction.
Error = Actual - Predicted
Example: Actual = 70, Predicted = 65,   Error = 5  

Why we need Cost Function?
We need one number that tells us 'How bad is the model?'
This number is called the Cost Function.
For Linear Regression:
Mean Square Error (MSE)
MSE = 1/n Sum from i=1 until n (yi - y'i)^2
Steps:
1. Calculate Error
2. Square Error
3. Average Error
Example:
Errors: 5 -2 -2
Squared: 25 4 4
Average 33/3 = 11 , MSE = 11


Training - find w and b that minimizes MSE (Find the line that makes the smallest mistakes).

Gradient Descent = Steps:
1. Start with random w and b
2. Calculate Error
3. Adjust b and w
4. Repeat
Untill Error becomes very small
R^2 used for measure quality


