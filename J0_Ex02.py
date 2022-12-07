
num = int (input ("Enter any number to test whether it is odd or even:"))

if (int(num) == num):

    print ("The number is an integer")

if (num == 0):

    print ("The number is zero")

if (num % 2) == 0:

    print ("The number is even")

else:
    print ("The provided number is odd")

# ---------------- OR ----------------------------
import sys

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

#if (len(sys.argv)>1):
print(len(sys.argv))

#mport sys

#print(f"Name of the script      : {sys.argv[0] =}")
#print(f"Arguments of the script : {sys.argv[1:] =}")

# python J1_Ex02.py arg1 arg2 arg3

# 
