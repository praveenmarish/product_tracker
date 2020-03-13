#core operations

from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient 
from warning import warnings
from PyQt5 import QtCore, QtGui, QtWidgets


class operations:


    def __init__(self,browser,product,emailid,password,targetid):
        self.url="https://www.flipkart.com"
        self.url1="https://www.amazon.in"
        self.url3="https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AddSession"
        self.browser=browser
        self.product=product
        self.emailid=emailid
        self.password=password
        self.targetid=targetid
        self.window=QtWidgets.QMainWindow()
        try:
            self.conn = MongoClient("mongodb://localhost:27017/")
            self.db = self.conn.database 
            self.collection = self.db.sites
            self.cursor = self.collection.find()

        except:
            
            self.ui=warnings("Problem on connecting to database")
        
    
    def save(self,product,url):
        try:
            product_entry = {
                "product_name":product, 
                "URL":url
                } 

            self.collection.insert_one(product_entry)
        
        except:
            
            self.ui=warnings("Problem on database")
            

    def show_link(self):
        try:
            product_name=""
            url=""
            for record in self.cursor:
                for key,value in record.items():
                    for _i in range (2):
                        if (key=="product_name"):
                            product_name=value
                        elif (key=="URL"):
                            url=value
                if (product_name!="" and url!=""):
                    return product_name,url

        except:
            
            self.ui=warnings("Problem on database")


    def delete(self,product,url):
        try:
            self.collection = self.db.sites 
            self.collection.delete_one = {
                "product_name":product, 
                "URL":url
                } 

        except:
           
            self.ui=warnings("Problem on database")

        
    def send_mail(self,product,url):
        try:
            self.browserdriver.get(self.url3)
            user_name_field = self.browserdriver.find_element_by_xpath("""//*[@id="identifierId"]""")
            user_name_field.send_keys(self.emailid)
            u_form_next = self.browserdriver.find_element_by_class_name('CwaK9')
            u_form_next.click()
            self.browserdriver.implicitly_wait(40)
            password_field=self.browserdriver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""")
            password_field.send_keys(self.password)
            p_form_next=self.browserdriver.find_element_by_class_name('CwaK9')
            p_form_next.click()
            self.browserdriver.implicitly_wait(40)
            compose=self.browserdriver.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
            compose.click()
            self.browserdriver.implicitly_wait(40)
            to_address=self.browserdriver.find_elements_by_xpath("""//*[@id=":pk"]""")
            to_address.send_keys(self.targetid)
            subject=self.browserdriver.find_elements_by_xpath("""//*[@id=":p2"]""")
            subject.send_keys(product)
            condent=self.browserdriver.find_elements_by_xpath("""//*[@id=":q7"]""")
            condent.send_keys(url)
            self.browserdriver.implicitly_wait(40)
            send=self.browserdriver.find_element_by_class_name('T-I J-J5-Ji aoO v7 T-I-atl L3')
            send.click()
        
        except:
            
            self.ui=warnings("Problem on sending mail")      

            
    def compare(self):

        try:
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

        except:
            
            self.ui=warnings("Problem on searching")
            
            
    def amaz_search(self):
        try:
            self.browserdriver.get(self.url1)
            search_field=self.browserdriver.find_element_by_xpath("""//*[@id="twotabsearchtextbox"]""")
            search_field.send_keys(self.product)
            search_field.submit()

        except:
            
            self.ui=warnings("Problem on searching")
        
        
    def flip_search(self):
        try:
            self.browserdriver.get(self.url)
            login_pop = self.browserdriver.find_element_by_class_name('_29YdH8')
            login_pop.click()
            search_field = self.browserdriver.find_element_by_class_name('LM6RPg')
            search_field.send_keys(self.product + '\n')

        except:
            self.ui=warnings("Problem on searching")
        
    
    def set_browser(self):
             
        try:
            if (self.browser=="google crome"):
                driver_path = os.path.join(os.getcwd(), 'chromedriver')
                self.browserdriver = webdriver.Chrome(driver_path)
        
           
            elif (self.browser=="microsoft edge"):
                driver_path = os.path.join(os.getcwd(), '')
                self.browserdriver = webdriver.Edge(driver_path)
        
              
            elif (self.browser=="mozilla firefox"):
                driver_path = os.path.join(os.getcwd(), '')
                self.browserdriver = webdriver.Firefox(driver_path)

        except:
            
            self.ui=warnings("Problem on opening browser")

   