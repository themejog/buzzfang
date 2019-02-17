# list services associated to breach on an email from have i been pwned

import requests
import json
import pprint
import sys

email = sys.argv[1]
breach_list = []

def haveibeenpwned(email):
    url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'+email
    response = requests.get(url)
    response.raise_for_status()
    breachData = json.loads(response.text)
    for i in range(len(breachData)):
        if breachData[i]['Title'] not in breach_list:
            breach_list.append(breachData[i]['Title'])
        else:
            continue
			

def breach_report(breach_list):
    if len(breach_list) > 0:
        print('Email %s is associated to the following services that have suffered from data breaches:' %(email))
        for i in breach_list:
            print('    * ' + i)
    else:
        print('Email %s is not associated with any know data breaches.' %(email))
        
#hackedemails(email)	
haveibeenpwned(email)
breach_report(breach_list)
