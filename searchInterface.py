from tkinter import *
import tkinter.filedialog
from searchDatabase import searchDB
winroot = Tk()
winroot.geometry("300x350")
winroot.title('Chinese Rhymer Search Interface')
DBFILE ='db.xlsx'

fm1= Frame(winroot)
fm1L = Frame(fm1)
fm1R = Frame(fm1)
result_label = Label(fm1L,text= 'All result')
result_label.pack(side=TOP,fill=X)
result_listbox = Listbox(fm1L)
result_listbox.pack(side=BOTTOM, fill=BOTH,expand=YES)
double_label = Label(fm1R, text = 'Double Rhyme')
double_label.pack(side=TOP,fill=X)
double_listbox = Listbox(fm1R)
double_listbox.pack(side=BOTTOM, fill=BOTH,expand=YES)
fm1L.pack(side=LEFT, fill=BOTH,expand=YES)
fm1R.pack(side=RIGHT, fill=BOTH, expand=YES)
fm1.pack(side=TOP,expand=YES)

def choose_db():
    global DBFILE
    DBFILE =tkinter.filedialog.askopenfilename()
    db_label.config(text='Current DB = '+DBFILE)
def search():
    result_listbox.delete(0,END)
    double_listbox.delete(0,END)
    word = search_entry.get()
    resdict,doublerhy = searchDB(word,DBFILE)
    for item in resdict:
        result_listbox.insert(END,str(item))
    for item in doublerhy:
        double_listbox.insert(END, str(item))



fm2 = Frame(winroot)
search_label = Label(fm2,text='输入词汇：')
search_label.pack(side=LEFT)
search_entry = Entry(fm2)
search_entry.pack(side=LEFT,fill=X,expand=YES)
search_button = Button(fm2,text='Search',command=search)
search_button.pack(side=LEFT,expand=YES)
fm2.pack(side=TOP,fill=X, expand=YES)

fm3 = Frame(winroot)
db_label = Label(fm3, text='Current DB = '+DBFILE)
db_label.pack(side=LEFT, fill=X,expand=YES)
choose_db_button = Button(fm3,text='Select Database',command=choose_db)
choose_db_button.pack(side=RIGHT)
fm3.pack(fill=X, expand=YES)


winroot.mainloop()