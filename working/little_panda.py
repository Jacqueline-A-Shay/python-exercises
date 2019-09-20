import json
import datetime
import pandas as pd

# Input and read in customer info based on customer_id
def retrieve_customer_profile(customer_id):
	customer_id = customer_id + '.json'
	with open(customer_id, "r") as jsonFile:
		data = json.load(jsonFile)
	return data

print("Good Day!  Please provide your customer id for further assistance.")
print("  ")  
print("Note: your id should begin with SATX followed by numbers")
print("  ")  
print("The default ID# is SATX01, if you need to establish an account with us, please contact your local representative.  Thank you!")
print("  ")  
customer_id = input("ID#: ")

data = retrieve_customer_profile(customer_id)

print("~~~ Welcome to your terminal checkbook! ~~~")

print("How may I help you today?")

print("You have the following options:")
print("1) view current balance")
print("2) record a debit (withdraw)")
print("3) record a credit (deposit)")
print("4) view your account summary")
print("5) exit")

df = pd.DataFrame(data) 
print(df)
type(df.index)
df.set_index('transaction_id',inplace=True)
df.head()

%matplotlib inline 

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') 

df.columns = list(map(str, df.columns))

# let's check the column labels types now
all(isinstance(column, str) for column in df.columns)
