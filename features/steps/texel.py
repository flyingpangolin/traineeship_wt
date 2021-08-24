# from behave import *
# from splinter.browser import Browser 
# from time import sleep

# @given(u'we have a Texel website')
# def step_impl(context):
#     context.browser = Browser('chrome')
#     context.browser.visit("https://www.texel.net")
#     context.button = context.browser.find_by_text("...")  
#     context.button.click()  
             

# @when(u'I click on the agenda page')
# def step_impl(context):
#     context.button = context.browser.find_by_id('agenda')  
#     context.button.click()
#     sleep(3)


# @then(u'an agenda will be shown')
# def step_impl(context):
#     context.browser.quit()


# @when(u'I click on the zien_en_doen page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on the zien_en_doen page')


# @then(u'I will be able to see the eten&drinken page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I will be able to see the eten&drinken page')