"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getCallsByMonthYear(phoneCall, month, year):

    timestamp = phoneCall[2]
    dt = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S')
    if(dt.year == year and dt.month == month):
        return True
    else:
        return False


"""
Add up the duration of all calls made
Save the data in a dictionary
"""


def trackCallDuration(dictionary, phoneNumber, callDuration):
    if(dictionary.get(phoneNumber) == None):
        dictionary[phoneNumber] = callDuration
    else:
        dictionary[phoneNumber] = int(
            dictionary.get(phoneNumber)) + int(callDuration)
    return dictionary


"""
Get all the phone calls made during September 2016
"""
records = filter(lambda x: getCallsByMonthYear(x, 9, 2016), calls)


"""
Track the duraction of the september calls that were made
"""
dictionary = {}
for record in records:
    outgoingNumber = record[0]
    recievingNumber = record[1]
    timestamp = record[2]
    callDuration = record[3]

    dictionary = trackCallDuration(dictionary, outgoingNumber, callDuration)
    dictionary = trackCallDuration(dictionary, recievingNumber, callDuration)


"""
Get the details for the phone number that spent the longest time spent on the phone during september 2016
"""
phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))


# print(len(list(records)))
# print(phoneMax);

print(f"{phoneMax[0]} spent the longest time, {phoneMax[1]} seconds, on the phone during September 2016.")