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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
"""
The run time complexity of accessing python list is O(1)
get length is also O(1)
"""

sxt = texts[0][0]
rxt = texts[0][1]
tt = texts[0][2]
print ("First record of texts, %s texts %s at time %s" %(sxt, rxt, tt))
total_calls = len(calls)-1
sxc = calls[total_calls][0]
rxc = calls[total_calls][1]
tc = calls[total_calls][2]
dc = calls[total_calls][3]
print ("Last record of calls, %s calls %s at time %s lasting %s" %(sxc, rxc, tc, dc))
