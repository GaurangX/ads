"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".
"""
"""
Run time complexity:
- Function call_duration iterates over list of calls. That for loop is O(n).
- Within for loop the if conditions check for items in a dictionary. Python
hashtable look up is O(1) profiler does not show any hash conflicts.
- Find_longest function uses sorted. Unlike sort, sorted in python is not in place.
Time complextiy of sorted is o(n log n). While it also requires O(n) space complexity.
It is also iterating over a list O(n).
"""
# (TODO): Technically texting is time spent on phone.
#         How to account for texting duration?
#         Tx Model: (avg text size) * (avg. texting speed char/sec)
#         Rx Model: (avg text size) * (avg. reading speed char/sec)
def call_duration(calls):
  call_tt = {}
  for i in range(len(calls)):
    if calls[i][0] in call_tt:
      call_tt[calls[i][0]] += int(calls[i][3])
    else:
      call_tt[calls[i][0]] = int(calls[i][3])
    # account for answering calls
    if calls[i][1] in call_tt:
      call_tt[calls[i][1]] += int(calls[i][3])
    else:
      call_tt[calls[i][1]] = int(calls[i][3])
  return call_tt

def find_longest (call_tt):
  longest_call = sorted(call_tt.values())
  for num,dur in call_tt.items():
    if longest_call[len(longest_call)-1] == dur :
      return (num, dur)

def main():
  call_dur = call_duration(calls)
  [number, duration] = find_longest(call_dur)
  print ("%s spent the longest time, %s seconds, on the phone," \
         "during September 2016." % (number, duration))

if __name__ == "__main__":
  main()
  #import profile
  #profile.run("main()")

