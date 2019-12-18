import json
import names
from twilio.rest import Client
from selenium import webdriver
from time import sleep
from random import randrange
from datetime import date
from survey import globalDeclaration

print("Made by Sunney")
sleep(5)

smslist = []

fname = names.get_first_name(gender='female')
lname = names.get_last_name()
parentName = names.get_first_name(gender='male') + " " + lname

y = randrange(2002, 2006)
m = randrange(1, 12)
d = randrange(1, 27)

if m >= 10 and d >= 10:
    pass
elif m < 10 and d < 10:
    m = "0" + str(m)
    d = "0" + str(d)
elif m < 10 and d >= 10:
    m = "0" + str(m)
elif m >= 10 and d < 10:
    d = "0" + str(d)

dob = "%s-%s-%s" % (m, d, y)

element_names = {}
with open("sortLists.json") as l:
    addys = json.load(l)
    passAddress = addys['addresses'][0]
    del addys['addresses'][0]

with open("sortLists.json", "w") as w:
    json.dump(addys, w)

def jsonCheck():
    try:
        with open("credentials.json") as check:
            credentialCheck(check)
    except FileNotFoundError:
        with open("credentials.json", "w") as bew:
            bew.write("""{
            "accountid": "",
            "accounttoken": ""
            }""")
        credentialCheck(bew)
def credentialCheck(key):
    with open("credentials.json") as key:
        data = json.load(key)
        if len(data['accountid']) > 0:
            print("Success... \nProceeding with the program")
            create_new_number(data['accountid'], data['accounttoken'])
        elif len(data['accounttoken']) == 0:
            print("No credentials detected\nPlease input your credentials:")
            id = input("Account ID\n> ")
            token = input("Account Token\n> ")
            create_new_number(id, token)

# Gets all the values required to then PASS it to another function
def create_new_number(id, token):
    global client
    client = Client(id, token)

    local = client.available_phone_numbers('US').local.list(area_code=626, limit=1)

    incoming_phone_number = client.incoming_phone_numbers \
    .create(phone_number=local[0].phone_number)
    incoming_phone_number.sid

    global numberf
    global numbersid
    numberf = incoming_phone_number.friendly_name
    numbersid = incoming_phone_number.sid
    smsCheck(numberf, id, token)

# Gets all the values required to then PASS it to another function
def passValues(accid, acctoken, numbersf):
    accountid = accid
    accounttoken = acctoken
    address = passAddress
    zip_code = "91731"
    number =  numbersf
    emailaddy = input("Email Address: \n> ")
    global date_of_birth
    date_of_birth = dob
    createFulllist(accountid, accounttoken, fname, lname, address, zip_code, number, emailaddy, date_of_birth)

def smsCheck(number, id, token):
    c = webdriver.Firefox()
    c.get('http://j.mp/2W6LJXo')

    c.find_element_by_name("teen_first_name").send_keys(fname)
    c.find_element_by_name("teen_last_name").send_keys(lname)
    c.find_element_by_name("teen_phone").send_keys(number)
    c.find_element_by_name("parent_signature").send_keys(parentName)
    c.find_element_by_name("submit-btn-saverecord").click()
    print("Done... Now waiting for a message")
    c.close()
    sleep(10)

    for sms in client.messages.list(from_='+13233700072'): # Adds up messages to [smslist] that were sent from a specific number
        smslist.append(sms.body) # Adds message bodies to the list

    client.incoming_phone_numbers(numbersid).delete()
    global urls
    urls = smslist[0]
    passValues(id, token, number)

# Executes the values and sends them to credentials.json and starts the browser
def createFulllist(accountid, accounttoken, firstname, lastname, address, zip_code, number, emailaddy, date_of_birth):
    element_names = {
    "accountid": accountid,
    "accounttoken": accounttoken,
    "infromation_fname": firstname,
    "infromation_lname": lastname,
    "street_address": passAddress,
    "city_sis": "El Monte",
    "state_sis": "CA",
    "zip_code": "91731",
    "cell_phone_number": number,
    "email_address": emailaddy,
    "date_of_birth": date_of_birth
    }
    with open("credentials.json", "w") as ac:
        json.dump(element_names, ac)
        with open("Generated Details.json", "w") as w:
            w.write(json.dumps(element_names, sort_keys=True, indent=4))
    browserStart(urls, element_names)

def browserStart(url, list):
    element_names = list
    b = webdriver.Firefox()

    # Goes to the URL where it all starts and agrees with the survey statement
    b.get(url)
    b.find_element_by_xpath("//select[@name='agreement']/option[text()='I agree']").click()

    # Finds and CLICKS the FIRST submit button
    button = b.find_element_by_xpath("//button[@name='submit-btn-saverecord']")
    button.click()

    sleep(1) # Sleeps 5 seconds for other page to load

    # Function to return send_keys for each element and it's value we have
    def variables(elementName, elementValue):
        if elementName != "state_sis":
            value = b.find_element_by_name(elementName)
            value.send_keys(elementValue) # Deleted return
        elif elementName == "state_sis":
            b.find_element_by_xpath("//select[@name='state_sis']/option[text()='California']").click()

    # For variable in the list, send it through the function to send_keys
    for variable, variableValues in element_names.items():
        if variable != "accountid" and variable != "accounttoken":
            variables(variable, variableValues)
    b.find_element_by_name("submit-btn-saverecord").click()

    globalDeclaration(b, date_of_birth.split("-")[2])

jsonCheck()
