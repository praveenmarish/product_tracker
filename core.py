from tkinter import *
from tkinter import messagebox


    

    
    
def search(browser):
    
    def take():
        print(str(radio.get()))
        pass


    tk=Tk()
    tk.title("search")
    tk.geometry("300x100")
    l1=Label(tk,text="select a E-commerce site")
    l1.place(x=40,y=60)
    l1.pack()
    radio=IntVar()
    r1=Radiobutton(tk,text="flipkart",variable=radio,value=1)
    r2=Radiobutton(tk,text="amazon",variable=radio,value=2)
    r1.pack(anchor=W)
    r2.pack(anchor=W)
    b1=Button(tk,text="Ok",width=9,command=take)
    b1.pack()
    tk.mainloop()
    
    
        
    
        
        
def compare():
    pass
def send_mail():
    pass

search("")