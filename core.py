from tkinter import *
from tkinter import messagebox
from selenium import webdriver


    
def search(browser,product):
    
    print (product)
    
    def product_search(driver):
         
        if(str(radio.get())==0):
                  
            pass
                  
        elif (radio.get()==1):
            matched_elements = driver.get("https://www.youtube.com")
            pass
        elif (radio.get()==2):
            matched_elements = driver.get("https://www.youtube.com")             
            pass
    
    def set_browser():
        #print(str(radio.get()))
        
        if (browser=="google crome"):
            browserdriver = webdriver.Chrome('chromedriver')
            product_search(browserdriver)
            pass
            
        elif (browser=="microsoft edge"):
            browserdriver = webdriver.Edge()
            product_search(browserdriver)
            pass
            
        elif (browser=="mozilla firefox"):
            browserdriver = webdriver.Firefox()
            product_search(browserdriver)
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
    b1=Button(tk,text="Ok",width=9,command=set_browser)
    b1.pack()
    tk.mainloop()
    pass
    
        
        
def compare():
    
    pass
def send_mail():
    
    pass

