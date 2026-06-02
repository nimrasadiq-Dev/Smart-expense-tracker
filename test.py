import pymysql

import matplotlib.pyplot as plt

print("--- SMART EXPENSE TRACKER WITH PIE CHART ---")

# 1. Database se connect hona
mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3307,
    database="smart_expense_db"
)
mycursor = mydb.cursor()

# 2. User se naye kharche enter karwana
while True:
    item = input("\nAap ne kis cheez par kharcha kiya? ")
    amount = int(input("Kitne paise kharch huay? "))
    
    sql = "INSERT INTO expenses (item_name, amount_spent) VALUES (%s, %s)"
    val = (item, amount)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    print(f"✓ '{item}' database mein save ho gaya!")
    
    aur_kharcha = input("Kya koi aur kharcha enter karna hai? (yes/no): ")
    if aur_kharcha.lower() == 'no':
        break

print("\n--- DATABASE SE DATA UTTHAYA JA RAHA HAI... ---")

# 3. SQL Query: Database se saara data wapas Python mein lekar aana
mycursor.execute("SELECT item_name, amount_spent FROM expenses")
rows = mycursor.fetchall()

# Data ko alag alag lists mein dalna taake graph ban sake
items = []
amounts = []
for row in rows:
    items.append(row[0])
    amounts.append(row[1])

# 4. DATA SCIENCE PART: Pie Chart (Graph) Generate karna
print("--- GRAPH GENERATING... ---")
plt.figure(figsize=(6, 6)) # Graph ka size set kiya
plt.pie(amounts, labels=items, autopct='%1.1f%%', startangle=140) # Gol chart banaya
plt.title("Aap ke Tamam Kharche (Expense Chart)")

# Graph ko screen par dikhana
plt.show()

print("\nProject successfully completed! 🎉")