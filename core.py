from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.keys import Keys



def save(val,val1,val2):
    print(val+val1+val2)
    pass




def flip_search(driver,product,url):
    driver.get(url)
    try:
        login_pop = driver.find_element_by_class_name('_29YdH8')
        # Here .click function use to tap on desire elements of webpage
        login_pop.click()
        print('pop-up closed')
    
    except:
        print("log in")
        
    # Here I get search field id from driver
    search_field = driver.find_element_by_class_name('LM6RPg')
    # Here .send_keys is use to input text in search field
    search_field.send_keys(product + '\n')
    # Here time.sleep is used to add delay for loading context in browser
    #time.sleep(2)
    # Here we fetched driver page source from driver.
    #page_html = driver.page_source
    # Here BeautifulSoup is dump page source into html format
    #soup = BeautifulSoup(page_html, 'html.parser')
    #driver.quit()
    url=driver.current_url
    return url


def amaz_search(driver,product,url):
    print (product)
    driver.get(url)
    
        
    # Here I get search field id from driver
    search_field=driver.find_element_by_xpath("""//*[@id="twotabsearchtextbox"]""")
    # Here .send_keys is use to input text in search field
    search_field.send_keys(product)
    search_field.submit()
    # Here time.sleep is used to add delay for loading context in browser
    #time.sleep(2)
    # Here we fetched driver page source from driver.
    #page_html = driver.page_source
    # Here BeautifulSoup is dump page source into html format
    #soup = BeautifulSoup(page_html, 'html.parser')
    #driver.quit()
    url=driver.current_url
    return url


    
def product_search(browser,product):
    
    #print (product)
    
    def search():
        #print("entered")
        #print(product) 
                  
        if (radio.get()==1):
            url="https://www.flipkart.com"
            #matched_elements = browser.get("https://www.flipkart.com")
            #search=browser.find_element_by_xpath("""//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input""")
            #element_enter.findElement(By.xpath("""""")).sendkeys(barcode);
            #search.send_keys(product)
            #search.submit()
            #soup=BeautifulSoup(browser.page_source,'html.parser')
            
            #print(soup)
            url=flip_search(browser,product,url)
            tk.withdraw()
             
        
        elif (radio.get()==2):
            url="https://www.amazon.in"
            #matched_elements = browser.get("https://www.amazon.com") 
            #soup=BeautifulSoup(browser.page_source,'html.parser')
            #print(soup)
            
            url=amaz_search(browser,product,url)
            tk.withdraw()
            
        
        else:
            ans=messagebox.askquestion("Confirm","Select a E-commerse site or did you give a url?\neg:https://www.site_name.com/product_name")  
            if (ans=="yes"):
                matched_elements = browser.get(product)
                tk.withdraw()
                url=browser.current_url
                
           
            #matched_elements = driver.get("https://"++)
    
        
            
        


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
    url=browser.current_url
    return url
    
        
        
def set_browser(browser,product):
    #print(str(radio.get()))
    

    if (browser=="google crome"):
        driver_path = os.path.join(os.getcwd(), 'chromedriver')
        browserdriver = webdriver.Chrome(driver_path)
        url=product_search(browserdriver,product)
        
           
    elif (browser=="microsoft edge"):
        driver_path = os.path.join(os.getcwd(), '')
        browserdriver = webdriver.Edge(driver_path)
        url=product_search(browserdriver,product)
        
              
    elif (browser=="mozilla firefox"):
        driver_path = os.path.join(os.getcwd(), '')
        browserdriver = webdriver.Firefox(driver_path)
        url=product_search(browserdriver,product)
        
    return url
    
            
        
        
def compare(browser,product):
    
    if (browser=="google crome"):
        driver_path = os.path.join(os.getcwd(), 'chromedriver')
        browserdriver = webdriver.Chrome(driver_path)
        url="https://www.flipkart.com"
        url1="https://www.amazon.in"
        urls=flip_search(browserdriver,product,url)
        #print (browserdriver.current_url)
        browserdriver.execute_script('''window.open("about:blank", "_blank");''')
        browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        browserdriver.switch_to.window(browserdriver.window_handles[1])
        #actions = ActionChains(browserdriver)      
        #actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
        #body = browserdriver.find_element_by_tag_name("body")
        #body.send_keys(Keys.CONTROL + 't')
        urls1=amaz_search(browserdriver,product,url1)
        #print (browserdriver.current_url)
        #product_search(browserdriver,product)
        return urls,urls1
        
           
    elif (browser=="microsoft edge"):
        driver_path = os.path.join(os.getcwd(), '')
        browserdriver = webdriver.Edge(driver_path)
        url="https://www.flipkart.com"
        url1="https://www.amazon.in"
        urls=flip_search(browserdriver,product,url)
        browserdriver.execute_script('''window.open("about:blank", "_blank");''')
        browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        browserdriver.switch_to.window(browserdriver.window_handles[1])
        urls1=amaz_search(browserdriver1,product,url1)
        #product_search(browserdriver,product)
        return urls,urls1
        
              
    elif (browser=="mozilla firefox"):
        driver_path = os.path.join(os.getcwd(), '')
        browserdriver = webdriver.Firefox(driver_path)
        url="https://www.flipkart.com"
        url1="https://www.amazon.in"
        urls=flip_search(browserdriver,product,url)
        browserdriver.execute_script('''window.open("about:blank", "_blank");''')
        browserdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        browserdriver.switch_to.window(browserdriver.window_handles[1])
        urls1=amaz_search(browserdriver1,product,url1)
        #product_search(browserdriver,product)
        return urls,urls1
    
        
    
def send_mail():
    
    pass
   


val3=""
val,val1=compare("google crome","watch")
save(val,val1,val3)
