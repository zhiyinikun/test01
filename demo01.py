import sys
try:
 s = input('Enter something --> ')
 print (s)
except EOFError:
 print ('\nWhy did you do an EOF on me?')
 sys.exit() # exit the program
except:
 print ('\nSome error/exception occurred.')
 # here, we are not exiting the program
print ('Done')