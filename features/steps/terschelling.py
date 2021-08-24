from behave import *
from splinter.browser import Browser 
from time import sleep
from hamcrest import assert_that, contains, equal_to
import logging

#background
@given(u'there is a Terschelling website')
def step_impl(context):
    context.browser = Browser('chrome')
    context.browser.visit("https://www.vvvterschelling.nl/")
     
@given(u'the cookies are accepted')
def step_impl(context): 
    if context.browser.is_element_present_by_id("popup-buttons")==False: 
       logging.error("There are no cookies to be accepted")
    else:
        context.button = context.browser.find_by_id('popup-buttons')  
        context.button.click() 
        logging.info("the cookies are accepted")

#scenario outline
@when(u'I click on the {menu} page')
def step_impl(context, menu):
    context.button = context.browser.find_by_text(menu).first  
    context.button.click()                                         
    sleep(5)  

@then(u'an {tabblad} will be shown')
def step_impl(context, tabblad):
    assert_that(context.browser.url, equal_to(tabblad))
    context.browser.quit()

#Scenario
@when(u'I click on Arrangementen')
def step_impl(context):
     context.button2 = context.browser.find_by_text("Arrangementen").first  
     context.button2.click()

@when(u'I search for Arrangementen from {begin} tot {einde}')
def step_impl(context, begin, einde):
     context.browser.fill('from[date]', begin)
     context.browser.fill("until[date]", einde)
     context.optie = context.browser.find_by_id("edit-search")  
     context.optie.click()
     sleep(3)

@then(u'I will be shown Het Bunker dagarrangement')
def step_impl(context):
    assert context.browser.is_text_present("Het Bunker Dagarrangement")
    context.browser.quit()  

@then(u'I will get a notification that you cannot search for dates in the past')
def step_impl(context):
    assert context.browser.is_element_present_by_css(".alert")


