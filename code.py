# =====================================
# STEP 1: IMPORT LIBRARIES
# =====================================

import pandas as pd
import sqlite3

# =====================================
# STEP 2: READ EXCEL DATASET
# =====================================

df = pd.read_excel("Employee_source_Dataset--lab06.xlsx")

print("Dataset:")
display(df)

# =====================================
# STEP 3: CREATE SQLITE DATABASE
# =====================================

conn = sqlite3.connect('employee.db')

# =====================================
# STEP 4: STORE DATA IN SQL TABLE
# =====================================

df.to_sql(
    'employees',
    conn,
    if_exists='replace',
    index=False
)

print("Table Created Successfully!")

# =====================================
# BUSINESS QUESTION 1
# Highest Salary
# =====================================

print("\nQ1. Which employee has the highest salary?\n")

query1 = """
SELECT Name, Salary
FROM employees
ORDER BY Salary DESC
LIMIT 1;
"""

display(pd.read_sql(query1, conn))

# =====================================
# BUSINESS QUESTION 2
# Lowest Salary
# =====================================

print("\nQ2. Which employee has the lowest salary?\n")

query2 = """
SELECT Name, Salary
FROM employees
ORDER BY Salary ASC
LIMIT 1;
"""

display(pd.read_sql(query2, conn))

# =====================================
# BUSINESS QUESTION 3
# Average Salary
# =====================================

print("\nQ3. What is the average salary of employees?\n")

query3 = """
SELECT AVG(Salary) AS Average_Salary
FROM employees;
"""

display(pd.read_sql(query3, conn))

# =====================================
# BUSINESS QUESTION 4
# Employee Count by Department
# =====================================

print("\nQ4. How many employees work in each department?\n")

query4 = """
SELECT Department,
COUNT(*) AS Employee_Count
FROM employees
GROUP BY Department;
"""

display(pd.read_sql(query4, conn))

# =====================================
# BUSINESS QUESTION 5
# Total Salary by Department
# =====================================

print("\nQ5. What is the total salary expenditure by department?\n")

query5 = """
SELECT Department,
SUM(Salary) AS Total_Salary
FROM employees
GROUP BY Department;
"""

display(pd.read_sql(query5, conn))

# =====================================
# BUSINESS QUESTION 6
# Employees earning above 100000
# =====================================

print("\nQ6. Which employees earn more than ₹100000?\n")

query6 = """
SELECT Name,
Department,
Salary
FROM employees
WHERE Salary > 100000;
"""

display(pd.read_sql(query6, conn))

# =====================================
# BUSINESS QUESTION 7
# Salary Ranking
# =====================================

print("\nQ7. Rank employees by salary.\n")

query7 = """
SELECT Name,
Department,
Salary
FROM employees
ORDER BY Salary DESC;
"""

display(pd.read_sql(query7, conn))

# =====================================
# CLOSE CONNECTION
# =====================================

conn.close()
