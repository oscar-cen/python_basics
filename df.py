
import pandas as pd
my_df=pd.read_excel('bankloan.xls')
# print(type(my_df))             # dataframe
# print(my_df.head(5))      # show first 5 rows + header = 6 rows   index:0~4
print(list(my_df.columns))
# print(my_df.head(5).transpose())  
print(my_df.shape)       # row and column numbers
print(my_df[0:5])         # first five rows, without header
print(my_df[-5:])            # last five rows
print(my_df['Income'][0:5])   # first five rows only filtered(shown) the 'Income' column
print(my_df[['Income','Edu']][0:5]) 
print(my_df.iloc[4:9,1:4])         # 4~8 rows, with 1~3 columns
print(my_df.Edu.value_counts())     # one column's summary
print(my_df.Edu.value_counts(normalize=True)*100)    # percentage
print(pd.crosstab(my_df['Edu'],my_df['Income']))     # biaozhong is the number of items satisfied for certain condition
print(my_df.sort_values('Income')[0:10])          # sort according to Income value
print(my_df.sort_values('Income',ascending=False)[0:10])  
my_df['New']=my_df['Edu']-my_df['Income']     # Create a new column
print(my_df[0:5])

 # print(my_df.groupby('Age')[['Age','Income']].mean())    # group by the column name
print(my_df.groupby('Age')['Income'].mean().reset_index()) 
print(my_df.groupby(['Age','Edu'])['Income'].mean().reset_index()) 
my_df.rename(columns={'Edu':'Education','Income':'Wage'},inplace=True)    # rename column
print(my_df[0:5])

import matplotlib.pyplot as plt 
import seaborn as sn

## sn.barplot(x = 'AGE', y = 'SOLD PRICE', data = soldprice_by_age)


## Univariant LR
import numpy as np
np.set_printoptions(precision=4, linewidth=100)
mba_salary_df = pd.read_excel('salary.xls') 
print(mba_salary_df.head(10))

## for i in range(25,50):
	##mba_salary_df['No.'][i]=i+1
	##mba_salary_df['Percentage'][i]= mba_salary_df['Percentage.1'][i-25]
	##mba_salary_df['Salary'][i]= mba_salary_df['Salary.1'][i-25]
  
   
import statsmodels.api as sm
X = sm.add_constant(mba_salary_df['Percentage'] )
print(X)

Y=mba_salary_df['Salary']
print(Y)

from sklearn.model_selection import train_test_split
train_X, test_X, train_Y, test_Y=train_test_split(X,Y,train_size=0.8,random_state=100)  ##80% is training data; note the 4 order
mba_salary_lm = sm.OLS(train_Y, train_X).fit()
print(mba_salary_lm.params)     ## fitting value
print(mba_salary_lm.summary2())   

## mba_salary_resid = mba_salary_lm.resid 
##probplot = sm.ProbPlot(mba_salary_resid) 
##plt.figure( figsize = (8, 6)) 
##probplot.ppplot( line='45' )
##plt.title('Fig 4.1 - Normal P-P Plot of Regression Standardized Residuals')
## plt.show()

pred_y = mba_salary_lm.predict( test_X )
print(pred_y)


## multi-linear-regression    ##read txt file, separated by comma
## 1. direct command, splitting data into training and test set
data2_df=pd.read_csv('multi.txt',header=None,names=['Size','Bedrooms','Price']) 
print(data2_df)
X=sm.add_constant(data2_df[['Size','Bedrooms']])
print(X)
Y=data2_df['Price']
print(Y)
train_X,test_X,train_Y,test_Y=train_test_split(X,Y,train_size=0.8,random_state=100)
data2_lm = sm.OLS(train_Y, train_X).fit()
print(data2_lm.params) 
print(data2_lm.summary2())

## 2. batch gradient descent
data2_df = (data2_df-data2_df.mean())/data2_df.std()    # normalization
data2_df.insert(0,'Ones',1)
print(data2_df)
cols = data2_df.shape[1]
X2 = data2_df.iloc[:,0:cols-1]
y2 = data2_df.iloc[:,cols-1:cols]
X2 = np.matrix(X2.values)       # convert to matrices
y2 = np.matrix(y2.values)
theta2 = np.matrix(np.array([0,0,0]))   # initilaize theta
alpha=0.1
iters=100


def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner)/(2*len(X))      # len(X)=row number of X

def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))    # theta initialization
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)       # cost initialization
    
    for i in range(iters):
        error = (X*theta.T) - y        # error is 1*m
        
        for j in range(parameters):
            term = np.multiply(error, X[:,j])    # term is 1*m   # multiply: every row does multiplication
            temp[0,j] = theta[0,j] - ((alpha/len(X))*np.sum(term))
            
        theta = temp
        cost[i] = computeCost(X, y, theta)       # cost is an array
    return theta, cost

g2, cost2 = gradientDescent(X2, y2, theta2, alpha, iters)
print(g2)
computeCost(X2, y2, g2)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(np.arange(iters), cost2, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()


## 3. normal equ
def normalEqn(X, y):
	one=np.linalg.inv(np.dot(X.T,X))
	two=np.dot(one,X.T)
	theta=np.dot(two,y)
	return theta
final_theta2=normalEqn(X2, y2)
print(final_theta2)


'''
## logistic regression (classification)
logistic_df=pd.read_csv('logistic.txt',header=None,names=['A','B','Credit'])
X=sm.add_constant(logistic_df[['A','B']])
Y=logistic_df['Credit']
train_X,test_X,train_Y,test_Y=train_test_split(X,Y,train_size=0.8,random_state=100)
logistic_lm=sm.Logit(train_Y,train_X).fit()
print(logistic_lm.params) 
print(logistic_lm.summary2())
print(logistic_lm.predict(test_X))
'''











