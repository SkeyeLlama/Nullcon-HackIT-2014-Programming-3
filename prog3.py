'''
Created on Jan 25, 2014

SkeyeLlama
Nullcon 2014 HackIT
Programming 3
a^b^c^d^e % p
'''
import telnetlib
import re
#import math
from urllib2 import Request, urlopen, URLError

'''
def effExp(a,b,m):
    c =1
    e = 0
    while e < b:
        e += 1
        c = (c * a) % m
        #print str(c)
   ''     
   # raw_input()
    return int(c)
        
    
     

def modExp(a, b, m) :
    """Computes a to the power b, modulo m, using binary exponentiation
    """
    a %= m
    ret = None
    
    if b == 0 :
        ret = 1
    elif b%2 :
        ret = a * modExp(a,b-1,m)
    else :
        ret = modExp(a,b//2,m)
        ret *= ret
        
    return ret%m
'''
print "Connecting~~~"
session = telnetlib.Telnet('23.23.190.204', 2000, 120)
while True:
    readterm = session.read_until('?', 120)
    print readterm
    parse = readterm.rpartition('\n')[-1]
    print parse
    numbers = re.findall(r'[0-9]+', parse)
    print numbers
   # print "Enter A,B,C,D,E,P:"
    A = int(numbers[2])
    B = int(numbers[3])
    C = int(numbers[4])
    D = int(numbers[5])
    E = int(numbers[6])
    P = int(numbers[7])
    #step1 = (D**E) % P 
    #print str(step1)
    #step2 = (C**step1) % P
    #print str(step2)
    #step3 = (B**step2) % P
    #print str(step3)
    #Key = (A**step3) % P
   #query = ('%28'+ str(A)+'+%5E+%28'+ str(B)+'+%5E+%28'+ str(C)+'+%5E+%28'+ str(D)+'+%5E+'+ str(E)+'%29%29%29%29+mod+'+ str(P))
    #NEED APP ID FROM WOLFRAM ALPHA FOR QUERY
    query = ('http://api.wolframalpha.com/v2/query?input=%28'+ str(A)+'+%5E+%28'+ str(B)+'+%5E+%28'+ str(C)+'+%5E+%28'+ str(D)+'+%5E+'+ str(E)+'%29%29%29%29+mod+'+ str(P)+'&appid=XXXXXX-XXXXXXXXXX&format=plaintext&includepodid=Result')
    print query
    try:
        response = urlopen(query)
        result = response.read()
    except URLError, e:
        print 'Got an error code:', e
    parse2 = result.rpartition('\n')[-3]
    print parse2
    numr = re.findall(r'[0-9]+', parse2)
    print numr[len(numr) -1]
    session.write(str(numr[len(numr)-1]) + '\n')
    #session.write(str(Key) + '\n')
