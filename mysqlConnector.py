import mysql.connector as c
# First Step ---> Install mysql connector package
con = c.connect(host="localhost", user="root", passwd="123456", database="adityadb")

# for checking connection to the databases:
# if con.is_connected():
#     print("success")
# else:
#     print("error")
# ------------------------------------------>>

cursor = con.cursor()  # It provides control over the databases.

# ------------------->>For inserting Data into databases----------->>
while True:
    sid = int(input("enter here your code "))
    name = input("enter your name ")
    salary = int(input("enter postal code "))

    query = "INSERT INTO Student values({},'{}',{})".format(sid, name, salary)
    cursor.execute(query)
    con.commit()  # for permanently save the data.
    print("data added")
    x = int(input("1->Enter more\n 2. Exit\nEnter choice: "))
    if x == 2:
        break

# ----------------------->>>>End-------------------------------------->>>