#!/usr/bin/python

import sys
import simplejson as json

def main(argv):
  line = sys.stdin.readline()
  try:
    while line:
      word2count[word] = word2count.get(word, 0) + count

      line = sys.stdin.readline()
  except:
    return None
if __name__ == "__main__":
  main(sys.argv)











#!/usr/bin/python

import sys
import simplejson as json

def main(argv):

  count = {}

  for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
      count = int(count)
      word2count[word] = word2count.get(word, 0) + count
    except ValueError:
      # count was not a number, so silently
      # ignore/discard this line
      pass

# sort the words lexigraphically;
#
# this step is NOT required, we just do it so that our
# final output will look more like the official Hadoop
# word count examples
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

# write the results to STDOUT (standard output)
for word, count in sorted_word2count:
    print '%s\t%s'% (word, count)



