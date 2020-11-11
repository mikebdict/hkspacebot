from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def facebook_poster_f(fbmsg, folder_filename_str):
    # Some long xpaths that we will need.
    create_post_xpath_str = ('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]'\
    +'/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div')
    enter_message_xpath_str = ('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]'\
    +'/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]'\
    +'/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div')
    add_photo_xpath_str = ('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/'\
    +'div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/'\
    +'div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/div/span/a/div[2]/input')
    subbmit_post_xpath_str = ('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/'\
    +'div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/'\
    +'div/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/span/button')
    # Absolute path for photo upload
    absolute_image_path_str = ''+folder_filename_str
    WINDOW_SIZE = "1920,1080"

    options = Options()
    # On the first run(s), you wont want to be in headless mode. During this time you should get
    #  the xpaths you need to make the posts and also save your account details so it can autologin when
    #  you set headless later.
    options.headless = True
    # Important for posting again and again with the same facebook account. Let Selenium save a
    # chrome dataprofile where it can save a username and password and session info for your facebook page.
    options.add_argument('--user-data-dir='+'')
    options.add_argument('--window-size=%s' % WINDOW_SIZE)
    options.add_argument('--no-sandbox')
    # Browser notifications can get in the way in headless mode
    options.add_argument('--disable-notifications')
    # options to disable some of chromes automation enabled features
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    selenium_chrome_instance = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # Open a log to save the bots progress in
    facebook_bot_log_li = []
    facebook_bot_log_li.append(f"{selenium_chrome_instance.capabilities['browserName']} version {selenium_chrome_instance.capabilities['browserVersion']} loaded")
    try:
        selenium_chrome_instance.get("")
        sleep(5)
        facebook_bot_log_li.append(f"Loaded page {selenium_chrome_instance.title}")
    except:
        facebook_bot_log_li.append('Couldnt log in exiting')
        selenium_chrome_instance.close()
        return(facebook_bot_log_li)
    # scroll down a bit to make sure the right xpath is visible
    selenium_chrome_instance.execute_script('window.scrollTo(0, 100)')
    sleep(1)
    # click create post <a> div
    try:
        selenium_chrome_instance.find_element_by_xpath(create_post_xpath_str).click()
        facebook_bot_log_li.append('Clicked create post')
        sleep(3)
    except:
        facebook_bot_log_li.append('Couldnt click create post')
        selenium_chrome_instance.close()
        return(facebook_bot_log_li)
    # Enter a message in the popup box
    try:
        selenium_chrome_instance.find_element_by_xpath(enter_message_xpath_str).send_keys(fbmsg)
        sleep(3)
        facebook_bot_log_li.append('Message entered')
    except:
        facebook_bot_log_li.append('Couldnt enter message')
        selenium_chrome_instance.close()
        return(facebook_bot_log_li)
    # add photo in the popup box
    try:
        selenium_chrome_instance.find_element_by_xpath(add_photo_xpath_str).send_keys(absolute_image_path_str)
        sleep(5)
        facebook_bot_log_li.append('Photo uploaded')
    except:
        facebook_bot_log_li.append('Couldnt upload image')
        selenium_chrome_instance.close()
        return(facebook_bot_log_li)
    # Click post in the popup box
    try:
        selenium_chrome_instance.find_element_by_xpath(subbmit_post_xpath_str).click()
        sleep(5)
        facebook_bot_log_li.append('Post created - exiting')
    except:
        facebook_bot_log_li.append('Createing post failed')
        selenium_chrome_instance.close
        return(facebook_bot_log_li)
    selenium_chrome_instance.close()
    return(facebook_bot_log_li)