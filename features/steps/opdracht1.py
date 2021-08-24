from behave import*

def create_text_file(filename):
    f = open(filename, "wt")
    f.close()

def add_line_to_file(filename, this_line):
  f = open(filename, "at")
  f.write(this_line + "\n")
  f.close()

@given(u'There is an empty text file available to us')
def step_impl(context):
    context.mijn_bestands_naam = "probeer1.txt"
    create_text_file(context.mijn_bestands_naam)


@when(u'I write the following table in it')
def step_impl(context):
    for row in context.table:
        course = row["course"] 
        participants = row["participants"]
        add_line_to_file(context.mijn_bestands_naam, course + "\t" + participants)  

@when(u'I open this file and check the number of lines')
def step_impl(context):
    f = open(context.mijn_bestands_naam,'rt')
    context.aantal_regels= len(f.readlines())
    f.close()

@then(u'This file has 3 lines in it')
def step_impl(context):
    assert context.aantal_regels == 3

#scenario outline
@given(u'The text file has been opened')
def step_impl(context):
    context.mijn_bestands_naam = "some_records.txt"
    context.nieuw = open(context.mijn_bestands_naam, "at")
    

@then(u'I write the values {first}, {second} and {third}')
def step_impl(context, first, second, third):
    context.nieuw.write(first + "\t" + second + "\t" + third + "\n")
    

@then(u'I close the file')
def step_impl(context):
    context.nieuw.close()
    

