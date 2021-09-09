from behave import *
import requests
 
@given('I want open a page')
def step_impl(context):
    pass

@when('I request GET')
def step_impl(context):
   context.resp = requests.get("http://httpbin.org/get")
 
@then('I should receive an OK response')
def step_impl(context):
   assert context.resp.status_code is 200 
 
@then('I should have my origin ip')
def step_impl(context):
    assert context.resp.json()['origin'] == '201.141.218.29'


@given('I want open results')
def step_impl(context):
    pass

@when('I GET the URI')
def step_impl(context):
   context.resp = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
 
@then('I check that http response has status code 200')
def step_impl(context):
   assert context.resp.status_code is 200 


@given('I have this URI')
def step_impl(context):
    for row in context.table:
        model.add_user(name=row['name'], value=row['value'])



 