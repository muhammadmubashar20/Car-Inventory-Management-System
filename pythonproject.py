import mysql.connector
from tkinter import *
from tkinter import messagebox


db = mysql.connector.connect(host="192.168.100.85", user="root", password="Mk@6528015", db="PythonProject")
cur = db.cursor()


def submit():
    user = Username.get()
    passw = password.get()

    logintodb(user, passw)


def logintodb(user, passw):

    cur.execute("select * from login")
    record = cur.fetchall()

    for (user, passw) in record:
        if user == user and passw == passw:
            open()
            break
    

    else:
        messagebox.showerror("Error", "Incorrect username or password")
        Username.delete(0, END)
        password.delete(0, END)


def open():

    global top1
    top1 = Toplevel()
    top1.title("Menu")
    top1.geometry("300x300")

    add_product = Button(top1, text="Add Product", command=addProduct, width=15)
    add_product.place(x=100, y=50)

    show_inventory = Button(top1, text="Show Inventory", command=showInventory, width=15)
    show_inventory.place(x=100, y=80)

    search_product = Button(top1, text="Search Product", width=15, command=showInventory)
    search_product.place(x=100, y=110)

    show_orders = Button(top1, text="Show Reservations", command=showOrders, width=15)
    show_orders.place(x=100, y=140)

    reset_pass = Button(top1, text="Reset Password", width=15, command=resetPass)
    reset_pass.place(x=100, y=170)


def resetPass():
    top6 = Toplevel()
    top6.geometry("300x300")
    top6.title("Reset Password")

    newPasslbl = Label(top6, text="New Password")
    newPass = Entry(top6, width=15)
    newPasslbl.place(x=50, y=20)
    newPass.place(x=175, y=20)

    confirmPasslbl = Label(top6, text="Confirm Password")
    confirmPass = Entry(top6, width=15)
    confirmPasslbl.place(x=50, y=50)
    confirmPass.place(x=175, y=50)

    def Reset():
        try:
            if newPass.get() == confirmPass.get() and len(newPass.get()) >= 8:
                cur.execute("update login set password=%s where user=%s", (newPass.get(), Username.get()))
                db.commit()

                top6.destroy()
                top1.destroy()

            else:
                messagebox.showerror("", "Try Again")
                newPass.delete(0, END)
                confirmPass.delete(0, END)

        except:
            messagebox.showerror("", "Try Again")
            newPass.delete(0, END)
            confirmPass.delete(0, END)


    reset = Button(top6, text="Reset", command=Reset)
    reset.place(x=100, y=100)


def addProduct():

    top2 = Toplevel()
    top2.title("Add Product")
    top2.geometry("300x300")

    modellbl = Label(top2, text="Model*")
    model = Entry(top2)
    modellbl.place(x=70, y=20)
    model.place(x=130, y=20, width=115)

    namelbl = Label(top2, text="Name*")
    name = Entry(top2)
    namelbl.place(x=70, y=50)
    name.place(x=130, y=50, width=115)

    brandlbl = Label(top2, text="Brand*")
    brand = Entry(top2)
    brandlbl.place(x=70, y=80)
    brand.place(x=130, y=80, width=115)

    colourlbl = Label(top2, text="Colour")
    colour = Entry(top2)
    colourlbl.place(x=70, y=110)
    colour.place(x=130, y=110, width=115)

    conditionlbl = Label(top2, text="Condition")
    condition = Entry(top2)
    conditionlbl.place(x=70, y=140)
    condition.place(x=130, y=140, width=115)

    addbtn = Button(top2, text="Add", command=lambda: add(brand.get(), name.get(),
                                                          model.get(), condition.get(), colour.get()))
    addbtn.place(x=90, y=180, width=115)


    def add(getbrand, getname, getmodel, getcondition, getcolour):

        if getcondition == "" and getcolour == "":
            try:
                cur.execute("insert into inventory(brand, name, model) values(%s, %s, %s)",
                            (getbrand, getname, getmodel))
                print("data inserted")
                db.commit()
                brand.delete(0, END)
                name.delete(0, END)
                model.delete(0, END)
                condition.delete(0, END)
                colour.delete(0, END)
                messagebox.showinfo("Success", "Data Inserted Successfully")
            except:
                messagebox.showerror("Failed", "Incomplete Data")

        elif getcolour == "":
            try:
                cur.execute("insert into inventory(brand, name, model, Car_Condition) values(%s, %s, %s, %s)",
                            (getbrand, getname, getmodel, getcondition))
                print("data inserted")
                db.commit()
                brand.delete(0, END)
                name.delete(0, END)
                model.delete(0, END)
                condition.delete(0, END)
                colour.delete(0, END)
                messagebox.showinfo("Success", "Data Inserted Successfully")
            except:
                messagebox.showerror("Failed", "Incomplete Data")

        elif getcondition == "":
            try:
                cur.execute("insert into inventory(brand, name, model, Colour) values(%s, %s, %s, %s)",
                            (getbrand, getname, getmodel, getcolour))
                print("data inserted")
                db.commit()
                brand.delete(0, END)
                name.delete(0, END)
                model.delete(0, END)
                condition.delete(0, END)
                colour.delete(0, END)
                messagebox.showinfo("Success", "Data Inserted Successfully")
            except:
                messagebox.showerror("Failed", "Incomplete Data")

        else:
            try:
                cur.execute("""insert into inventory(brand, name, model, Colour, Car_Condition) 
                            values(%s, %s, %s, %s, %s)""", (getbrand, getname, getmodel, getcolour, getcondition))
                print("data inserted")
                db.commit()
                brand.delete(0, END)
                name.delete(0, END)
                model.delete(0, END)
                condition.delete(0, END)
                colour.delete(0, END)
                messagebox.showinfo("Success", "Data Inserted Successfully")
            except:
                messagebox.showerror("Failed", "Incomplete Data")




def showInventory():

    top3 = Toplevel()
    cur.execute("select * from inventory")
    inv = cur.fetchall()
    print(inv)

    frame1 = Frame(top3)
    frame1.pack()
    frame2 = Frame(top3, bd=5)
    frame2.pack()

    col1 = Label(frame2, text="No.")
    col1.grid(row=0, column=0)
    col2 = Label(frame2, text="Brand")
    col2.grid(row=0, column=1)
    col3 = Label(frame2, text="Name")
    col3.grid(row=0, column=2)
    col4 = Label(frame2, text="Model")
    col4.grid(row=0, column=3)
    col5 = Label(frame2, text="Colour")
    col5.grid(row=0, column=4)
    col6 = Label(frame2, text="Condition")
    col6.grid(row=0, column=5)

    i = 1
    for item in inv:
        for j in range(len(item)):
            e = Label(frame2, text=item[j], width=15, justify="center", relief=SUNKEN)
            e.grid(row=i, column=j)
        delbtn = Button(frame2, text="delete", fg="Red", width=5, relief=SOLID,
                        command=lambda n=item[1], d=item[2]: remove(n, d))
        delbtn.grid(row=i, column=j+1, padx=5, pady=2)
        i = i + 1

    def remove(brand, name):
        rmv = messagebox.askyesnocancel("Remove", "Are you sure you want to remove this row?")

        if rmv:
            try:
                cur.execute("delete from inventory where brand=%s and name=%s limit 1", (brand, name))
                cur.execute("alter table inventory drop no")
                cur.execute("alter table inventory add No int key auto_increment first")
                db.commit()

                top3.destroy()

                showInventory()
            except:
                messagebox.showerror("ERROR", "Something went wrong")



    global searchInventorybar

    searchInventorylbl = Label(frame1, text="Search")
    searchInventorylbl.grid(row=0, column=0)
    searchInventorybar = Entry(frame1, width=25)
    searchInventorybar.grid(row=0, column=1, columnspan=2, pady=8)

    searchInventorybtn = Button(frame1, text="Search", command=searchInventory)
    searchInventorybtn.grid(row=0, column=4, padx=10)


def searchInventory():

    query = "select * from inventory where Brand=%s or Name=%s or Model=%s or Car_Condition=%s or Colour=%s"
    top4 = Toplevel()
    cur.execute(query, (searchInventorybar.get(), searchInventorybar.get(),
                        searchInventorybar.get(), searchInventorybar.get(), searchInventorybar.get()))
    inv = cur.fetchall()
    print(inv)

    if searchInventorybar.get() == "":
        messagebox.showerror("", "Empty field")

    elif inv == []:
        messagebox.showerror("", "Not Available")

    else:
        col1 = Label(top4, text="No.")
        col1.grid(row=0, column=0)
        col2 = Label(top4, text="Brand")
        col2.grid(row=0, column=1)
        col3 = Label(top4, text="Name")
        col3.grid(row=0, column=2)
        col4 = Label(top4, text="Model")
        col4.grid(row=0, column=3)
        col5 = Label(top4, text="Colour")
        col5.grid(row=0, column=4)
        col6 = Label(top4, text="Condition")
        col6.grid(row=0, column=5)

        i = 1
        for item in inv:
            for j in range(len(item)):
                e = Label(top4, width=15, text=item[j], justify="center", relief=SUNKEN)
                e.grid(row=i, column=j)
            i = i+1



def showOrders():
    top5 = Toplevel()
    cur.execute("select * from orders")
    inv = cur.fetchall()
    print(inv)
    col1 = Label(top5, text="No.")
    col1.grid(row=0, column=0)
    col2 = Label(top5, text="Brand")
    col2.grid(row=0, column=1)
    col3 = Label(top5, text="Name")
    col3.grid(row=0, column=2)
    col4 = Label(top5, text="Model")
    col4.grid(row=0, column=3)
    col5 = Label(top5, text="Customer Name")
    col5.grid(row=0, column=4)

    i = 1
    for item in inv:
        for j in range(len(item)):
            e = Label(top5, width=15, text=item[j], justify="center", relief=SUNKEN)
            e.grid(row=i, column=j)
        shipbtn = Button(top5, text="Ship", justify="center", width=5, fg="red", relief=SOLID,
                         command=lambda d=item[1], n=item[2]: shipOrder(d, n))
        shipbtn.grid(row=i, column=j + 1, padx=5, pady=2)
        delbtn = Button(top5, text="delete", fg="Red", width=5, relief=SOLID,
                        command=lambda n=item[1], d=item[2]: remove(n, d))
        delbtn.grid(row=i, column=j + 2, padx=5, pady=2)
        i = i + 1

    def shipOrder(brand, name):

        ship = messagebox.askokcancel(title="Ship", message="Ship to Customer")

        if ship:
            try:
                a = brand
                cur.execute("""select brand, name, model from orders where
                            brand=%s and name=%s limit 1""", (a, name))
                b = cur.fetchone()
                print(b)

                cur.execute("""select brand, name, model from inventory where 
                            name=(select name from orders where brand=%s and name=%s limit 1)""", (a, name))
                c = cur.fetchone()
                print(c)

                if b == c:

                    cur.execute("delete from orders where brand=%s limit 1", (a,))
                    cur.execute("delete from inventory where brand=%s limit 1", (a,))

                    cur.execute("alter table orders drop no")
                    cur.execute("alter table orders add No int key auto_increment first")

                    cur.execute("alter table inventory drop no")
                    cur.execute("alter table inventory add No int key auto_increment first")

                    db.commit()

                    top5.destroy()

                    showOrders()

                else:
                    messagebox.showerror("ERROR", "Not Available")
            except:
                messagebox.showerror("ERROR", "Something went wrong")

    def remove(brand, name):
        rmv = messagebox.askyesnocancel("Remove", "Are you sure you want to remove this row?")

        if rmv:
            try:
                cur.execute("delete from orders where brand=%s and name=%s limit 1", (brand, name))
                cur.execute("alter table orders drop no")
                cur.execute("alter table orders add No int key auto_increment first")
                db.commit()

                top5.destroy()

                showOrders()
            except:
                messagebox.showerror("ERROR", "Something went wrong")



root = Tk()
root.geometry("300x300")
root.title("Inventory Management System")

Usernamelbl = Label(root, text="Username")
Username = Entry(root)
Usernamelbl.place(x=50, y=20)
Username.place(x=125, y=20, width=115)

passwordlbl = Label(root, text="Password")
e1_str = StringVar()
password = Entry(root, show="*", textvariable=e1_str)
passwordlbl.place(x=50, y=50)
password.place(x=125, y=50, width=115)

check = IntVar(value=0)


def my_show():
    if check.get() == 1:
        password.config(show='')
    else:
        password.config(show='*')


c1 = Checkbutton(root, text='Show Password', variable=check, onvalue=1, offvalue=0, command=my_show)
c1.place(x=125, y=70)

submitbtn = Button(root, text="Login", command=submit)
submitbtn.place(x=75, y=135, width=55)

exitbtn = Button(root, text="exit", command=exit)
exitbtn.place(x=150, y=135, width=55)


mainloop()