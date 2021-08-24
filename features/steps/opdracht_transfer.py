from behave import*

def transfer_money(balance, amount, max_amount):
    if balance- amount < 0:
        transfer_money == False
    elif amount > max_amount:
        transfer_money == False
    else:
        transfer_money == True

#background

@given(u'I have 5000 euro in my bank account')
def step_impl(context):
    context.geld = 5000


@given(u'my bank allows me to transfer 1000 euro max')
def step_impl(context):
    context.max_transfer = 1000
        
#scenario

@when(u'I transfer {geld} euro to my friends bank account')
def step_impl(context, geld):
    transfer_money(context.geld, int(geld), context.max_transfer)


@then(u'the money has {tekst} been transferred')
def step_impl(context, tekst):
    if transfer_money != None:
        assert tekst

     
    



