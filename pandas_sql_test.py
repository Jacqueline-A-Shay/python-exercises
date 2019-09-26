import pandas as pd

from env import host, user, password

# url = f'mysql+pymysql://{user}:{password}@{host}/employees'
database_name = "albums_db"

#df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
query = """SELECT * FROM albums"""
df = pd.read_sql(query,url)
# print(df)

print(df)


# make a df from select * from employees
employees_query = "select * from employees"
database_name = "employees"

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
employees = pd.read_sql(employees_query, url)
employees.head()

# salary
salaries_query = "select * from salaries where to_date > now()"
database_name = "employees"

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
salaries = pd.read_sql(salaries_query, url)
salaries.head()

emp_sal = pd.merge(employees, salaries, left_on = "emp_no", right_on= "emp_no", how = "inner")
type(emp_sal)
emp_sal.head()