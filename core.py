#core operations

from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient 



class operations:
    def __init__(self,browser,product,emailid,password,targetid):
        self.url="https://www.flipkart.com"
        self.url1="https://www.amazon.in"
        self.url3="https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3DOGB%26tab%3Drk1%26utm_medium%3Dapp&csig=AF-SEnb_VvdqbWeCSl9g%3A1583582267&flowName=GlifWebSignIn&flowEntry=AddSession"
        self.browser=browser
        self.product=product
        self.emailid=emailid
        self.password=password
        self.targetid=targetid
        
        
    
    def save(self,product,url):
            
        try: 
            conn = MongoClient("mongodb://localhost:27017/") 

        except:
            print("can't connect able to connect to db")  
           
        # database 
        db = conn.database 
          
        # Created or Switched to collection names: my_gfg_collection 
        collection = db.sites 
  
        product_entry = {
            "product_name":product, 
            "URL":url
            } 
        
          
        # Insert Data 
        collection.insert_one(product_entry) 
            
  

    def show_link(self):
        try:
            conn = MongoClient("mongodb://localhost:27017/") 
            
        except:   
            print("Could not connect to MongoDB")
        
    
        # database 
        db = conn.database 
      
        # Created or Switched to collection names: my_gfg_collection 
        collection = db.sites 
        cursor = collection.find() 
        for record in cursor:
            print(record) 
  

    def delete(self,product,url):
        try: 
            conn = MongoClient("mongodb://localhost:27017/") 

        except:
            print("can't connect able to connect to db")  
           
        # database 
        db = conn.database 
          
        # Created or Switched to collection names: my_gfg_collection 
        collection = db.sites 
  
        collection.delete_one = {
            "product_name":product, 
            "URL":url
            } 



        
        
    def send_mail(self):
        self.browserdriver.get(self.url3)
        user_name_field = self.browserdriver.find_element_by_xpath("""//*[@id="identifierId"]""")
        user_name_field.send_keys(self.emailid)
        u_form_next = self.browserdriver.find_element_by_class_name('CwaK9')
        u_form_next.click()
        #password_field=self.browserdriver.find_element_by_class_name('Xb9hP')
        #password_field.send_keys(self.password)
        self.browserdriver.implicitly_wait(20)
        password_field=self.browserdriver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""")
        #password_field=self.browserdriver.find_elements_by_name('password')
        #password_field.clear()
        password_field.send_keys(self.password)
        p_form_next=self.browserdriver.find_element_by_class_name('CwaK9')
        p_form_next.click()
       
        

            
    def compare(self):
    
        if (self.browser=="google crome"):
            self.set_browser()
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
               
        elif (self.browser=="microsoft edge"):
            self.set_browser()
            self.flip_search()
            self.browserdriver.execute_script('''window.open("about:blank", "_blank");''')
            self.browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            self.browserdriver.switch_to.window(self.browserdriver.window_handles[1])
            self.amaz_search()
            
            
                  
        elif (self.browser=="mozilla firefox"):
            self.set_browser()
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
        
    
        
        
    def flip_search(self):
        self.browserdriver.get(self.url)
        try:
            login_pop = self.browserdriver.find_element_by_class_name('_29YdH8')
            # Here .click function use to tap on desire elements of webpage
            login_pop.click()
            
        except:
            print("No pop-up")
        
        # Here I get search field id from driver
        search_field = self.browserdriver.find_element_by_class_name('LM6RPg')
        # Here .send_keys is use to input text in search field
        search_field.send_keys(self.product + '\n')
        
        
        
        
        
    
    
    def set_browser(self):
       
        if (self.browser=="google crome"):
            driver_path = os.path.join(os.getcwd(), 'chromedriver')
            self.browserdriver = webdriver.Chrome(driver_path)
            #self.product_search()
            pass
        
           
        elif (self.browser=="microsoft edge"):
            driver_path = os.path.join(os.getcwd(), '')
            self.browserdriver = webdriver.Edge(driver_path)
            #self.product_search()
            pass
        
              
        elif (self.browser=="mozilla firefox"):
            driver_path = os.path.join(os.getcwd(), '')
            self.browserdriver = webdriver.Firefox(driver_path)
            #self.product_search()
            pass
        
     
    