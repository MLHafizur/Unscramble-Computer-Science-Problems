"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoingCalls = []
recevingCalls = []

telemarketersCalls = []

for call in calls:
    outgoingNumber = call[0]
    receivingNumber = call[1]

    if outgoingNumber not in outgoingCalls:
        outgoingCalls.append(outgoingNumber)
    
    if receivingNumber not in recevingCalls:
        recevingCalls.append(receivingNumber)

outgoingTexts = []
receivingTexts = []

for text in texts:
    outgoingNumber = text[0]
    receivingNumber = text[1]

    if outgoingNumber not in outgoingTexts:
        outgoingTexts.append(outgoingNumber)
    
    if receivingNumber not in receivingTexts:
        receivingTexts.append(receivingNumber)

for cellNumber in outgoingCalls:
    if((cellNumber not in recevingCalls) and (cellNumber not in outgoingTexts) and (cellNumber not in receivingTexts)):
        telemarketersCalls.append(cellNumber)

print("These numbers could be telemarketers: ")
print(*sorted(telemarketersCalls), sep='\n')
# print(len(telemarketersCallslist))