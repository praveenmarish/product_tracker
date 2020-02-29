from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from bs4 import BeautifulSoup


    
def product_search(browser,product):
    
    print (product)
    
    def search():
        #print("entered")
        #print(product) 
                  
        if (radio.get()==1):
            matched_elements = browser.get("https://www.flipkart.com")
            soup=BeautifulSoup(browser.page_source,'html.parser')
            print(soup)
            pass
        elif (radio.get()==2):
            matched_elements = browser.get("https://www.amazon.com") 
            soup=BeautifulSoup(browser.page_source,'html.parser')
            print(soup)
            pass
        else:
            ans=messagebox.askquestion("Confirm","Select a E-commerse site or did you give a url?\neg:https://www.site_name.com")  
            if (ans=="yes"):
                matched_elements = browser.get(product)
                tk.withdraw()
                pass
            
            else:
                pass
            #matched_elements = driver.get("https://"++)
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
    b1=Button(tk,text="Ok",width=9,command=search)
    b1.pack()
    tk.mainloop()
    pass
    
        
        
def set_browser(browser,product):
    #print(str(radio.get()))
    
    if (browser=="google crome"):
        browserdriver = webdriver.Chrome('chromedriver')
        product_search(browserdriver,product)
        pass
           
    elif (browser=="microsoft edge"):
        browserdriver = webdriver.Edge()
        product_search(browserdriver,product)
        pass
              
    elif (browser=="mozilla firefox"):
        browserdriver = webdriver.Firefox()
        product_search(browserdriver,product)
        pass 
            
        
        
def compare():
    
    pass
def send_mail():
    
    pass

set_browser("google crome","https://www.amazon.com/")
