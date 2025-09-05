import tkinter as tk;
import pymysql
from tkinter import messagebox

class hotel():
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")

        scrn_width = self.root.winfo_screenwidth() # winfo_screenwidth is built-in method for width
        scrn_height = self.root.winfo_screenheight() # winfo_screeheight is built-in method for height

        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")

        mainTitle = tk.Label(self.root, text="Hotel Management System", bd=5, relief= "groove", bg="gray",fg="yellow",font=("Arial",40,"bold"))
                            #label place,text-------------------borderwidth,3d or flat border,background,foreground,font
        mainTitle.pack(side="top",fill="x")

        #-----------input frame----------------

        inputFrame = tk.Frame(self.root, bg="light green", bd=5 , relief="groove")
        inputFrame.place(x=20,y=90, width=500, height=670)

        nameLabel = tk.Label(inputFrame, text="Customer Name:", bg="light green", font=("Arial",15,"bold"))
        nameLabel.grid(row=0 , column=0, padx=20 , pady=30)
        self.nameIn = tk.Entry(inputFrame, bd=2, width=15, font=("Aria",15))
        self.nameIn.grid(row=0, column=1, padx=5, pady=30)

        idLabel = tk.Label(inputFrame, text="Customer ID:", bg="light green", font=("Arial",15,"bold"))
        idLabel.grid(row=1 , column=0, padx=20 , pady=30)
        self.idIn = tk.Entry(inputFrame, bd=2, width=15, font=("Aria",15))
        self.idIn.grid(row=1, column=1, padx=5, pady=30)

        stayLabel = tk.Label(inputFrame, text="Nigth Stay:", bg="light green", font=("Arial",15,"bold"))
        stayLabel.grid(row=2 , column=0, padx=20 , pady=30)
        self.stayIn = tk.Entry(inputFrame, bd=2, width=15, font=("Aria",15))
        self.stayIn.grid(row=2, column=1, padx=5, pady=30)

        okBtn = tk.Button(inputFrame,text="Ok",command=self.ok_fun, width=20, bg="sky blue", bd=3,font=("Arial",20,"bold"))
        okBtn.grid(row=3,column=0,columnspan=2,padx=40,pady=50)

        insertBtn = tk.Button(inputFrame,command=self.insert_db,text="Insert", width=20, bg="sky blue", bd=3,font=("Arial",20,"bold"))
        insertBtn.grid(row=4,column=0,columnspan=2,padx=40,pady=30)

        #--------------output frame----------

        outputFrame = tk.Frame(self.root, bg="light green", bd=5 , relief="groove")
        outputFrame.place(x=550,y=90, width=950, height=670)

        titleLabel = tk.Label(outputFrame,text="Five Star Hotel", bg="gray", fg="red", bd=5, width=28, font=("Arial",30,"bold"))
        titleLabel.grid(row=0,column=0, padx=20,pady=20)

        rateLabel=tk.Label(outputFrame,text="Rent for Night: 1000",bg="light green", bd=3,font=("Arial",20,"bold"))
        rateLabel.grid(row=1,column=0,padx=50,pady=30)

        self.list = tk.Listbox(outputFrame, width=82, height=18 ,bg="cyan", font=("Arial",15))
        self.list.grid(row=2, column=0,padx=13)


        

    def ok_fun(self):
        name = self.nameIn.get()
        id = self.idIn.get()
        stay = int(self.stayIn.get())

        con=pymysql.connect(host="localhost", user="your_username", passwd="your_password", database="hotel")
        cur =con.cursor()
        cur.execute("select avail_room, rent from info")
        data = cur.fetchone()

        if data[0] >0:
            bill =data[1] * stay
            printBill = f"Rent of Mr/Mrs.{name} with ID: {id} is: {bill}"
            self.list.insert(tk.END,printBill)

            update= data[0] -1
            cur.execute("update info set avail_room=%s",update)
            con.commit()
            con.close()
        else:
            tk.messagebox.showerror("Error","All Rooms Reserved!")

    def insert_db(self):
        con=pymysql.connect(host="localhost", user="your_username", passwd="your_password", database="hotel")
        cur =con.cursor()
        cur.execute("insert into info values(5,1000)")
        con.commit()
        con.close()


root = tk.Tk() #user interface window
obj = hotel(root) #object creation
root.mainloop() #mainloop is used to handle all events in window