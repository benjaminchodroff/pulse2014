import SoftLayer
import datetime
from pprint import pprint as pp
from private import apiKey
apiUsername="benjamin.chodroff"
# http://sldn.softlayer.com/article/python
client = SoftLayer.API.Client()
client = SoftLayer.API.Client(apiUsername, apiKey)
resp = client['Account'].getObject()
print "Company name: " + resp['companyName']
# prints 'IBM - JazzHub'
guests = client['Account'].getVirtualGuests()
for guest in guests:
    print guest

# prints all the machines we own

#http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
print "Creating a new Virtual Guest!"
newCCI = {
    'hostname': 'pulse2014',
    'domain': 'demo.com',
    'startCpus': 1,
    'maxMemory': 1024,
    'operatingSystemReferenceCode': 'CENTOS_6_64',
    'hourlyBillingFlag': True,
    'localDiskFlag': False,
    'networkComponents': [{'maxSpeed': 1000}],
    'datacenter': {'name': 'dal05'},
    'blockDevices': [{"device": "0", "diskImage": { "capacity": 100 }},{"device": "2", "diskImage": { "capacity": 250}} ],
    'postInstallScriptUri': "https://raw2.github.com/benjaminchodroff/pulse2014/master/install.sh"
}
# Warning: this does order the machine immediately and there are costs
result = client['Virtual_Guest'].createObject(newCCI)
pp(result)

#http://gettingstartedwithchef.com/first-steps-with-chef.html
