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
"""
Run time complexity:
  - find_telem: The for loops iterate over list of calls and texts respectively.
  They can be O(n) and O(m) where n is length  of calls and m is lengths of texts.
  It also has another loop that iterates over a call_tx list O(p) and the if
  condition checks for a number in concatenated list of call_ex and text O(q).
  That for loop has overall complexity of O(p*q). List append operations are O(1).
  - unique_telem: Iterates over list O(n) and creates a hash table O(1).
  - sort_and_print: An in place sort operation over a list O(n log n). And the
  for loop iterates over a sorted list O(m).
"""


def find_telem(calls, texts):
  call_tx = []
  call_rx = []
  text = []
  for i in range(len(calls)):
    call_tx.append(calls[i][0])
    call_rx.append(calls[i][1])

  for i in range(len(texts)):
    text.append(texts[i][0])
    text.append(texts[i][1])

  telem =[]
  for num in call_tx:
    if num not in (call_rx + text):
      telem.append(num)
  return (telem)

def unique_telem(telem):
  return list(set(telem))

def sort_and_print(uniq_num):
  uniq_num.sort()
  for i in uniq_num:
    print (i)

def main():
  num_list = find_telem(calls, texts)
  uniq_num = unique_telem(num_list)
  print ("These numbers could be telemarketers: ")
  sort_and_print(uniq_num)

if __name__ == "__main__":
  main()
  #import profile
  #profile.run("main()")
