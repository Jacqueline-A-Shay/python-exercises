
# update json file
with open("replayScript.json", "r") as jsonFile:
    data = json.load(jsonFile)

tmp = data["location"]
data["location"] = "NewPath"

with open("replayScript.json", "w") as jsonFile:
    json.dump(data, jsonFile)

# create log
import json

x = [{
  "name": "John",
  "     "
}]

with open("file_name.json", "w") as jsonFile:
	json.dump(data_to_write_to_json,jsonFile)
with open("    .json", "r") as jsonFile:
	data = json.load(jsonFile)

# import json

# res = []
# seen = set()

# def add_entry(res, name, element, type):

#     # check if in seen set
#     if (name, element, type) in seen:
#         return res

#     # add to seen set
#     seen.add(tuple([name, element, type]))

#     # append to results list
#     res.append({'name': name, 'element': element, 'type': type})

#     return res

# args = ['xyz', '4444', 'test2']

# res = add_entry(res, *args)  # add entry - SUCCESS
# res = add_entry(res, *args)  # try to add again - FAIL

# args2 = ['wxy', '3241', 'test3']

# res = add_entry(res, *args2)  # add another - SUCCESS

import json

account_info = []
seen = set()

def add_entry(account_info, customer_id,transaction_id, amount, record_type, category, store, description): #type = debt or credit

    # check if in seen set
    if (transaction_id) in seen:
        return account_info

    # add to seen set
    seen.add(tuple([customer_id, transaction_id, amount, record_type, category, store, description]))
    # need to find a way to create new id

    # append to results list
    account_info.append(
    	{"customer_id": customer_id,
    	"transaction_id": transaction_id, 
    	"amount": amount, 
    	"record_type": record_type, 
    	"category": category,
    	"store": store,
    	"description": description})

    return account_info

args = ['SATX01','SATX01_0001', '5,000.00', 'credit', 'salary', 'Mailchimp', 'paycheck']
account_info = add_entry(account_info, *args)  # add entry - SUCCESS

args2 = ['SATX01','SATX01_0002', '75.30', 'debit','grocery','HEB', 'weekly shopping']
account_info = add_entry(account_info, *args2)  # add another - SUCCESS

# def write_to_json(data_to_write_to_json, file_name):
#     with open(file_name, 'a', encoding='utf-8') as file:
#         for item in data_to_write_to_json:
#             x = json.dumps(item, indent=4)
#             file.write(x + '\n')

# #export to JSON
# write_to_json(account_info, 'bank_data.json')

with open("SATX01.json", "w") as jsonFile:
	json.dump(account_info,jsonFile)

with open("bank_2.json", "r") as jsonFile:
	test_data = json.load(jsonFile)







def retrieve_customer_profile(customer_id):
	customer_id = customer_id + '.json'
	with open(customer_id, "r") as jsonFile:
		data = json.load(jsonFile)
		return data

print("Good Day!  Please provide your customer id for further assistance.")  
print("Note: your id should begin with SATX followed by numbers")
customer_id = input("ID#: ")

data = retrieve_customer_profile(customer_id)
def process_num(b):
	return float(b.replace(',',''))


credit = [process_num(b['amount']) for b in data if b['amount'] and b['record_type'] == 'credit']
total_credit = sum(credit)

debit = [process_num(b['amount']) for b in data if b['amount'] and b['record_type'] == 'debit']
total_debit = sum(debit)

current_balance = total_credit - total_debit












def write_to_json(lst, fn):
    with open(fn, 'a', encoding='utf-8') as file:
        for item in lst:
            x = json.dumps(item, indent=4)
            file.write(x + '\n')

#export to JSON
write_to_json(res, 'elements.json')

# active_users = [profile for profile in profiles if profile['isActive']]
# n_active_users = len(active_users)


# def handle_balance(s):
# 	return float(s[1:].replace(',', ''))


# user_with_the_lowest_balance
# user_with_the_lowest_balance = profiles[0]
# for user in profiles[1:]:
#     if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
#         user_with_the_lowest_balance = user

current_credit = [b for b in data if b['amount'] and b['record_type'] == 'credit']
current_credit
[{'customer_id': 'SATX01',

  'transaction_id': 'SATX01_0001',

  'amount': '5,000.00',
  
  'record_type': 'credit',
  
  'category': 'salary',
  
  'store': 'Mailchimp',
  
  'description': 'paycheck'},

 {'customer_id': 'SATX01',
  'transaction_id': 'SATX01_0002',
  'amount': '75.30',
  'record_type': 'debt',
  'category': 'grocery',
  'store': 'HEB',
  'description': 'weekly shopping'}]



















# Take user input
# account_info = []
# seen = set()
# use account_info to search for the file belonging to particular customer


# work on updating transaction_id
account_info = []
seen = set()

def add_entry(account_info, customer_id,transaction_id, amount, record_type, category, store, description): #type = debt or credit

    # check if in seen set
    if (transaction_id) in seen:
        return account_info

    # add to seen set
    seen.add(tuple([customer_id, transaction_id, amount, record_type, category, store, description]))
    # need to find a way to create new id

    # append to results list
    account_info.append(
    	{"customer_id": customer_id,
    	"transaction_id": transaction_id, 
    	"amount": amount, 
    	"record_type": record_type, 
    	"category": category,
    	"store": store,
    	"description": description})

    return account_info

args = ['SATX01','SATX01_0001', '5,000.00', 'credit', 'salary', 'Mailchimp', 'paycheck']
account_info = add_entry(account_info, *args)  # add entry - SUCCESS

args2 = ['SATX01','SATX01_0002', '75.30', 'debt','grocery','HEB', 'weekly shopping']
account_info = add_entry(account_info, *args2)  # add another - SUCCESS










# if transaction_id in seen
# transaction_id update

import datetime
transaction_id = datetime.datetime.now()

credit = [process_num(b['amount']) for b in data if b['amount'] and b['record_type'] == 'credit']

import datetime


def get_entry_details():
	customer_id = data[0]["customer_id"]
	transaction_id = str(datetime.datetime.now())
	amount = input("How much will you like to withdraw? ")
	record_type = 'debit'
	category = input("What's the category for this purchase?")
	if category == '':
		category = 'null'
	store = input("Which store did you shop with?")
	if store == '':
		store = 'null'
	description = input("Would you like to enter description for the transaction?")
	if description == '':
		description = 'null'
	return customer_id, transaction_id, amount, record_type, category, store, description

x = get_entry_details()


def add_entry(customer_id, transaction_id, amount, record_type, category = "no entry", store = "no entry", description = "no entry"): #type = debit or credit
	amount = float(amount)
    # append to results list
    data.append({"customer_id": x[0]})
    # 	"transaction_id": transaction_id, 
    # 	"amount": amount, 
    # 	"record_type": record_type, 
    # 	"category": category,
    # 	"store": store,
    # 	"description": description
    

    return data

ready_to_save = input("Ready to save editing? True/False")
def save_input(ready_to_save):
	if ready_to_save:
		return add_entry(customer_id, transaction_id, amount, record_type, category = "no entry", store = "no entry", description = "no entry")

save_input(ready_to_save)
















