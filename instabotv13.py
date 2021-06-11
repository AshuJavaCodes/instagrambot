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
from tkinter import messagebox as tkMessageBox
import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import * 
from tkinter.ttk import Progressbar
from selenium.common.exceptions import NoSuchElementException
print("\n")
result = pyfiglet.figlet_format("Instagram Bot v 1.2", font = "digital" ) 
print(result)
window = tk.Tk()
window.title("Instagram Bot")
driver = webdriver.Firefox()
#------------------------------------------------------
def notnow():
    notnow_button = driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
    try:
        notnow_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    except NoSuchElementException:
        notnow_button = driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
    pass
    time.sleep(2)
def Info_bot():
    tkMessageBox.showinfo("Information","Instagram Bot Made By : \n Ashutosh,Atul,Indresh \n Special Thanks to Namrata Choudhary For Guiding us. \n  id is : insta_bot_aia Current demo pass is : orientalinstabotaia")
notnow_button = ttk.Button(window, text = "Information about Instagram Bot",command = Info_bot)
notnow_button.grid(row =3,column=0)
# ----------------------------------------------------
#-------------------PROGRESS BAR-------------------------------
# progress = Progressbar(pl1, orient = HORIZONTAL, length = 100, mode = 'determinate')
# ------------------------------------------------------------------
def login(usr_og,pss,delay_login):
#-------------------------------------------------
    try:
        pl1  = Toplevel(window)
        pl1.title("Login Progress is Shown Here !")
        pl1.geometry('350x100')
        progress = Progressbar(pl1, orient = HORIZONTAL, length = 100, mode = 'determinate')
        progress['value'] =20
        pl1_label = ttk.Label(pl1,text = " Login progress ::")
        pl1_label.grid(row=0,column=0)
        pl1.update_idletasks()
        progress.grid(row=0,column =2)
#------------------------------------------------------------------
        time.sleep(delay_login)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        usr_ent.clear()
        usr_ent.send_keys(usr_og)
        time.sleep(2)
    #------------------------------------------------------------
        progress['value'] = 20
        pl1_label = ttk.Label(pl1,text = "Login progress ::")
        pl1_label.grid(row=0,column=0)
        pl1.update_idletasks()
        progress.grid(row=0,column =2)
    #----------------------------------------------------------------------
        pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        pss_ent.clear()
        pss_ent.send_keys(pss)
        time.sleep(2)
    #---------------------------------------------------------
        progress['value'] = 60
        pl1_label = ttk.Label(pl1,text = "Login progress ::")
        pl1_label.grid(row=0,column=0)
        pl1.update_idletasks()
        progress.grid(row=0,column =2)
    #------------------------------------------------------------------
        login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
        login.click()
        time.sleep(4)
        progress['value'] = 100
    #------------------------------------------------------------
        notnow()
        pl1_label = ttk.Label(pl1,text = "Login Progress ::")
        pl1_label.grid(row=0,column=0)
        progress.grid(row=0,column =2)
        pl1_close_button = ttk.Button(pl1, text = "Login Done !", command = pl1.destroy)
        pl1_close_button.grid(row=1,column=0)
    except NoSuchElementException:
        try:
            not_login = driver.find_element_by_id("slfErrorAlert")
            tkMessageBox.showinfo("Information","Incorrect Password or Username ! \n Please Try Again !")
            progress['value'] =5
            pl1_label = ttk.Label(pl1,text = " Login process Interrupted ::")
            pl1_label.grid(row=0,column=0)
            pl1.update_idletasks()
            progress.grid(row=0,column =2)
            pl1.destroy()
        except NoSuchElementException:
            tkMessageBox.showinfo("Information","Notifications already disabled.")
    pass
    time.sleep(2)
#-------------------------------------------------------------------
    # tkMessageBox.showinfo("Information","Login Done.")
def like_post(post_og,d3):
    time.sleep(d3)
    driver.get(f"{post_og}")
    like_poster = driver.find_element_by_class_name('wpO6b').click()
    time.sleep(2)
def comment(post_link_og,comment_og,d2):
    time.sleep(d2)
    driver.get(f"{post_link_og}")
    comment_click = driver.find_element_by_css_selector("._15y0l > button:nth-child(1)").click()
    cmt_click2 = driver.find_element_by_class_name("Ypffh").send_keys(f"{comment}") # right
    cmt_click4 = driver.find_element_by_css_selector(".X7cDz>button:nth-child(2)").click()
def message(user_og,info_msg_og,d6):
    print("Please be patient it would take around 30 SECONDS to send desired message.") 
    msg_click1 = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
    msg_click2 = driver.find_element_by_css_selector(".sqdOP").click()
    time.sleep(4)
    msg_find = driver.find_element_by_css_selector(".j_2Hd")
    time.sleep(4)
    msg_find.send_keys(f"{user_og}")
    time.sleep(6)
    click_user = driver.find_element_by_css_selector("div.qyrsm").click()
    time.sleep(6)
    msg_nxt = driver.find_element_by_css_selector(".cB_4K").click()
    time.sleep(6)
    msg_entr = driver.find_element_by_css_selector("div.Igw0E:nth-child(3)>textarea:nth-child(1)").click()
    pyautogui.typewrite(f"{info_msg_og}")
    time.sleep(d6)
    msg_send =  driver.find_element_by_css_selector("div.Igw0E:nth-child(4)>button:nth-child(1)").click() 
def explore_and_follow(explore_term_og,link_to_profile,d4):
    time.sleep(d4)
    inputElement = driver.find_element_by_css_selector('.XTCLo')
    inputElement.send_keys(f"{explore_term_og}")
    inputElement.send_keys(Keys.ENTER)
    driver.get(f"{link_to_profile}")
    time.sleep(2)
    follow_click = driver.find_element_by_css_selector("._6VtSN").click()
    time.sleep(5)
def unfollow(profile_lnk_og,d7):
    time.sleep(d7)
    driver.get(f"{profile_lnk_og}")
    click1 = driver.find_element_by_css_selector('._6VtSN').click()
    time.sleep(2)
    click_final =  driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]').click()
    time.sleep(2)
def private(d5):
    time.sleep(d5)
    driver.get("https://www.instagram.com/accounts/privacy_and_security/")
    private_click =  driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/section[1]/div/div/div/label/div").click()
    time.sleep(3)
def block(blockog,d8):
    time.sleep(d8)
    driver.get("https://www.instagram.com/indresh_pawar/")
    block_click1 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
    block_click2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]").click()
    block_click3 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/button[1]").click()
    time.sleep(4)
def pass_change_ogg(old_password_ogg,new_password_ogg,confirm_new_pass_ogg):
    click1_pass_change = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
    time.sleep(1)
    click2_pass_change = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
    time.sleep(1)
    click3_pass_change =  driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]").click()
    time.sleep(1)
    input_old_pass_ogg = driver.find_element_by_id("cppOldPassword")
    time.sleep(1)
    input_old_pass_ogg.send_keys(f"{old_password_ogg}")
    time.sleep(1)
    input_new_pass_ogg = driver.find_element_by_id("cppNewPassword")
    time.sleep(1)
    input_new_pass_ogg.send_keys(f"{new_password_ogg}")
    time.sleep(1)
    confirm_new_input_ogg = driver.find_element_by_id("cppConfirmPassword")
    time.sleep(1)
    confirm_new_input_ogg.send_keys(f"{confirm_new_pass_ogg}")
    time.sleep(4)
    change_pass_button_ogg = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div/button").click()
    tkMessageBox.showinfo("Information","Password Changed Successfully.")
     
def loginbt():
    btu1 = u1.get()
    btpss = pss1.get()
    d1_login_bt = d1ttk.get()
    login(btu1,btpss,d1_login_bt)
    # notnow()
#---------------------------------------------
login_button = ttk.Button(window, text = "LOGIN",command = loginbt)
login_button.grid(row =3,column=1)
# ------------------------------------------------
userttk = ttk.Label(window,text ="enter your username :: ")
userttk.grid(row = 0,column =0, sticky = tk.W)
u1 = tk.StringVar()
user_entryttk =  ttk.Entry(window, width = 16, textvariable = u1)
user_entryttk.grid(row= 0,column=1)
# --------------------------------------
psstk = ttk.Label(window, text ="enter your password :: ")
psstk.grid(row = 1,column =0, sticky = tk.W)
pss1 = tk.StringVar()
pss_entry =  ttk.Entry(window, width = 16, textvariable = pss1,show ="*")
pss_entry.grid(row= 1,column=1)
# ------------------------------------------
delaylogintk = ttk.Label(window, text ="Delay time for login :: ")
delaylogintk.grid(row = 2,column =0, sticky = tk.W)
d1ttk = tk.IntVar()
d1ttk_entry =  ttk.Entry(window, width = 5, textvariable = d1ttk)
d1ttk_entry.grid(row= 2,column=1)
#------------------------------------------------------
# def notnow():
    # notnow_button = driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
    # try:
        # notnow_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    # except NoSuchElementException:
        # notnow_button.driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
    # pass
    # time.sleep(2)
# notnow_button = ttk.Button(window, text = "Click to Get no notifications from Instagram.",command = notnow)
# notnow_button.grid(row =3,column=0)
# ----------------------------------------------------
def reset():
    time.sleep(2)
    print("Intiating Reset please wait for a moment.....")
    driver.get("https://www.google.com/")
    driver.delete_all_cookies()
    time.sleep(2)
    driver.delete_all_cookies()
    print("Cookies Cleared")
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    print("Logging out !")
    log_out =driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
    time.sleep(2)
    log_out2 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
    time.sleep(2)
    log_out3 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[9]").click()
    time.sleep(2)
    user_entryttk.delete(0, "end")
    pss_entry.delete(0,"end")
    print("Reset Completed !")    
reset_button = ttk.Button(window, text = "Reset and Restart (Under Development)",command = reset)
reset_button.grid(row =4,column=0)
# ---------------------------------------------------------
def closebrowser():
    driver.quit()
    window.destroy()
close_button = ttk.Button(window, text = "Close Browser",command = closebrowser)
close_button.grid(row =5,column=0)
# --------------------------------------------------------------
def featuresMenu():
     
    # Toplevel object which will  
    # be treated as a new window 
    fm = Toplevel(window)
    #-------------------PROGRESS BAR-------------------------------
    progress = Progressbar(fm, orient = HORIZONTAL, length = 100, mode = 'determinate')
    #-------------------------------------------------------------------------  
    #sets the title of the 
    # Toplevel widget
# -------------------------------------- 
    fm.title("Features of InstaBot")
    fmpostttk = ttk.Label(fm,text ="Post link ::  ")
    fmpostttk.grid(row = 0,column =0, sticky = tk.W)
    fmpost1 = tk.StringVar()
    fmpost_entryttk =  ttk.Entry(fm, width = 16, textvariable = fmpost1)
    fmpost_entryttk.grid(row= 0,column=1)
# -----------------------------------------------
    delayposttk = ttk.Label(fm, text ="Delay time for post like :: ")
    delayposttk.grid(row = 1,column =0, sticky = tk.W)
    fmd1ttk = tk.IntVar()
    fmd1ttk_entry =  ttk.Entry(fm, width = 5, textvariable = fmd1ttk)
    fmd1ttk_entry.grid(row= 1,column=1)
# ------------------------------------------------------
    def likebt():
        og_like = fmpost1.get()
        og_delay = fmd1ttk.get()
        like_post(og_like,og_delay)
        
    like_button = ttk.Button(fm, text = "LIKE",command = likebt)
    like_button.grid(row =1,column=2)
#---------------------------------------------------------
    fmcommentttk = ttk.Label(fm,text ="Comment link ::  ")
    fmcommentttk.grid(row = 2,column =0, sticky = tk.W)
    fmcomment1 = tk.StringVar()
    fmcomment_entryttk =  ttk.Entry(fm, width = 16, textvariable = fmcomment1)
    fmcomment_entryttk.grid(row= 2,column=1)
# -----------------------------------------------
    fmcommentinfottk = ttk.Label(fm , text = "What comment :: ")
    fmcommentinfottk.grid(row = 3,column = 0, sticky  =tk.W)
    fmcmtinfotkk = tk.StringVar()
    fmcmtinfottk_entry = ttk.Entry(fm, width = 16, textvariable  = fmcmtinfotkk)
    fmcmtinfottk_entry.grid(row =3,column=1)
#---------------------------------------------------------
    delaycommenttk = ttk.Label(fm, text ="Delay time for post like :: ")
    delaycommenttk.grid(row = 4,column =0, sticky = tk.W)
    fmd2ttk = tk.IntVar()
    fmd2ttk_entry =  ttk.Entry(fm, width = 5, textvariable = fmd2ttk)
    fmd2ttk_entry.grid(row= 4,column=1)
# ------------------------------------------------------
    def commentbt():
        og_cmt = fmcomment1.get()
        og_cmt_delay = fmd2ttk.get()
        ogg_comment_info = fmcmtinfotkk.get()
        comment(og_cmt,ogg_comment_info,og_cmt_delay) 
    comment_button = ttk.Button(fm, text = "Comment",command = commentbt)
    comment_button.grid(row =4,column=2)
#---------------------------------------------------------
    fmexpttk = ttk.Label(fm,text ="explore term ::  ")
    fmexpttk.grid(row = 5,column =0, sticky = tk.W)
    fmexp1 = tk.StringVar()
    fmexp_entryttk =  ttk.Entry(fm, width = 16, textvariable = fmexp1)
    fmexp_entryttk.grid(row= 5,column=1)
# -----------------------------------------------
    pflnktk = ttk.Label(fm, text ="profile link :: ")
    pflnktk.grid(row = 6,column =0, sticky = tk.W)
    fmpfttk = tk.StringVar()
    pflnk_entry =  ttk.Entry(fm, width = 16, textvariable = fmpfttk)
    pflnk_entry.grid(row= 6,column=1)
#----------------------------------------------------
    delayfollowtk = ttk.Label(fm, text ="Delay time for following::  ")
    delayfollowtk.grid(row = 7,column =0, sticky = tk.W)
    fmfollowttk = tk.IntVar()
    fmfollowttk_entry =  ttk.Entry(fm, width = 5, textvariable = fmfollowttk)
    fmfollowttk_entry.grid(row= 7,column=1)
# ------------------------------------------------------
    def followbt():
        explore_term_ogg = fmexp1.get()
        profile_link_ogg = fmpfttk.get()
        delay_follow_ogg = fmfollowttk.get()
        explore_and_follow(explore_term_ogg,profile_link_ogg,delay_follow_ogg) 
    follow_button = ttk.Button(fm, text = "FOLLOW",command = followbt)
    follow_button.grid(row =7,column=2)
#---------------------------------------------------------
    fmblockttk = ttk.Label(fm,text ="block link ::   ")
    fmblockttk.grid(row = 8,column =0, sticky = tk.W)
    fmblock12 = tk.StringVar()
    fmblock_entryttk =  ttk.Entry(fm, width = 16, textvariable = fmblock12)
    fmblock_entryttk.grid(row= 8,column=1)
# -----------------------------------------------
    delayblocktk = ttk.Label(fm, text ="Delay time for blocking ")
    delayblocktk.grid(row = 9,column =0, sticky = tk.W)
    fmblockdttk = tk.IntVar()
    fmblockttk_entry =  ttk.Entry(fm, width = 5, textvariable = fmblockdttk)
    fmblockttk_entry.grid(row= 9,column=1)
# ------------------------------------------------------
    def blockbt():
        block_link_ogg = fmblock12.get()
        block_delay_ogg = fmblockdttk.get()
        block(block_link_ogg,block_delay_ogg) 
    block_button = ttk.Button(fm, text = "BLOCK",command = blockbt)
    block_button.grid(row =9,column=2)
#---------------------------------------------------------
#---------------------------------------------------------
    fmmsgttk = ttk.Label(fm,text =" TO username ::  ")
    fmmsgttk.grid(row = 10,column =0, sticky = tk.W)
    fmmsg1 = tk.StringVar()
    fmmsg_entryttk =  ttk.Entry(fm, width = 16, textvariable = fmmsg1)
    fmmsg_entryttk.grid(row= 10,column=1)
# -----------------------------------------------
    infotk = ttk.Label(fm, text ="type the message :: ")
    infotk.grid(row = 11,column =0, sticky = tk.W)
    fminfottk = tk.StringVar()
    info_entry =  ttk.Entry(fm, width = 16, textvariable = fminfottk)
    info_entry.grid(row= 11,column=1)
#----------------------------------------------------
    delaymessagetk = ttk.Label(fm, text ="Delay time for message ::  ")
    delaymessagetk.grid(row = 12,column =0, sticky = tk.W)
    fmmessagettk = tk.IntVar()
    fmmessagettk_entry =  ttk.Entry(fm, width = 5, textvariable = fmmessagettk)
    fmmessagettk_entry.grid(row= 12,column=1)
#-----------------------------------------------
    def messagebt():
        message_user_ogg = fmmsg1.get()
        message_user_info_ogg =fminfottk.get()
        message_delay_ogg = fmmessagettk.get()
        message(message_user_ogg,message_user_info_ogg,message_delay_ogg)
    message_button = ttk.Button(fm, text = "SEND",command = messagebt)
    message_button.grid(row =12,column=2)
#-----------------------------------------------
    private_button = ttk.Button(fm, text = "Switch 2 Private A/c",command = private)
    private_button.grid(row =13,column=2)
#----------------------------------------------------
    unfollowlnktk = ttk.Label(fm, text =" unfollow profile link :: ")
    unfollowlnktk.grid(row = 14,column =0, sticky = tk.W)
    fmunfollowttk = tk.StringVar()
    unfollowlnk_entry =  ttk.Entry(fm, width = 16, textvariable = fmunfollowttk)
    unfollowlnk_entry.grid(row= 14,column=1)
#----------------------------------------------------
    delayunfollowtk = ttk.Label(fm, text ="Delay time for un-following::  ")
    delayunfollowtk.grid(row = 15,column =0, sticky = tk.W)
    fmun1followttk = tk.IntVar()
    fmunfollowttk_entry =  ttk.Entry(fm, width = 5, textvariable = fmunfollowttk)
    fmunfollowttk_entry.grid(row= 15,column=1)
# ------------------------------------------------------
    def unfollowbt():
        unfollow_user_link_ogg = fmunfollowttk.get()
        delay_unfollow_ogg = fmun1followttk.get()
        unfollow(unfollow_user_link_ogg,delay_unfollow_ogg)     
    unfollow_button = ttk.Button(fm, text = "unfollow",command = unfollowbt)
    unfollow_button.grid(row =15,column=2)
#--------------------------------------------------------------------

    fm.mainloop()
#--------------------------------------------------------------------------------   
feature_button = ttk.Button(window, text = "Feature Menu",command = featuresMenu)
feature_button.grid(row =6,column=0)
def advanceMenu():
    # tkMessageBox.showinfo("Information","Under Development")
    adm = Toplevel(window) 
    #sets the title of the 
    # Toplevel widget
# ------------------------------------------- 
    adm.title("Advance Features of Instabot")
#---------------------------------------------Begin Advance Features From Here !
    def passchangebt_enter():
        pss_change_menu = Toplevel(window)
        pss_change_menu.title("Change Password")
        #---------------------------------------------------
        pass_change_label = ttk.Label(pss_change_menu,text = "Enter current password here.")
        pass_change_label.grid(row=0,column= 0, sticky = tk.W)
        pss_change_old_var = tk.StringVar()
        pass_change_label_entry = ttk.Entry(pss_change_menu,textvariable = pss_change_old_var,show = "#")
        pass_change_label_entry.grid(row=0,column=1)
        #-------------------------------------------------------------------
        pass_change_current_label = ttk.Label(pss_change_menu,text = "Enter new password here.")
        pass_change_current_label.grid(row=1,column= 0, sticky = tk.W)
        current_x1 = tk.StringVar()
        pass_change_label_entry_current = ttk.Entry(pss_change_menu,textvariable = current_x1,show = "#")
        pass_change_label_entry_current.grid(row=1,column=1)
        #-------------------------------------------------------------------
        def passchangebt2():
            p1_old = pss_change_old_var.get()
            p2_current = current_x1.get()
            pass_change_ogg(p1_old,p2_current,p2_current)
        pass_change_confirm_btn = ttk.Button(pss_change_menu, text = "Change Password !!", command = passchangebt2)
        pass_change_confirm_btn.grid(row= 2,column = 0, sticky =tk.W)
    pass_change_button = ttk.Button(adm, text = "To Change Password",command = passchangebt_enter)
    pass_change_button.grid(row =1,column=2)
#----------------------------------------------
    adm.mainloop()
#----------------------------------------------

advance_feature_button = ttk.Button(window, text = "Advance feature Menu",command = advanceMenu)
advance_feature_button.grid(row=7,column=0)
window.mainloop()
if driver.quit() == True:
    window.destroy()
print("Closing the Browser. \n")
driver.quit()
print("400 LINES OF CODE DONE SUCCESSFULLY !")

print("Thanks for using Instabot v1.2 Made by Ashutosh,Indresh,Atul")
