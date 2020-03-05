#core operations

from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient 



class operations:
    def Get_Data(self,browser,product,emailid,password,targetid):
        self.url="https://www.flipkart.com"
        self.url1="https://www.amazon.in"
        self.browser=browser
        self.product=product
        self.emailid=emailid
        self.password=password
        self.targetid=targetid
        
        
    def save_link(self):
        def save():
            
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
                "product_name":"product", 
                "URL":"url"
                } 
        
          
            # Insert Data 
            rec_id = collection.insert_one(product_entry) 
        
          
            print("Data inserted with record ids",rec_id)
            
            
            
            
       
        
            
            
  

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
        
     
    