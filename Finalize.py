from tkinter import *
import re
import mysql.connector
import tkinter.messagebox as tsmg
from PIL import ImageTk, Image
from tkinter import filedialog
from io import BytesIO
from functools import partial
global Ans1, E12
global filename

regex ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#mydb = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb1 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb2 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb3 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb4 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb6 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb11 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
mydb12 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
#mydb13 = mysql.connector.connect(host = 'localhost',user = 'root',password = 'NoSignal@0612',database = 'rohitdatabase')
mydb14 = mysql.connector.connect(host = 'localhost',user = 'root',password = 'NoSignal@0612',database = 'rohitdatabase')

#mycursor = mydb.cursor()
mycursor1 = mydb1.cursor()
mycursor2 = mydb2.cursor()
mycursor3 = mydb3.cursor()
mycursor4 = mydb4.cursor()
mycursor6 = mydb6.cursor()
mycursor11 = mydb11.cursor()
mycursor12 = mydb12.cursor()
#mycursor13 = mydb13.cursor()
mycursor14 = mydb14.cursor()

my_db7 = mysql.connector.connect(host="localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")
c7 = my_db7.cursor()

root20 = Tk()
root20.title("LOGIN")
root20.configure(bg="pink")
root20.geometry('2000x750')

img1 = Image.open("Capture8.PNG")
img1 = img1.resize((350,300),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
label3 = Label(root20,image=img1)
label3.place(x=0,y=0)

img2 = Image.open("Capture8.PNG")
img2 = img2.resize((350,300),Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
label4 = Label(root20,image=img2)
label4.place(x=1000,y=450)

def logout():
    quit()

def validate():

    my_db8 = mysql.connector.connect(host="localhost", user="root", password="NoSignal@0612", database="rohitdatabase")
    c8 = my_db8.cursor()

    c8.execute("select * from DETAILS where Cid = %s and password = %s",(uname.get(),password.get()))
    row = c8.fetchone()
    if row == None :
        tsmg.showerror("ERROR","INVALID USERNAME AND PASSWORD")
    else :
        global tup
        tup = uname.get()
        mydb = mysql.connector.connect(host="localhost", user="root", password="NoSignal@0612",
                                       database="rohitdatabase")
        mycursor = mydb.cursor()
        stat = """SELECT * from DETAILS where Cid not in (SELECT Cidr from Requests where Cida = %s) and gender = (SELECT genderpre from DETAILS where Cid = %s)"""
        mycursor.execute(stat,(tup,tup))

        def matches1():
            c4.delete(text0)
            c4.delete(text1)
            c4.delete(text2)
            c4.delete(text5)
            c4.delete(text6)
            c4.delete(text7)
            c4.delete(text8)

            text3.config(image='')
            matches()

        def matches2():

            stat3 = """SELECT * from DETAILS where CID in
                (Select cidr from Requests where cida = %s AND rel = TRUE
                UNION
                Select cida from Requests where cidr = %s AND rel = TRUE)"""

            mycursor6.execute(stat3, (tup, tup))
            matches()

        def matches():

            try:

                global text0, text1, text2, text3, text5, text6, text7, text8, record
                record = mycursor6.fetchone()
                text0 = c4.create_text(220, 460, text=record[1], fill="white", font="TimesNewRoman 12 bold")
                text1 = c4.create_text(220, 490, text=record[2], fill="white", font="TimesNewRoman 12 bold")
                text2 = c4.create_text(220, 520, text=record[6], fill="white", font="TimesNewRoman 12 bold")
                text5 = c4.create_text(220, 550, text=record[7], fill="white", font="TimesNewRoman 12 bold")
                text6 = c4.create_text(220, 580, text=record[9], fill="white", font="TimesNewRoman 12 bold")
                text7 = c4.create_text(580, 520, text=record[10], fill="white", font="TimesNewRoman 12 bold")
                text8 = c4.create_text(580, 490, text=record[11], fill="white", font="TimesNewRoman 12 bold")

                logo = record[3]

                img = Image.open(BytesIO(logo))
                img = img.resize((400, 300), Image.ANTIALIAS)
                phimg = ImageTk.PhotoImage(img)
                text3 = Label(c4, image=phimg)
                text3.phimg = phimg
                text3.place(x=220, y=50)
                #mycursor6.close()

            except Exception as e:

                tsmg.showinfo("Congratulations", "You have found this number of matches")
                print(e)
                root4.destroy()
                home_my_profile()

        def profile_your_matches():

            global root4, c4
            root4 = Tk()
            root4.geometry("800x700")
            root4.title("Your Matches")

            photo4 = Image.open("Back2.jpg")
            photo4 = photo4.resize((800, 700), Image.ANTIALIAS)
            photo4 = ImageTk.PhotoImage(photo4)

            c4 = Canvas(root4, width=800, height=700)
            c4.place(x=0, y=0)
            c4.create_image(0, 0, image=photo4, anchor="nw")

            c4.create_text(100, 430, text="PROFILE DETAILS    :", fill="yellow", font="TimesNewRoman 12 bold")
            c4.create_text(80, 460, text="Name        :", fill="white", font="TimesNewRoman 12 bold")
            c4.create_text(85, 490, text="Age         :", fill="white", font="TimesNewRoman 12 bold")
            c4.create_text(75, 520, text="Hobbies     :", fill="white", font="TimesNewRoman 12 bold")
            c4.create_text(70, 550, text="Profession   :", fill="white", font="TimesNewRoman 12 bold")
            c4.create_text(75, 580, text="Location    :", fill="white", font="TimesNewRoman 12 bold")

            l2 = Label(c4, text="Contact Details", bg="black", fg="yellow", relief=SUNKEN, borderwidth=5,
                       font="TimesNewRoman 13 bold", padx=20, pady=10)
            l2.place(x=400, y=420)

            c4.create_text(400, 490, text="Contact Number  :", fill="white", font="TimesNewRoman 12 bold")
            c4.create_text(415, 520, text="Email id           :", fill="white", font="TimesNewRoman 12 bold")

            b10 = Button(c4, text="Next", bg="red", fg="white", command=matches1, relief=SUNKEN, borderwidth=2,
                         font="TimesNewRoman 10 bold", padx=30, pady=5)
            b10.place(x=550, y=620)

            def Him():
                root4.destroy()
                home_my_profile()

            b12 = Button(c4, text="Back", bg="red", fg="white",command = Him, relief=SUNKEN, borderwidth=2,
                         font="TimesNewRoman 10 bold", padx=30, pady=5)
            b12.place(x=50, y=20)

            b11 = Button(c4, text="Logout", bg="red", fg="white", command=logout, relief=SUNKEN, borderwidth=2,
                         font="TimesNewRoman 10 bold", padx=30, pady=5)
            b11.place(x=650, y=20)

            matches2()
            root4.mainloop()

        def accept_request():

            tsmg.showinfo("Congratulations", "You have accepted successfully")
            temp = textd0
            tup1 = (1,tup,temp)
            sql = "Update Requests set rel = %s where cida = %s AND cidr = %s"
            mycursor3.execute(sql, tup1)
            mydb3.commit()
            your_request1()

        def decline_request():

            temp = textd0
            tup2 = (temp, tup)
            sql = "Delete from Requests where cidr = %s AND cida = %s"
            mycursor4.execute(sql, tup2)
            mydb4.commit()
            your_request1()

        def your_request1():

            c3.delete(textd1)
            c3.delete(textd2)
            c3.delete(textd6)
            c3.delete(textd7)
            c3.delete(textd9)
            c3.delete(textr3)

            textd3.config(image='')
            your_request()

        def your_request():

            try:

                global textd0,textd1, textd2, textd3, textd6, textd7, textd9, textr3
                record = mycursor1.fetchone()
                var = mycursor2.fetchone()

                textd0 = record[0]
                textd1 = c3.create_text(250, 160, text=record[1], fill="white", font="TimesNewRoman 12 bold")
                textd2 = c3.create_text(250, 190, text=record[2], fill="white", font="TimesNewRoman 12 bold")
                textd6 = c3.create_text(250, 220, text=record[6], fill="white", font="TimesNewRoman 12 bold")
                textd7 = c3.create_text(250, 250, text=record[7], fill="white", font="TimesNewRoman 12 bold")
                textd9 = c3.create_text(250, 280, text=record[9], fill="white", font="TimesNewRoman 12 bold")

                textr3 = c3.create_text(350, 430, text=var[3], fill="white", font="TimesNewRoman 12 bold")

                logo = record[3]

                img = Image.open(BytesIO(logo))
                img = img.resize((300, 250), Image.ANTIALIAS)
                phimg = ImageTk.PhotoImage(img)
                textd3 = Label(c3, image=phimg)
                textd3.phimg = phimg
                textd3.place(x=450, y=100)

            except:

                tsmg.showinfo("Congratulations", "You have reached end of Request Database")
                root3.destroy()

        def edprof():
            def edit_submit(tempstr):

                mydb13 = mysql.connector.connect(host='localhost', user='root', password='NoSignal@0612',
                                                 database='rohitdatabase')
                mycursor13 = mydb13.cursor()

                def convertToBinaryForm(filename):
                    with open(filename, 'rb') as file:
                        Binary_Data = file.read()

                        return Binary_Data

                photo = convertToBinaryForm(Ed24.get())

                tuped = (photo, ed2.get(), ed3.get(), ed1.get(), ed4.get(), tup)
                stated = """UPDATE DETAILS SET Image = %s,Profession = %s,Location = %s,Email_id = %s,Number = %s where Cid = %s"""
                mycursor13.execute(stated, tuped)
                mycursor13.close()
                mydb13.commit()
                mydb13.close()
                rooted.destroy()
                home_my_profile()

            def edit_openfilename():
                filename = filedialog.askopenfilename(title="UPLOAD PHOTO")
                Ed24.insert(0, filename)
                return filename

            def edit():
                x = edit_openfilename()
                i = Image.open(x)
                i = i.resize((325, 250), Image.ANTIALIAS)
                i = ImageTk.PhotoImage(i)
                l = Label(rooted, image=i)
                l.image = i
                l.place(x=425, y=125)

            rooted = Tk()
            rooted.geometry("800x700")
            rooted.title("Edit Profile")

            photo = Image.open("Req.jpg")
            photo = photo.resize((800, 700), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)

            ced = Canvas(rooted, width=800, height=700)
            ced.place(x=0, y=0)
            ced.create_image(0, 0, image=photo, anchor="nw")

            ced.create_text(120, 200, text="   Email-ID        :", fill="white", font="TimesNewRoman 14 bold")
            ced.create_text(120, 250, text="Profession      :", fill="white", font="TimesNewRoman 14 bold")
            ced.create_text(120, 300, text="  Location        :", fill="white", font="TimesNewRoman 14 bold")
            ced.create_text(120, 350, text="Contact No     :", fill="white", font="TimesNewRoman 14 bold")
            ced.create_text(120, 150, text="EDIT PROFILE DETAILS   :", fill="yellow", font="TimesNewRoman 13 bold")

            email = StringVar()
            ed1 = Entry(rooted, borderwidth=3, width=25, textvariable=email)
            ed1.place(x=215, y=190)

            prof = StringVar()
            ed2 = Entry(rooted, borderwidth=3, width=25, textvariable=prof)
            ed2.place(x=215, y=240)

            loc = StringVar()
            ed3 = Entry(rooted, borderwidth=3, width=25, textvariable=loc)
            ed3.place(x=215, y=290)

            cont = StringVar()
            ed4 = Entry(rooted, borderwidth=3, width=25, textvariable=cont)
            ed4.place(x=215, y=340)

            image = StringVar()
            Ed24 = Entry(rooted, borderwidth=5, width=50, textvariable=image)
            Ed24.place(x=435, y=450)

            tempstr = Ed24.get()
            bedit = Button(rooted, text="ADD IMAGE", bg="blue", fg="yellow", font=("bold", 13), command=edit)
            bedit.place(x=540, y=400)

            bedit1 = Button(rooted, text="SUBMIT", bg="green", fg="white", font=("bold", 13), command=partial(edit_submit,tempstr))
            bedit1.place(x=375, y=550)

            rooted.mainloop()

        def home_my_profile():

            mydb5 = mysql.connector.connect(host="localhost", user="root", password="NoSignal@0612",
                                            database="rohitdatabase")
            mycursor5 = mydb5.cursor()
            stat1 = """SELECT * from DETAILS where Cid = %s"""
            print(tup)
            mycursor5.execute(stat1,(tup,))
            root2 = Tk()
            root2.geometry("800x700")
            root2.title("My Profile")

            photo2 = Image.open("Back0.jpg")
            photo2 = photo2.resize((800, 700), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(photo2)

            c2 = Canvas(root2, width=800, height=700)

            c2.place(x=0, y=0)
            c2.create_image(0, 0, image=photo2, anchor="nw")
            c2.create_text(120, 230, text="Age                :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(108, 260, text="Profession         :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(115, 290, text="Hobby             :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(100, 320, text="Contact Number  :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(92, 350, text="Gender Preference :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(110, 380, text="Location          :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(113, 410, text="Email id          :", fill="white", font="TimesNewRoman 12 bold")
            c2.create_text(115, 470, text="Question asked by you   :", fill="white", font="TimesNewRoman 12 bold")

            try:
                record = mycursor5.fetchone()

                text5 = c2.create_text(100, 30, text="Hi, " + record[1], fill="white", font="TimesNewRoman 12 bold")
                text0 = c2.create_text(300, 230, text=record[2], fill="white", font="TimesNewRoman 12 bold")

                text1 = c2.create_text(300, 260, text=record[7], fill="white", font="TimesNewRoman 12 bold")

                text2 = c2.create_text(300, 290, text=record[6], fill="white", font="TimesNewRoman 12 bold")
                text4 = c2.create_text(300, 320, text=record[11], fill="white", font="TimesNewRoman 12 bold")
                text6 = c2.create_text(300, 350, text=record[12], fill="white", font="TimesNewRoman 12 bold")
                text7 = c2.create_text(300, 380, text=record[9], fill="white", font="TimesNewRoman 12 bold")
                text8 = c2.create_text(300, 410, text=record[10], fill="white", font="TimesNewRoman 12 bold")
                text9 = c2.create_text(200, 500, text=record[4], fill="white", font="TimesNewRoman 12 bold")

                logo = record[3]
                img = Image.open(BytesIO(logo))
                img = img.resize((300, 225), Image.ANTIALIAS)
                phimg = ImageTk.PhotoImage(img)
                text3 = Label(c2, image=phimg)
                text3.phimg = phimg
                text3.place(x=450, y=200)

                def profile_your_request2():
                    root2.destroy()
                    profile_your_request()

                b4 = Button(c2, text="Your Request", bg="blue", fg="white", relief=SUNKEN, borderwidth=3,
                            font="TimesNewRoman 10 bold", command=profile_your_request2, padx=50, pady=10)
                b4.place(x=100, y=80)

                mycursor5.close()

                def profile_your_matches1():
                    root2.destroy()
                    profile_your_matches()

                b5 = Button(c2, text="Your Matches", bg="blue", fg="white", relief=SUNKEN, borderwidth=3,
                            font="TimesNewRoman 10 bold", command=profile_your_matches1, padx=50, pady=10)
                b5.place(x=500, y=80)

                b6 = Button(c2, text="Logout", bg="yellow", fg="black", relief=SUNKEN, borderwidth=2,
                            font="TimesNewRoman 10 bold", command=logout, padx=40, pady=5)
                b6.place(x=650, y=20)

                def edprof1():
                    root2.destroy()
                    edprof()

                b7 = Button(c2, text="    Edit Profile    ", bg="blue", fg="white", relief=SUNKEN, borderwidth=2,
                            font="TimesNewRoman 10 bold", padx=30, pady=10, command=edprof1)
                b7.place(x=310, y=600)

                def Push():
                    root2.destroy()
                    validate()

                b8 = Button(c2, text="   BACK   ", bg="blue", fg="white", relief=SUNKEN, borderwidth=2,
                            font="TimesNewRoman 10 bold", padx=30, pady=10, command=Push)
                b8.place(x=110, y=600)


            except Exception as e:

                print("Error Occured", e)

            root2.mainloop()

        def profile_your_request():

            stat2 = """Select * from DETAILS where CID in
                    (Select cidr from Requests where cida = %s AND rel = 0)"""
            mycursor1.execute(stat2,(tup,))
            stat3 = """Select * from Requests where cida = %s"""
            mycursor2.execute(stat3,(tup,))
            profile_your_request1()

        def profile_your_request1():

            global c3, root3
            root3 = Tk()
            root3.geometry("800x600")
            root3.title("Your Request's")

            photo3 = Image.open("Back4.jpg")
            photo3 = photo3.resize((800, 600), Image.ANTIALIAS)
            photo3 = ImageTk.PhotoImage(photo3)

            c3 = Canvas(root3, width=800, height=600)
            c3.place(x=0, y=0)
            c3.create_image(0, 0, image=photo3, anchor="nw")

            c3.create_text(105, 90, text="PROFILE DETAILS  :", fill="yellow", font="TimesNewRoman 13 bold")
            c3.create_text(105, 160, text="Name          :", fill="white", font="TimesNewRoman 12 bold")
            c3.create_text(110, 190, text="Age           :", fill="white", font="TimesNewRoman 12 bold")
            c3.create_text(100, 220, text="Hobbies       :", fill="white", font="TimesNewRoman 12 bold")
            c3.create_text(100, 250, text="Profession  :", fill="white", font="TimesNewRoman 12 bold")
            c3.create_text(100, 280, text="Location      :", fill="white", font="TimesNewRoman 12 bold")
            c3.create_text(140, 380, text="Answer to your Question:", fill="white", font="TimesNewRoman 12 bold")

            b8 = Button(c3, text="Accept Request", bg="red", fg="white", relief=SUNKEN, borderwidth=2,
                        font="TimesNewRoman 10 bold", padx=30, pady=5, command=accept_request)
            b8.place(x=200, y=500)

            b9 = Button(c3, text="Decline Request", bg="red", fg="white", relief=SUNKEN, borderwidth=2,
                        font="TimesNewRoman 10 bold", padx=30, pady=5, command=decline_request)
            b9.place(x=400, y=500)

            b10 = Button(c3, text="Logout", bg="red", fg="white", relief=SUNKEN, borderwidth=3,
                        font="TimesNewRoman 10 bold", padx=30, pady=5, command=logout)
            b10.place(x=650, y=30)

            def Pushkar():
                root3.destroy()
                home_my_profile()

            b11 = Button(c3, text="Back", bg="red", fg="white", relief=SUNKEN, borderwidth=3,
                        font="TimesNewRoman 10 bold", padx=30, pady=5, command=Pushkar)
            b11.place(x=50, y=30)

            your_request()

            root3.mainloop()

        def request_a_date(string1):

            def click(string):

                answer_text = answer.get(1.0, END + "-1c")
                stat = """INSERT into Requests(Cidr,Cida,rel,answer) values(%s,%s,%s,%s)"""
                tup6 = (tup,string,0,answer_text)
                mycursor12.execute(stat, tup6)
                mycursor12.close()
                mydb12.commit()
                mydb12.close()
                root50.destroy()
                home_next1()

            root50 = Toplevel()
            root50.geometry("800x700")
            root50.title("Request's")

            # Here is the photo for background image
            photo = Image.open("Req.jpg")
            photo = photo.resize((800, 700), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)

            # specifications for canvas
            c1 = Canvas(root50, width=800, height=700)
            c1.place(x=0, y=0)
            c1.create_image(0, 0, image=photo, anchor="nw")

            # sample query executed.Change it to whatever you want
            stat3 = "SELECT * FROM DETAILS where Cid = %s"
            mycursor11.execute(stat3,(string1,))
            record = mycursor11.fetchone()

            # for title named Question in the program
            c1.create_text(400, 100, text="Question", fill="blue", font="TimesNewRoman 20 bold")

            # A rectangle for the outline
            c1.create_rectangle(650, 5, 150, 150, outline="white", width="2")

            # This gives the question stored in the database at the required index of the record.Again a sample, change it
            c1.create_text(400, 200, text=record[4], fill="white", font="TimesNewRoman 20 italic")

            # creates a text box for the user to enter.It is named as answer
            answer = Text(root50, width=80, height=12, fg="white", bg="black", font="TimesNewRoman 10 bold")
            answer.pack(padx=150)
            answer.place(x=120, y=300)

            # Finally this is a button named submit
            submit = Button(root50, text='Submit', width=10, bg="blue", fg="white",
                               command=partial(click, string1))
            submit.pack()
            submit.place(x=360, y=530)

            root50.mainloop()

        def home_next1():

            c1.delete(text1)
            c1.delete(text2)
            c1.delete(text5)
            c1.delete(text6)
            c1.delete(text7)
            c1.delete(text9)
            b2.pack_forget()
            text3.config(image='')
            home_next()

        def home_next():

            try:
                global text1, text2, text3, text5, text6, text7, text9, record, b2
                record = mycursor.fetchone()

                text1 = c1.create_text(480, 430, text=record[1], fill="white", font="TimesNewRoman 12 bold")

                text2 = c1.create_text(480, 460, text=record[2], fill="white", font="TimesNewRoman 12 bold")

                text6 = c1.create_text(480, 490, text=record[6], fill="white", font="TimesNewRoman 12 bold")

                text7 = c1.create_text(480, 520, text=record[7], fill="white", font="TimesNewRoman 12 bold")

                text9 = c1.create_text(480, 550, text=record[9], fill="white", font="TimesNewRoman 12 bold")

                logo = record[3]

                img = Image.open(BytesIO(logo))
                img = img.resize((400, 300), Image.ANTIALIAS)
                phimg = ImageTk.PhotoImage(img)

                text3 = Label(c1, image=phimg)

                text3.phimg = phimg
                text3.place(x=200, y=80)

                b3 = Button(c1, text="Request a Date", bg="red", fg="white", relief=SUNKEN, borderwidth=3,
                            font="TimesNewRoman 10 bold", padx=30, pady=5,command = partial(request_a_date,record[0]))
                b3.place(x=200, y=620)

                stat2 = """SELECT Persontest from DETAILS where Cid = %s"""
                mycursor14.execute(stat2, (tup,))
                for i in mycursor14:
                    Ans1 = i[0]

                Ans2 = record[5]
                c = 0

                for i in range(len(Ans1)):
                    if (Ans1[i] == Ans2[i]):
                        c = c + 1

                text5 = c1.create_text(480, 580, text=c, fill="yellow", font="TimesNewRoman 12 bold")

            except:

                tsmg.showinfo("Congratulations", "You have reached end of database")
                root.destroy()

        root = Tk()
        root.geometry("800x700")
        root.title("Home")

        photo = Image.open("2.jpg")
        photo = photo.resize((800, 700), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(photo)

        c1 = Canvas(root, width=800, height=700)
        c1.place(x=0, y=0)
        c1.create_image(0, 0, image=photo, anchor="nw")

        c1.create_text(308, 430, text="Name           :", fill="white", font="TimesNewRoman 12 bold")

        c1.create_text(310, 460, text="Age             :", fill="white", font="TimesNewRoman 12 bold")

        c1.create_text(305, 490, text="Hobby          :", fill="white", font="TimesNewRoman 12 bold")

        c1.create_text(300, 520, text="Profession     :", fill="white", font="TimesNewRoman 12 bold")

        c1.create_text(300, 550, text="Location        :", fill="white", font="TimesNewRoman 12 bold")

        c1.create_text(300, 580, text="Number of Answers Matched     :", fill="yellow", font="TimesNewRoman 12 bold")

        home_next()
        b1 = Button(root, text="Next", bg="red", fg="white", relief=SUNKEN, borderwidth=2, font="TimesNewRoman 10 bold",
                    command=home_next1, padx=30, pady=5)
        b1.place(x=500, y=620)

        def home_my_profile1():
            #mycursor.close()
            root.destroy()
            home_my_profile()

        b2 = Button(root, text="My Profile", bg="red", fg="white", relief=SUNKEN, borderwidth=2,
                    font="TimesNewRoman 10 bold", padx=15, command=home_my_profile1)
        b2.place(x=680, y=50)

        b3 = Button(c1, text="Logout", bg="red", fg="white", relief=SUNKEN, borderwidth=2,
                    font="TimesNewRoman 10 bold", padx=15, command=logout)
        b3.place(x=20, y=50)

        root.mainloop()

    c8.close()
    my_db8.commit()
    my_db8.close()

def register():

    def con():

        def p():
            def convertToBinaryForm(filename):
                with open(filename, 'rb') as file:
                    Binary_Data = file.read()

                    return Binary_Data

            photo = E12.get()

            una = uname.get()
            na = name.get()
            ag = age.get()
            photo = convertToBinaryForm(photo)
            de = des.get()
            qu = a.get() + b.get() + m.get() + d.get() + e.get()
            ho = hobbies.get()
            pr = profession.get()
            cl4 = clicked4.get()
            lo = location.get()
            ma = mail.get()
            co = contact.get()
            cl5 = clicked5.get()
            pas = password.get()

            sql_statement = "Insert into DETAILS(Cid,Name,Age,Image,Question,Persontest,hobby,Profession,Gender,Location,Email_id,Number,genderpre,Password) " \
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            put_tuple = (una, na, ag, photo, de, qu, ho, pr, cl4, lo, ma, co, cl5, pas)
            c7.execute(sql_statement, put_tuple)
            c7.close()
            my_db7.commit()
            my_db7.close()
            logout()

        top1 = Toplevel()
        top1.title("REGISTRATION")
        top1.geometry("1800x1100")
        top1.config(bg='magenta')

        l1 = Label(top1, text="WHAT WOULD YOU PREFER....", bg='magenta', font=('bold', 30))
        l1.place(x=0, y=40)

        l2 = Label(top1, text="1)", bg="magenta", fg="black", font=('bold', 15))
        l2.place(x=0, y=150)

        a = StringVar()
        a.set(" ")
        b1 = Radiobutton(top1, text="DOG", variable=a, value="1", bg="magenta", fg="black", font=('bold', 15))
        b2 = Radiobutton(top1, text="CAT", variable=a, value="2", bg="magenta", fg="black", font=('bold', 15))

        b1.place(x=100, y=150)
        b2.place(x=300, y=150)

        l2 = Label(top1, text="2)", bg="magenta", fg="black", font=('bold', 15))
        l2.place(x=0, y=300)

        b = StringVar()
        b.set(" ")
        b1 = Radiobutton(top1, text="MOUNTAIN", variable=b, value="1", bg="magenta", fg="black", font=('bold', 15))
        b2 = Radiobutton(top1, text="BEACH", variable=b, value="2", bg="magenta", fg="black", font=('bold', 15))

        b1.place(x=100, y=300)
        b2.place(x=300, y=300)

        l2 = Label(top1, text="3)", bg="magenta", fg="black", font=('bold', 15))
        l2.place(x=0, y=450)

        m = StringVar()
        m.set(" ")
        b1 = Radiobutton(top1, text="RED WINE", variable=m, value="1", bg="magenta", fg="black", font=('bold', 15))
        b2 = Radiobutton(top1, text="WHITE WINE", variable=m, value="2", bg="magenta", fg="black", font=('bold', 15))

        b1.place(x=100, y=450)
        b2.place(x=300, y=450)

        l2 = Label(top1, text="4)", bg="magenta", fg="black", font=('bold', 15))
        l2.place(x=800, y=150)

        d = StringVar()
        d.set(" ")
        b1 = Radiobutton(top1, text="SINGINIG", variable=d, value="1", bg="magenta", fg="black", font=('bold', 15))
        b2 = Radiobutton(top1, text="DANCING", variable=d, value="2", bg="magenta", fg="black", font=('bold', 15))

        b1.place(x=900, y=150)
        b2.place(x=1100, y=150)

        l2 = Label(top1, text="5)", bg="magenta", fg="black", font=('bold', 15))
        l2.place(x=800, y=300)

        e = StringVar()
        e.set(" ")
        b1 = Radiobutton(top1, text="USA", variable=e, value="1", bg="magenta", fg="black", font=('bold', 15))
        b2 = Radiobutton(top1, text="LONDON", variable=e, value="2", bg="magenta", fg="black", font=('bold', 15))

        b1.place(x=900, y=300)
        b2.place(x=1100, y=300)

        #b_back = Button(top1, text="BACK", bg="blue", font=("bold", 13))
        b_next = Button(top1, text="SUBMIT",borderwidth = 5, bg="yellow",padx = 40, font=("bold", 13), command=p)

        #b_back.place(x=500, y=640)
        b_next.place(x=600, y=600)

        top1.mainloop()

    root = Tk()
    root.config(bg="magenta")
    root.title("REGISTRATION")
    img_register = Image.open("Capture6.PNG")
    resized = img_register.resize((1700, 1500), Image.ANTIALIAS)
    img_register = ImageTk.PhotoImage(resized)

    label9 = Label(root, image=img_register)
    label9.pack()

    def openfilename():
        filename = filedialog.askopenfilename(title="UPLOAD PHOTO")
        E12.insert(0, filename)
        return filename

    def link():

        x = openfilename()
        i = Image.open(x)
        i = i.resize((400, 300), Image.ANTIALIAS)
        i = ImageTk.PhotoImage(i)
        l = Label(root, image=i)
        l.image = i
        l.place(x=920, y=60)

    b = Button(root, text="ADD IMAGE", bg="blue", fg="yellow", font=("bold", 20), command=link)
    b.place(x=1040, y=400)

    image = StringVar()
    E12 = Entry(root, borderwidth=5, width=50, textvariable=image)
    E12.place(x=975, y=480)

    title = Label(root, text="REGISTRATION FORM", fg="white", bg="blue", font=("bold", 15))
    title.place(x=600, y=30)

    label1 = Label(root, text="NAME      ", bg="magenta", fg="black", font=("bold", 12))
    label1.place(x=550, y=80)

    def on_entry_click(event):
        if e1.get() == ' Fname  Mname  Lname':
            e1.delete(0, "end")
            e1.insert(0, '')
            e1.config(fg='black')

    name = StringVar()
    e1 = Entry(root, borderwidth=5, width=25, textvariable=name)
    e1.place(x=690, y=80)
    e1.insert(0, " Fname  Mname  Lname")
    e1.bind('<FocusIn>', on_entry_click)
    e1.config(fg='grey', font=("bold", 10))

    label2 = Label(root, text="EMAIL-ID  ", bg="magenta", fg="black", font=("bold", 12))
    label2.place(x=550, y=140)

    mail = StringVar()
    e2 = Entry(root, borderwidth=5, width=25, textvariable=mail)
    e2.place(x=690, y=140)

    label3 = Label(root, text="LOCATION   ", bg="magenta", fg="black", font=("bold", 12))
    label3.place(x=550, y=200)

    location = StringVar()
    e3 = Entry(root, borderwidth=5, width=25, textvariable=location)
    e3.place(x=690, y=200)

    label4 = Label(root, text="CONTACT NO", bg="magenta", fg="black", font=("bold", 12))
    label4.place(x=550, y=260)

    contact = IntVar()
    contact.set(" ")
    e4 = Entry(root, borderwidth=5, width=25, textvariable=contact)
    e4.place(x=690, y=260)

    label5 = Label(root, text="GENDER     ", bg="magenta", fg="black", font=("bold", 12))
    label5.place(x=550, y=320)

    clicked4 = StringVar()
    clicked4.set("GENDER")
    drop4 = OptionMenu(root, clicked4, "Male", "Female", "Other")
    drop4.place(x=690, y=320)

    label6 = Label(root, text="GENDER \nPREFERENCE", bg="magenta", fg="black", font=("bold", 12))
    label6.place(x=550, y=380)

    clicked5 = StringVar()
    clicked5.set("GENDER")
    drop5 = OptionMenu(root, clicked5, "Male", "Female", "Other")
    drop5.place(x=690, y=380)

    label6 = Label(root, text="PROFESSION  ", bg="magenta", fg="black", font=("bold", 12))
    label6.place(x=550, y=440)

    profession = StringVar()
    e5 = Entry(root, borderwidth=5, width=25, textvariable=profession)
    e5.place(x=690, y=440)

    label7 = Label(root, text="AGE  ", bg="magenta", fg="black", font=("bold", 12))
    label7.place(x=550, y=500)

    age = IntVar()
    age.set(" ")
    e7 = Entry(root, borderwidth=5, width=25, textvariable=age)
    e7.place(x=690, y=500)

    def connect():

        global img, hobbies, des, uname, password, c_password

        top = Toplevel()
        top.title("REGISTRATION")
        top.geometry("1400x1000")

        img = Image.open("Background2.png")
        resized = img.resize((1400, 900), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized)

        label1 = Label(top, image=img)
        label1.place(x=0, y=0)

        title = Label(top, text="REGISTRATION FORM", fg="white", bg="blue", font=("bold", 15))
        title.place(x=550, y=30)

        label2 = Label(top, text="USERNAME  ", bg="magenta", fg="blue", font=("bold", 13))
        label2.place(x=500, y=300)

        def on_entry_click1(event):
            if e1.get() == 'Email-ID/Phone no.':
                e1.delete(0, "end")
                e1.insert(0, '')
                e1.config(fg='black')

        uname = StringVar()
        e1 = Entry(top, width=25, borderwidth=5, textvariable=uname)
        e1.place(x=650, y=300)
        e1.insert(0, "Email-ID/Phone no.")
        e1.bind('<FocusIn>', on_entry_click1)
        e1.config(fg='grey', font=("bold", 10))

        label2 = Label(top, text="PASSWORD  ", bg="magenta", fg="blue", font=("bold", 13))
        label2.place(x=500, y=360)

        def on_entry_click2(event):
            if e2.get() == 'Minimum 8 characters':
                e2.delete(0, "end")
                e2.insert(0, '')
                e2.config(fg='black')

        password = StringVar()
        e2 = Entry(top, width=25, borderwidth=5, textvariable=password)
        e2.place(x=650, y=360)
        e2.insert(0, "Minimum 8 characters")
        e2.bind('<FocusIn>', on_entry_click2)
        e2.config(fg='grey', font=("bold", 10))

        label2 = Label(top, text="CONFIRM \nPASSWORD  ", bg="magenta", fg="blue", font=("bold", 13))
        label2.place(x=500, y=420)

        c_password = StringVar()
        e3 = Entry(top, width=30,show = '*', borderwidth=5, textvariable=c_password)
        e3.place(x=650, y=420)

        label3 = Label(top, text="HOBBIES  ", bg="magenta", fg="blue", font=("bold", 13))
        label3.place(x=500, y=180)

        hobbies = StringVar()
        e4 = Entry(top, width=25, borderwidth=5, textvariable=hobbies)
        e4.place(x=650, y=180)

        label4 = Label(top, text="PERSONAL \nQUESTION  ", bg="magenta", fg="blue", font=("bold", 13))
        label4.place(x=500, y=230)

        des = StringVar()
        e5 = Entry(top, width=25, borderwidth=5, textvariable=des)
        e5.place(x=650, y=240)

        #b_back = Button(top, text="BACK", bg="blue", fg="white", font=("bold", 13))
        #b_back.place(x=500, y=540)

        def con1():
            a = e2.get()
            b = e3.get()
            if(e3.get() == "" or e4.get() == "" or e5.get() == ""):
                tsmg.showinfo("Error","Fill the Details")
            elif(len(a) < 8):
                tsmg.showinfo("Error","Invalid Password")
            elif(a != b):
                tsmg.showinfo("Error","Password not matched")
            else:
                con()

        b_submit = Button(top, text="NEXT",borderwidth = 5, command=con1, bg="blue", fg="white",padx = 25, font=("bold", 13))
        b_submit.place(x=600, y=540)

        top.mainloop()

    def connect1():
        a = e4.get()
        if(e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or E12.get == ""):
            tsmg.showinfo("Error", "Fill the details")
        elif(e2.get() != ""):
            if(re.search(regex,e2.get())):
                if (len(a) != 11):
                    tsmg.showinfo("Error", "Invalid Contact Number")
                else:
                    connect()
            else:
                tsmg.showinfo("Error","Invalid Email")

    #b1 = Button(root, text="BACK", bg="blue", fg="white", font=("bold", 13))
    b2 = Button(root, text="NEXT", bg="blue",borderwidth = 5, fg="white", font=("bold", 13),padx = 25, command=connect1)

    #b1.place(x=550, y=570)
    b2.place(x=650, y=570)

    root.mainloop()

title = Label(root20,text="LOGIN FORM",bg="black",fg="white",font=("italic",15))
title.place(x=600,y=200)

label1 = Label(root20,text="USERNAME    : ",bg="pink",fg="red",font=("bold",10))
label1.place(x=525,y=300)

uname=StringVar()
e1 = Entry(root20,borderwidth=5,textvariable=uname)
e1.place(x=700,y=300)

label2 = Label(root20,text="PASSWORD    : ",bg="pink",fg="red",font=("bold",10))
label2.place(x=525,y=350)

password = StringVar()
e2 = Entry(root20,borderwidth=5,show = '*',textvariable=password)
e2.place(x=700,y=350)

def validate1():
    if uname.get() == "" and password.get() == "" :
        tsmg.showerror("ERROR","FILL THE DETAILS")
    else :
        root20.destroy()
        validate()

b1 = Button(root20,text="LOGIN",bg="blue",padx = 30,fg="white",font=("bold",10),borderwidth=5,command=validate1)
b1.place(x=525,y=450)

def register1():
    root20.destroy()
    register()

b2 = Button(root20,text="REGISTER",bg="blue",padx = 30,fg="white",font=("bold",10),borderwidth=5,command = register1)
b2.place(x=700,y=450)

root20.mainloop()
