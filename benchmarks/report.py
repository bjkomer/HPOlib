# This script takes an output file as an argument, and returns a list of results
# as well as the best result found in the file

import sys
import re

def main( filename, optimizer='hyperopt' ):
  rfile = open( filename, 'r' )
  results = []
  if 'smac' in filename:
    optimizer='smac'
  if optimizer=='hyperopt':
    for line in rfile.readlines():
      if 'Result:' in line:
        try:
          results.append( float(re.findall("-?\d+.\d+", line)[0]) )
        except:
          results.append( float(re.findall("-?\d+", line)[0]) )
  if optimizer=='smac':
    for line in rfile.readlines():
      if 'Performance of the Incumbent:' in line:
        try:
          results.append( float(re.findall("-?\d+.\d+", line)[0]) )
        except:
          results.append( float(re.findall("-?\d+", line)[0]) )

  print( min( results ) )
  print( len( results ) )


if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( sys.argv[1] )
  elif len ( sys.argv ) == 3:
    main( sys.argv[1], sys.argv[2] )
