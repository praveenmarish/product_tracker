from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient 



class operations:
    def __init__(self,browser,product,emailid,password,targetid):
        self.url="https://www.flipkart.com"
        self.url1="https://www.amazon.in"
        self.browser=browser
        self.product=product
        self.emailid=emailid
        self.password=password
        self.targetid=targetid
        
        
    def save_link(self):
        def save():
            print(product)
            print(url)
                
            try: 
                conn = MongoClient() 
                print("Connected successfully!!!") 
            except:   
                print("Could not connect to MongoDB")
        
    
            # database 
            db = conn.database 
          
            # Created or Switched to collection names: my_gfg_collection 
            collection = db.sites 
  
            product_entry = {
                "product_name":product, 
                "URL":url
                } 
        
          
            # Insert Data 
            rec_id = collection.insert_one(product_entry) 
        
          
            print("Data inserted with record ids",rec_id)
            tk.withdraw()
            
            
            
        
        tk=Tk()
        tk.title("save to database")
        tk.geometry("450x200")
        l1=Label(tk,text="Fill the details to save")
        l1.place(x=40,y=60)
        l1.pack()
        l2=Label(tk,text="Enter product name:")
        l2.place(x=20,y=50)
        e1=Entry(tk,width = 40)
        e1.place(x=150,y=50)
        l3=Label(tk,text="URL")
        l3.place(x=20,y=100)
        
        e2=Entry(tk,width = 40)
        e2.place(x=150,y=100)
        product=e1.get()
        url=e2.get()
        
        b1=Button(tk,text="Save",width=10,command=save).place(x=200,y=140)
        tk.mainloop()
        
        
            
            
  

    def show_link():
        try:
            conn = MongoClient() 
            print("Connected successfully!!!") 
        except:   
            print("Could not connect to MongoDB")
        
    
        # database 
        db = conn.database 
      
        # Created or Switched to collection names: my_gfg_collection 
        collection = db.sites 
        cursor = collection.find() 
        for record in cursor:
            print(record) 
  

      
        
        
    def send_mail(self):
          
        pass

            
    def compare(self):
    
        if (self.browser=="google crome"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
               
        elif (self.browser=="microsoft edge"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
                  
        elif (self.browser=="mozilla firefox"):
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
            
            
    def amaz_search(self):
        self.browserdriver.get(self.url1)      
        search_field=self.browserdriver.find_element_by_xpath("""//*[@id="twotabsearchtextbox"]""")
        search_field.send_keys(self.product)
        search_field.submit()
        tk.withdraw()
    
        
        
    def flip_search(self):
        self.browserdriver.get(self.url)
        try:
            login_pop = self.browserdriver.find_element_by_class_name('_29YdH8')
            # Here .click function use to tap on desire elements of webpage
            login_pop.click()
            print('pop-up closed')
    
        except:
            print("log in")
        
        # Here I get search field id from driver
        search_field = self.browserdriver.find_element_by_class_name('LM6RPg')
        # Here .send_keys is use to input text in search field
        search_field.send_keys(self.product + '\n')
        tk.withdraw()
        
        
        
    def product_search(self):
        def search():
           
            if (radio.get()==1):
                self.flip_search()
                
             
        
            elif (radio.get()==2):
                self.amaz_search()
                
                
        
            elif(radio.get()==0):
                ans=messagebox.askquestion("Confirm","Select a E-commerse site or did you want to open browser?")  
                if (ans=="yes"):
                    self.browserdriver.get(self.product)
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
        
     
    