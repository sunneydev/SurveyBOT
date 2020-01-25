import json
import names
from twilio.rest import Client
from selenium import webdriver
from time import sleep
from random import randrange
from datetime import date
from Survey import globalDeclaration
from twilio.base.exceptions import TwilioRestException, TwilioException
from json.decoder import JSONDecodeError

smslist = []

def rannames():
    global fname, lname, parentName

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

def checkList():
    global passAddress, zip_code, fname, lname, parentName
    print("1. Generate random names\n2. No, I have my own names\n")
    anw1 = input("> ")
    if anw1 == "1":
        rannames()
    elif anw1 == "2":
        fname = input("First Name\n> ")
        print("")
        lname = input("Last Name\n> ")
        parentName = names.get_first_name(gender="male") + " " + lname
    else:
        print("Input 1 or 2 only")
        checkList()
    zip_code = input("\nZip Code:\n> ")
    passAddress = input("\nAddress:\n> ")
    print("\nName - %s %s\nParent Name - %s\nZip Code - %s\nAddress - %s" % (fname, lname, parentName, zip_code, passAddress))
    print("\n\nAre you sure you want to proceed?\n1. Yes\n2. No")
    anw2 = input("> ")
    if anw2 == "1":
        credentialCheck()
    elif anw2 == "2":
        checkList()
    else:
        print("Not sure I understand. Please try again.")
        checkList()

def credentialCheck():
    try:
        with open("credentials.json") as key:
            data = json.load(key)

            if len(data['accountid']) == 34:
                create_new_number(data['accountid'], data['accounttoken'])
            else:
                raise KeyError
    except (KeyError, JSONDecodeError, FileNotFoundError, KeyError):
        print("\nPlease Enter credentials manually")
        acid = input("Account ID\n> ")
        act = input("Account Token\n> ")
        with open("credentials.json", "w") as w:
            data = {"accountid": acid, "accounttoken": act}
            json.dump(data, w)
        create_new_number(acid, act)

# Gets all the values required to then PASS it to another function
def create_new_number(id, token):
    global client
    client = Client(id, token)

    try:
        local = client.available_phone_numbers('US').local.list(area_code=626, limit=1)
        incoming_phone_number = client.incoming_phone_numbers.create(phone_number=local[0].phone_number)
    except TwilioException:
        print("\nCouldn't Login\nTry again!")
        with open("credentials.json", "w") as clear:
            return credentialCheck()

    print("\nLogin of Twilio was successful... \nProceeding with the program")
    global numberf
    global numbersid
    numberf = incoming_phone_number.friendly_name
    numbersid = incoming_phone_number.sid
    smsCheck(numberf, id, token)

# Gets all the values required to then PASS it to another function
def passValues(numbersf):
    global date_of_birth, emailaddy
    address = passAddress
    number =  numbersf
    emailcheck = input("Name - %s %s\nEmail Address: \n> " % (fname, lname))
    emailanswercheck = input("Are you sure?\n1. Yes\n2. No\n> ")
    if emailanswercheck == "1":
        emailaddy = emailcheck
    elif emailanswercheck == "2":
        emailaddy = input("\nInput Email\n> ")
    else:
        passValues(numbersf)
    date_of_birth = dob
    createFulllist(fname, lname, address, zip_code, number, emailaddy, date_of_birth)

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
    passValues(number)

# Executes the values and sends them to credentials.json and starts the browser
def createFulllist(firstname, lastname, address, zip_code, number, emailaddy, date_of_birth):
    element_names = {
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
    detail_names = {
    "Names": firstname + " " + lastname,
    "Addresses": passAddress,
    "Phone Numbers": number,
    "Email Addresses": emailaddy,
    "Birthdays": date_of_birth
    }
    try:
        with open("details.json") as r:

            data = json.load(r)
            desirableDict = data.copy()

            for key in data.keys():
                if key in detail_names:
                    if type(data[key]) is list:
                        data[key].extend([detail_names[key],])
                    else:
                        desirableDict[key] = [data[key],detail_names[key]]
        with open("details.json",'w') as f:
            f.write(json.dumps(desirableDict, indent=4, sort_keys=False))

    except (JSONDecodeError, FileNotFoundError):
        with open("details.json", "w") as w:
            json.dump(detail_names, w)

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
        variables(variable, variableValues)
    b.find_element_by_name("submit-btn-saverecord").click()

    globalDeclaration(b, date_of_birth.split("-")[2], emailaddy)

checkList()
