from tkinter import *
import sys 
import json
from Naked.toolshed.shell import muterun_js
from PIL import ImageTk,Image  

class OwnerWindow:
   def __init__(self, win):
         self.win = win
         self.lbl1=Label(self.win, text='Owner Name', font=('Helvetica',12))
         self.t1=Entry(self.win, width=20, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.t1.place(x=150, y=50)
         self.b1=Button(self.win, text='Proceed', command=self.CallProg)
         self.b1.place(x=150, y=150)


   def CallProg(self):
      owner=self.t1.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(owner + "@")

      # Writing multiple strings
      # at a time
      #file1 = open('myfile', 'w')
      #L = [owner + "\n"]
      #file1.writelines(L)
  
      # Closing file
      #file1.close()
  
      # Checking if the data is
      # written to file or not
      #file1 = open('myfile', 'r')
      #print(file1.read())
      #file1.close()

      response = muterun_js('./dist/query_owner.js')

      s = str(response.stdout)
     
      start = "b'["
      end = "]\n'"

      x = s[3:][:-4]
      

      x = x.replace("\\'", "'")

      x = x.replace('},{', '}=:={')

      y = x.split('=:=')

      ctr=0
      y_coor=50
      for item in y:
         z = json.loads(y[ctr])
         ctr += 1

         result1=Label(self.win, text='Brand     :    ' + z["Record"]["Brand"], font=('Helvetica',12))
         result1.place(x=400, y=y_coor)

         result2=Label(self.win, text='Model     :    ' + z["Record"]["Model"], font=('Helvetica',12))
         y_coor += 20
         result2.place(x=400, y=y_coor)

         result3=Label(self.win, text='Serial No :    ' + z["Record"]["SerialNo"], font=('Helvetica',12))
         y_coor += 20
         result3.place(x=400, y=y_coor)


         result4=Label(self.win, text='Dealer     :   ' + z["Record"]["AuthDealer"], font=('Helvetica',12))
         y_coor += 20
         result4.place(x=400, y=y_coor)

         try:
            result5=Label(self.win, text='Ownership Date :  ' + z["Record"]["OwnershipDate"], font=('Helvetica',12))
            y_coor += 20
            result5.place(x=400, y=y_coor)
         except:
            print("No Key")
         

         y_coor += 50


class RegisterWindow:
   def __init__(self, win):
         self.win=win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.lbl2=Label(self.win, text='Dealer', font=('Helvetica',12))
         self.lbl3=Label(self.win, text='Brand', font=('Helvetica',12))
         self.lbl4=Label(self.win, text='Model', font=('Helvetica',12))
         self.lbl5=Label(self.win, text='Serial Number', font=('Helvetica',12))
         self.lbl6=Label(self.win, text='Owner Name', font=('Helvetica',12))
         self.lbl7=Label(self.win, text='Ownership Date', font=('Helvetica',12))
         self.lbl8=Label(self.win, text='Status', font=('Helvetica',12))
         self.t1=Entry(self.win, font=('Helvetica',12), bd=3)
         self.t2=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.t3=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.t4=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.t5=Entry(self.win, width=20, font=('Helvetica',12), bd=3)
         self.t6=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.t7=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.t8=Entry(self.win, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.lbl2.place(x=50, y=80)
         self.lbl3.place(x=50, y=110)
         self.lbl4.place(x=50, y=140)
         self.lbl5.place(x=50, y=170)
         self.lbl6.place(x=50, y=200)
         self.lbl7.place(x=50, y=230)
         self.lbl8.place(x=50, y=260)
         self.t1.place(x=200, y=50)
         self.t2.place(x=200, y=80)
         self.t3.place(x=200, y=110)
         self.t4.place(x=200, y=140)
         self.t5.place(x=200, y=170)
         self.t6.place(x=200, y=200)
         self.t7.place(x=200, y=230)
         self.t8.place(x=200, y=260)
         self.b1=Button(self.win, text='Submit', command=self.CallProg)
         self.b1.place(x=200, y=310)

   def CallProg(self):
      watchid=self.t1.get()
      dealer=self.t2.get()
      brand=self.t3.get()
      model=self.t4.get()
      serialnum=self.t5.get()
      owner=self.t6.get()
      ownership_date=self.t7.get()
      status=self.t8.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid + "@" + dealer  + "@" + brand + "@" + model + "@" + serialnum + "@" + owner + "@" + ownership_date + "@" + status)
  
      response = muterun_js('./dist/create_new_watch.js')

      s = str(response.stdout)

      x = s[2:][:-3]

      result1=Label(self.win, text='Transaction has been submitted' + x, font=('Helvetica',12))
      result1.place(x=200, y=350)

      
class WatchDetailsWindow:
   def __init__(self, win):
         self.win = win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.t1=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.t1.place(x=150, y=50)
         self.b1=Button(self.win, text='Proceed', command=self.CallProg)
         self.b1.place(x=150, y=150)


   def CallProg(self):
      watchid=self.t1.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid + "@")

      response = muterun_js('./dist/query_watch.js')

      s = str(response.stdout)
      print(s)
      start = "b'["
      end = "]\n'"

      x = s[2:][:-3]
      

      x = x.replace("\\'", "'")

      x = x.replace('},{', '}=:={')

      y = x.split('=:=')

      ctr=0
      y_coor=50
      for item in y:
         z = json.loads(y[ctr])
         ctr += 1

         result1=Label(self.win, text='Dealer :  ' + z["AuthDealer"], font=('Helvetica',12))
         y_coor += 20
         result1.place(x=500, y=y_coor)

         result2=Label(self.win, text='Brand :  ' + z["Brand"], font=('Helvetica',12))
         y_coor += 20
         result2.place(x=500, y=y_coor)

         result3=Label(self.win, text='Model :  ' + z["Model"], font=('Helvetica',12))
         y_coor += 20
         result3.place(x=500, y=y_coor)

         result4=Label(self.win, text='Owner :  ' + z["Owner"], font=('Helvetica',12))
         y_coor += 20
         result4.place(x=500, y=y_coor)

         try:
            result5=Label(self.win, text='Ownership Date :  ' + z["OwnershipDate"], font=('Helvetica',12))
            y_coor += 20
            result5.place(x=500, y=y_coor)
         except:
            print("No Key")

         result6=Label(self.win, text='Serial No :  ' + z["SerialNo"], font=('Helvetica',12))
         y_coor += 20
         result6.place(x=500, y=y_coor)

         result7=Label(self.win, text='Status :  ' + z["Status"], font=('Helvetica',12))
         y_coor += 20
         result7.place(x=500, y=y_coor)

         y_coor += 50
         

class WatchHistoryWindow:
   def __init__(self, win):
         self.win = win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.t1=Entry(self.win, width=30, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.t1.place(x=150, y=50)
         self.b1=Button(self.win, text='Proceed', command=self.CallProg)
         self.b1.place(x=150, y=150)


   def CallProg(self):
      watchid=self.t1.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid + "@")

      response = muterun_js('./dist/query_history.js')

      s = str(response.stdout)
      print(s)
      start = "b'["
      end = "]\n'"

      x = s[3:][:-4]
      

      x = x.replace("\\'", "'")

      x = x.replace('},{', '}=:={')

      y = x.split('=:=')

      ctr=0
      y_coor=50
      for item in y:
         z = json.loads(y[ctr])
         ctr += 1

         result1=Label(self.win, text='Dealer :  ' + z["Record"]["AuthDealer"], font=('Helvetica',12))
         y_coor += 20
         result1.place(x=500, y=y_coor)

         result2=Label(self.win, text='Brand :  ' + z["Record"]["Brand"], font=('Helvetica',12))
         y_coor += 20
         result2.place(x=500, y=y_coor)

         result3=Label(self.win, text='Model :  ' + z["Record"]["Model"], font=('Helvetica',12))
         y_coor += 20
         result3.place(x=500, y=y_coor)

         result4=Label(self.win, text='Owner :  ' + z["Record"]["Owner"], font=('Helvetica',12))
         y_coor += 20
         result4.place(x=500, y=y_coor)

         try:
            result5=Label(self.win, text='Ownership Date :  ' + z["Record"]["OwnershipDate"], font=('Helvetica',12))
            y_coor += 20
            result5.place(x=500, y=y_coor)
         except:
            print("No Key")

         result6=Label(self.win, text='Serial No :  ' + z["Record"]["SerialNo"], font=('Helvetica',12))
         y_coor += 20
         result6.place(x=500, y=y_coor)

         result7=Label(self.win, text='Status :  ' + z["Record"]["Status"], font=('Helvetica',12))
         y_coor += 20
         result7.place(x=500, y=y_coor)

         y_coor += 50


class WatchExistsWindow:
   def __init__(self, win):
         self.win = win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.t1=Entry(self.win,font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.t1.place(x=150, y=50)
         self.b1=Button(self.win, text='Proceed', command=self.CallProg)
         self.b1.place(x=150, y=100)
         self.b2=Button(self.win, text="Clear", command=clear_frame)
         self.b2.place(x=150, y=150)

   def CallProg(self):
      watchid=self.t1.get()       

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid)
  
      response = muterun_js('./dist/query_exists.js')

      s = str(response.stdout)

      x = s[2:][:-3]

      result1=Label(self.win, text=x, font=('Helvetica',12))
      result1.place(x=200, y=250)



class OwnerUpdateWindow:
   def __init__(self, win):
         self.win=win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.lbl2=Label(self.win, text='Owner Name', font=('Helvetica',12))
         self.lbl3=Label(self.win, text='Ownership Date', font=('Helvetica',12))
         self.t1=Entry(self.win, font=('Helvetica',12), bd=3)
         self.t2=Entry(self.win, font=('Helvetica',12), bd=3)
         self.t3=Entry(self.win, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.lbl2.place(x=50, y=80)
         self.lbl3.place(x=50, y=110)
         self.t1.place(x=200, y=50)
         self.t2.place(x=200, y=80)
         self.t3.place(x=200, y=110)
         self.b1=Button(self.win, text='Submit', command=self.CallProg)
         self.b1.place(x=200, y=170)

   def CallProg(self):
      watchid=self.t1.get()
      owner=self.t2.get()
      ownership_date=self.t3.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid + "@" + owner + "@" + ownership_date)
  
      response = muterun_js('./dist/update_ownership.js')

      s = str(response.stdout)

      x = s[2:][:-3]

      result1=Label(self.win, text='Result : ' + x, font=('Helvetica',12))
      result1.place(x=200, y=250)


class StatusUpdateWindow:
   def __init__(self, win):
         self.win=win
         self.lbl1=Label(self.win, text='Watch ID', font=('Helvetica',12))
         self.lbl2=Label(self.win, text='Status', font=('Helvetica',12))
         self.t1=Entry(self.win, font=('Helvetica',12), bd=3)
         self.t2=Entry(self.win, font=('Helvetica',12), bd=3)
         self.lbl1.place(x=50, y=50)
         self.lbl2.place(x=50, y=80)
         self.t1.place(x=200, y=50)
         self.t2.place(x=200, y=80)
         self.b1=Button(self.win, text='Submit', command=self.CallProg)
         self.b1.place(x=200, y=170)

   def CallProg(self):
      watchid=self.t1.get()
      status=self.t2.get()

      with open('myfile', 'w', encoding='utf8') as file1:
         file1.write(watchid + "@" + status)
  
      response = muterun_js('./dist/update_status.js')

      s = str(response.stdout)

      x = s[2:][:-3]

      result1=Label(self.win, text='Result : ' + x, font=('Helvetica',12))
      result1.place(x=200, y=250)


def RegisterFunc():
    clear_frame()
    regwin=RegisterWindow(topFrame)

def OwnerFunc():
    clear_frame()
    ownerwin=OwnerWindow(topFrame)

def OwnerUpdateFunc():
    clear_frame()
    ownerupdwin=OwnerUpdateWindow(topFrame)

def StatusUpdateFunc():
    clear_frame()
    statuswin=StatusUpdateWindow(topFrame)

def WatchExistsFunc():
    clear_frame()
    existswin=WatchExistsWindow(topFrame)

def WatchDetailsFunc():
    clear_frame()
    detailswin=WatchDetailsWindow(topFrame)

def WatchHistoryFunc():
    #canvas.delete('all')
    clear_frame()
    historywin=WatchHistoryWindow(topFrame)

def clear_frame():
   for widgets in topFrame.winfo_children():
      widgets.destroy()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


root = Tk()
root.geometry("1000x600+10+10")
root.title('CHRONOLEDGER')
root.wm_title("CHRONOLEDGER BLOCKCHAIN")

topFrame = Frame(root, width=9000, height=500)  # Added "container" Frame.
topFrame.pack(side=TOP, fill='both', expand=True, anchor=N)

#titleLabel = Label(topFrame, font=('arial', 12, 'bold'),text="CHRONOLEDGER BLOCKCHAIN", bd=5, anchor=NW)
#titleLabel.pack(side=LEFT)

#rightFrame = Frame(topFrame, width=400, height=550, bd=4, relief="ridge")
#rightFrame.pack(side=RIGHT,fill='both', expand=True, anchor=N)
#rightLabel = Label(rightFrame, font=('arial', 12, 'bold'), bd=5, anchor=E)
#rightLabel.pack()

#Bottom = Frame(root, width=1350, height=50, bd=4, relief="ridge")
#Bottom.pack(side=BOTTOM, fill=X, expand=1, anchor=S)

#lbl1=Label(rightFrame, text='Watch ID', font=('Helvetica',12))
#lbl1.place(x=50, y=50)

menubar = Menu(root)
submitmenu = Menu(menubar, tearoff=0)
submitmenu.add_command(label="Register New Watch", font=('Helvetica',15),command=RegisterFunc)
submitmenu.add_command(label="Update Watch Owner", font=('Helvetica',15), command=OwnerUpdateFunc)
submitmenu.add_command(label="Update Watch Status", font=('Helvetica',15), command=StatusUpdateFunc)
submitmenu.add_command(label="Delete Watch", font=('Helvetica',15), command=donothing)

submitmenu.add_separator()

submitmenu.add_command(label="Exit", font=('Helvetica',15), command=root.quit)
menubar.add_cascade(label="Submit", font=('Helvetica',15), menu=submitmenu)
querymenu = Menu(menubar, tearoff=0)
querymenu.add_command(label="Owner's Watch Collection", font=('Helvetica',15), command=OwnerFunc)
querymenu.add_command(label="Watch History by ID", font=('Helvetica',15), command=WatchHistoryFunc)
querymenu.add_command(label="Watch Asset by ID", font=('Helvetica',15), command=WatchDetailsFunc)
querymenu.add_command(label="Watch Exists", font=('Helvetica',15), command=WatchExistsFunc)
querymenu.add_command(label="All Watches by Brand", font=('Helvetica',15), command=donothing)
querymenu.add_command(label="Watch Status", font=('Helvetica',15), command=donothing)
querymenu.add_command(label="All Watch Assets", font=('Helvetica',15), command=donothing)


menubar.add_cascade(label="Query", font=('Helvetica',15), menu=querymenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", font=('Helvetica',15), command=donothing)
helpmenu.add_command(label="About...", font=('Helvetica',15), command=donothing)
menubar.add_cascade(label="Help", font=('Helvetica',15), menu=helpmenu)

canvas = Canvas(topFrame, width = 800, height = 700)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("patekimg.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 


root.config(menu=menubar)
root.mainloop()

