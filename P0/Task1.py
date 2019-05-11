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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Run time complexity:
  - get_freq has a for loop iterating over length of texts (a list of n
  lines from texts.csv) and another list of calls (a list of m lines from
  calls.csv). TIme complexities of those loops are of O(n) and O(m) respectively.
  Whithin each loop if condition checks a hashtable (python dictionary)
  called "phone_numbers". The worst case look up time is of O(1) and hence they
  do not contribute to the complexity of for loops.
  - find unique function iterates over the dictionary of length n items. Time
  complexity of this operation would be O(n). List append is O(1)
  - Aligns with python profile output:

"""

def get_freq (texts, calls):
  phone_numbers = {}
  for i in range(len(texts)):
    if texts[i][0] in phone_numbers:
      phone_numbers[texts[i][0]] += 1
    else:
      phone_numbers[texts[i][0]] = 1

    if texts[i][1] in phone_numbers:
      phone_numbers[texts[i][1]] += 1
    else:
      phone_numbers[texts[i][1]] = 1

  for i in range(len(calls)):
    if calls[i][0] in phone_numbers:
      phone_numbers[calls[i][0]] += 1
    else:
      phone_numbers[calls[i][0]] = 1

    if calls[i][1] in phone_numbers:
      phone_numbers[calls[i][1]] += 1
    else:
      phone_numbers[calls[i][1]] = 1
  return phone_numbers

def find_unique (phone_numbers):
  unique_pn = []
  for k,v in phone_numbers.items():
    if v >= 1:
      unique_pn.append(k)
  return unique_pn

def main():
  all_pn =  get_freq (texts, calls)
  print ("There are %d different telephone numbers in the records." %len(find_unique(all_pn)))

if __name__ == "__main__" :
  main()
  #import profile
  #profile.run("main()")


