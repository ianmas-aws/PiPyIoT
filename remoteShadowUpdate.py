import boto3
import json

client = boto3.client('iot-data', region_name='eu-west-1')

while 1:
    str = raw_input("Enter sequence: ");
    print "Received sequence is : ", str
    state = '{ "state": { "desired": { "sequence": "' + str + '" } } }'
    print "Sending sequence", state    
    response = client.update_thing_shadow(
        thingName='Pi_Py_SDK',
        payload=state
    )
