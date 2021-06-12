from selenium import webdriver
from schedule import * 
import schedule 
import time as time_module 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import autoit
import sched
import pyfiglet

driver = webdriver.Firefox()
time.sleep(2)
driver.maximize_window()

print("\n")
result = pyfiglet.figlet_format("Instagram Bot.", font = "digital" ) 
print(result)
def login(usr,pss,delay_login):
    time.sleep(delay_login)
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    usr_ent.clear()
    usr_ent.send_keys(usr)
    time.sleep(2)

    pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    pss_ent.clear()
    pss_ent.send_keys(pss)
    time.sleep(2)

    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
    login.click()
    time.sleep(4)
def notnow():
    notnow_button = driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
    time.sleep(2)
def like_post(post,d3):
    time.sleep(d3)
    driver.get(f"{post}")
    like_poster = driver.find_element_by_class_name('wpO6b').click()
    time.sleep(2)
def comment(post_link,comment,d2):
    time.sleep(d2)
    driver.get(f"{post_link}")
    comment_click = driver.find_element_by_css_selector("._15y0l > button:nth-child(1)").click()
    cmt_click2 = driver.find_element_by_class_name("Ypffh").send_keys(f"{comment}") # right
    cmt_click4 = driver.find_element_by_css_selector(".X7cDz>button:nth-child(2)").click()
def message(user,info_msg,d6):
    print("Please be patient it would take around 30 SECONDS to send desired message.") 
    msg_click1 = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
    msg_click2 = driver.find_element_by_css_selector(".sqdOP").click()
    time.sleep(4)
    msg_find = driver.find_element_by_css_selector(".j_2Hd")
    time.sleep(4)
    msg_find.send_keys(f"{user}")
    time.sleep(6)
    click_user = driver.find_element_by_css_selector("div.qyrsm").click()
    time.sleep(6)
    msg_nxt = driver.find_element_by_css_selector(".cB_4K").click()
    time.sleep(6)
    msg_entr = driver.find_element_by_css_selector("div.Igw0E:nth-child(3)>textarea:nth-child(1)").click()
    pyautogui.typewrite(f"{info_msg}")
    time.sleep(d6)
    msg_send =  driver.find_element_by_css_selector("div.Igw0E:nth-child(4)>button:nth-child(1)").click() 
def explore_and_follow(explore_term,link_to_profile,d4):
    time.sleep(d4)
    inputElement = driver.find_element_by_css_selector('.XTCLo')
    inputElement.send_keys(f"{explore_term}")
    inputElement.send_keys(Keys.ENTER)
    driver.get(f"{link_to_profile}")
    time.sleep(2)
    follow_click = driver.find_element_by_css_selector("._6VtSN").click()
    time.sleep(5)
def unfollow(profile_lnk,d7):
    time.sleep(d7)
    driver.get(f"{profile_lnk}")
    click1 = driver.find_element_by_css_selector('._6VtSN').click()
    time.sleep(2)
    click_final =  driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]').click()
    time.sleep(2)
def private(d5):
    time.sleep(d5)
    driver.get("https://www.instagram.com/accounts/privacy_and_security/")
    private_click =  driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/section[1]/div/div/div/label/div").click()
    time.sleep(3)
def block(d8):
    time.sleep(d8)
    driver.get("https://www.instagram.com/indresh_pawar/")
    block_click1 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
    block_click2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]").click()
    block_click3 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/button[1]").click()
    time.sleep(4)
print("Enter the username and password to proceed :: ")
usrname = input("Enter the username :: ")
pssword = input("Enter the password  :: ")
print("Select Task to perform : ".center(200), "\n")
print("1. Comment on a post via a link".center(200), "\n")      
print("2. Like on a post via Link".center(200), "\n")
print("3. explore and follow (Enter the exact username please) ".center(200), "\n")
print("4. make the user account private (if not private)".center(200), "\n")
print("5. Message the user (takes 30 seconds to complete) ".center(200), "\n")
print("6. unfollow (if you are following the user)".center(200), "\n")
print("7.block the user".center(200), "\n")
print("8. Execute the task at particular time".center(200), "\n")
print("9. Close the Browser".center(200).center(200), "\n")
while True:
    delay_login_user = input("After how much time the login should begin  >> ")
    d1 = int(delay_login_user)
    # login(usrname,pssword,d1)
    # time.sleep(4)
    # notnow()

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice == '1':
        
           x1= str(input("Paste the link of the post on which you want to comment ::  "))
           cmt=str(input("Your comment you want to type ::  "))
           delay_cmt_user = input("After how much time the comment task should begin::  ")
           d2 = int(delay_cmt_user)
           login(usrname,pssword,d1)
           time.sleep(4)
           notnow()
           comment(x1,cmt,d2)
        elif choice == '2':
            li2=str(input("Link of the post you want to like. > "))
            delay_li_user = input("After how much time the like task should begin >  ")
            d3 = int(delay_li_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            like_post(li2,d3)
        elif choice == '3':
            exp1 = str(input("Enter the explore Term > "))
            exp2 = str(input("enter the user profile link > "))
            delay_exp_user = input("After how much time the explore task should begin :: > ")
            d4 = int(delay_exp_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            explore_and_follow(exp1,exp2,d4)
        elif choice == '4':
            delay_private_user = input("After how much time the private user task should begin  > ")
            d5 = int(delay_private_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            private(d5)
        elif choice == '5':
            usrMsg = str(input("Enter the username you want to send the message to : >  "))
            infoMsg = str(input("Enter the Message you want to send ::  >  "))
            delay_msg_user = input("After how much time the message task should begin  > ")
            d6 = int(delay_msg_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            message(usrMsg,infoMsg,d6)
        elif choice == '6':
            prlnk = str(input("Paste the Profile Link here :: "))
            delay_unfollow_user = input("After how much time the unfollow task should begin  > ")
            d7 = int(delay_unfollow_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            unfollow(prlnk,d7)
        elif choice == '7':
            blocklnk = str(input("Paste the profile link you want to block  > "))
            delay_block_user = input("After how much time the block task should begin  > ")
            d8 = int(delay_block_user)
            login(usrname,pssword,d1)
            time.sleep(4)
            notnow()
            block(blocklnk,d8)
        elif choice == '8':
            print("This Feature is under Developement please wait   > ")
            delay_8_user = input("After how much time the xxxx task should begin  >  ")
            d9 = int(delay_8_user)
            driver.close()
        elif choice == '9':
            delay_close_user = input("After how much time the closing task should begin > ")
            d10 = int(delay_close_user)
            time.sleep(d10)
            print("Closing Browser.")
        break
    else:
        print("Invalid Input")        
