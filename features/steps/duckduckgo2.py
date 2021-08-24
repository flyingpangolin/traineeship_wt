from behave import *
from splinter.browser import Browser 
from time import sleep
import logging
from hamcrest import assert_that, contains, equal_to

@given(u'is the webbrowser googlechrome')
def step_impl(context):
   context.browser = Browser('chrome')
   logging.info("The program has started")

@when(u'I go to DuckDuckGo')
def step_impl(context):
    context.browser.visit("https://duckduckgo.com") 
    

@when(u'search for raspberry pi retro website')
def step_impl(context):
    context.browser.fill('q', 'raspberry pi retro website')        
    context.button = context.browser.find_by_id('search_button_homepage')  
    context.button.click()                                         
    sleep(7)
    context.browser.quit()
    
@then(u'I will find rasberry pi retro websites')
def step_impl(context):
    assert context.browser != None   # moet nog anders

# scenario2

@when(u'search for from my bowl')
def step_impl(context):
    context.browser.fill('q', 'from my bowl')        
    context.button = context.browser.find_by_id('search_button_homepage')  
    context.button.click()                                         
    sleep(3)
    

@when(u'click on the link')
def step_impl(context):
    context.browser.click_link_by_href("https://frommybowl.com/")
    sleep(3)
    

@then(u'I will be on the website from my bowl')
def step_impl(context):
    assert_that( context.browser.url,  equal_to("https://frommybowl.com/"))
    