from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys



class operations:
    def __init__(self,browser,product,emailid,password,targetid):
        url="https://www.flipkart.com"
        url1="https://www.amazon.in"
        self.browser=browser
        self.product=product
        self.emailid=emailid
        self.password=password
        self.targetid=targetid
        
        
    def save():
        print(self.browserdriver.current_url)
        pass
        
        
    def send_mail():
          
        pass

            
    def compare():
    
        if (browser=="google crome"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
               
        elif (browser=="microsoft edge"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
                  
        elif (browser=="mozilla firefox"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
            
            
    def amaz_search():
        self.browserdriver.get(url1)      
        search_field=self.browserdriver.find_element_by_xpath("""//*[@id="twotabsearchtextbox"]""")
        search_field.send_keys(self.product)
        search_field.submit()
    
        
        
    def flip_search():
        self.browserdriver.get(url)
        try:
            login_pop = browserdriver.find_element_by_class_name('_29YdH8')
            # Here .click function use to tap on desire elements of webpage
            login_pop.click()
            print('pop-up closed')
    
        except:
            print("log in")
        
        # Here I get search field id from driver
        search_field = self.browserdriver.find_element_by_class_name('LM6RPg')
        # Here .send_keys is use to input text in search field
        search_field.send_keys(self.product + '\n')      
        
        
        
    def product_search(self):
        def search():
           
            if (radio.get()==1):
                self.flip_search()
                tk.withdraw()
             
        
            elif (radio.get()==2):
                self.amaz_search()
                tk.withdraw()
                
        
            else:
                ans=messagebox.askquestion("Confirm","Select a E-commerse site or did you give a url?\neg:https://www.site_name.com/product_name")  
                if (ans=="yes"):
                    search = self.browserdriver.get(self.product)
                    tk.withdraw()
                   


        tk=Tk()
        tk.title("search")
        tk.geometry("250x150")
        l1=Label(tk,text="select a E-commerce site")
        l1.place(x=40,y=60)
        l1.pack()
        radio=IntVar()
        r1=Radiobutton(tk,text="flipkart",variable=radio,value=1)
        r2=Radiobutton(tk,text="amazon",variable=radio,value=2)
        r1.pack(anchor=W)
        r2.pack(anchor=W)
        l2=Label(tk,text="if you give URL of product,\nclick ok")
        l2.pack()
        b1=Button(tk,text="Ok",width=9,command=search)
        b1.pack()
        tk.mainloop()
        
        
        
    
    
    def set_browser(self):
       
        if (self.browser=="google crome"):
            driver_path = os.path.join(os.getcwd(), 'chromedriver')
            self.browserdriver = webdriver.Chrome(driver_path)
            self.product_search()
        
           
        elif (self.browser=="microsoft edge"):
            driver_path = os.path.join(os.getcwd(), '')
            self.browserdriver = webdriver.Edge(driver_path)
            self.product_search()
        
              
        elif (self.browser=="mozilla firefox"):
            driver_path = os.path.join(os.getcwd(), '')
            self.browserdriver = webdriver.Firefox(driver_path)
            self.product_search()
        
     