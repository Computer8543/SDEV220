import pandas as pd

# read top 10 rows
df = pd.read_csv('./telco_churn.csv')
print(df.head(10))

# print bottom 5 rows
print(df.tail(15))

# convert a dictionary to a dataframe
tempdict: dict = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf: pd.DataFrame = pd.DataFrame.from_dict(tempdict)
print(dictdf.head())

# print all column names
print(df.columns)

# print the data types
print(df.dtypes)

# print statistics minus objects
print(df.describe())

# print statistics with objects
print(df.describe(include='object'))

# print State column
print(df.State)

# print International plan column
print(df['International plan'])

# print two columns
print(df[['State', 'International plan']])

# print unique values in State column
print(df.State.unique())

# print unique values in Churn column
print(df.Churn.unique())

# print rows that match a column value
print(df[df['International plan']== 'No'])

# print rows that match two columns
print(df[(df['International plan']== 'No') & (df['Churn']== False)])

# print a specific row number
print(df.iloc[14])

# print a specific row and column
print(df.iloc[14,0])

# print a specific range of rows
print(df.iloc[22:33])

# make a dataframe copy and create an index
state: pd.DataFrame = df.copy()
state.set_index('State', inplace=True)
print(state.head())

# print rows on a specific indexed column value
print(state.loc['OH'])

# print the sum of rows where each column has a null 
print(df.isnull().sum())

# drop all the null values
df.dropna(inplace=True)
print(df.isnull().sum())

# drop/delete an entire column
df.drop('Area code', axis=1)

# create a calculated column 
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']

# Update all columns
df['New Column'] = 100 # all
print(df.head())

# Update a single column
df.iloc[0,-1] = 10 # row 0, last column
print(df.head())

# add a calculated field using a lambda 
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)
print(df[df['Churn']==True].head())

# df conversions

# output to csv
df.to_csv('output.csv')

# output to json
df.to_json()

# output to html
df.to_html()

# delete dataframe  
del df 
