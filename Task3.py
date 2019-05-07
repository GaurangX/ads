"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
"""
Run time complexity:
  - extract_cx_rx: Iterates over a list of calls, which is O(n). On top of that
  the string slice is basically a copy and would do O(m), where m is the
  length of string. Comparing to area code is O(1). Also, builds a default dict
  that maps one to many hash table.
  - extract_codes: iterates over a list O(n). Regex is basically a string
  matching. And the complexity can be O(m), where m is the length of string.
  - Find_unique: Basically iterating over a list of codes O(n) and addint it to a
  hash table O(1).
  - sort_and_print: Python's inplace sort method is O(n log n). Printing
  iterates over a list O(n).
  - Find_fix2fix: Iterates over a list O(n). Slicing of the string is O(m), m is
  length of string.
"""

# (TODO): Do mobile phones in banglore area have specific prefix?
def extract_cx_rx(calls):
  caller_rx = {}
  for i in range(len(calls)):
    if calls[i][0][0:5] == "(080)":
      key = calls[i][0]
      caller_rx.setdefault(key , []).append(calls[i][1])
  return caller_rx

def extract_codes(rx_list):
  codes = []
  code_patt = re.compile(r'(\d+)')
  for k,v in rx_list.items():
    for i in range(len(v)):
      result = code_patt.search(v[i])
      mob = result.group(0)[0]
      mob = v[i][0]
      if ((mob != '(')):
        codes.append(result.group(0)[0:4])
      else:
        codes.append(result.group(0))
  return codes

def find_unique(codes):
  return list(set(codes))

def sort_and_print (codes_unique):
  codes_unique.sort()
  print("The numbers called by people in Bangalore have codes:")
  for i in codes_unique:
    print (i)

def find_fix2fix(rx_list):
  count_ = 0
  for k,v in rx_list.items():
    for i in range(len(v)):
      if v[i][0:5] == "(080)":
        count_ += 1
  return (count_/len(calls)*100)

def main():
  rx_list = extract_cx_rx(calls)
  codes = extract_codes(rx_list)
  codes_unique = find_unique(codes)
  sort_and_print(codes_unique)
  find_fix2fix(rx_list)
  print ("%.2f percent of calls from fixed lines in Bangalore are calls" \
         "to other fixed lines in Bangalore." % find_fix2fix(rx_list))

if __name__ == "__main__":
  main()
  #import profile
  #profile.run("main()")



