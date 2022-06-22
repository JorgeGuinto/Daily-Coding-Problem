"Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded"
"For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'."
"You can assume that the messages are decodable. For example, '001' is not allowed."

#Con O(exponencial)
def numDecodings(s):
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0
    return numDecodingsHelper(s, len(s))
 
 
def numDecodingsHelper(s, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] > "0":
        count = numDecodingsHelper(s, n-1)
    if (s[n - 2] == '1' or (s[n - 2] == '2'and s[n - 1] < '7')):
        count += numDecodingsHelper(s, n - 2)
    return count

#Con O(n)
def myNumDecoding(s):
    n = len(s)
    count = [0] * (n)
    count [n-1] = 1
    found0 = 0
    if s[n-1] == '0':
        count[n-2]  = 1
        n = n-1
        found0 = 1
    prevDouble = False

    for i in range(n-1,0,-1):
        
        if s[i-1] == '0':
            found0 = 2
            for j in range(0,n-1):
                count[j] = count[j+1]
            continue
        
        if found0 > 0:
            count[i-1] = count[i]
            found0 += -1
            continue
        
        if s[i-1] == '1' or (s[i-1] == '2' and s[i] < '7'):
            if prevDouble:
                if len(s)-i == 2:
                    count[i-1] =  int((2)*(count[i+1])) + 1
                else:
                    count[i-1] =  int((2)*(count[i+1])) + count[i+2]
            else:
                count[i-1] = 2*(count[i])
            prevDouble = True

        elif s[i-1] > '0':
            count[i-1] = count[i]
            prevDouble = False

    return count[0]

 #A Dynamic Programming based Python3
# implementation to count decodings
 
# A Dynamic Programming based function
# to count decodings
def countDecodingDP(digits, n):
 
    count = [0] * (n + 1); # A table to store
                           # results of subproblems
    count[0] = 1;
    count[1] = 1;
 
    for i in range(2, n + 1):
 
        count[i] = 0;
 
        # If the last digit is not 0, then last
        # digit must add to the number of words
        if (digits[i - 1] > '0'):
            count[i] = count[i - 1];
 
        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if (digits[i - 2] == '1' or
           (digits[i - 2] == '2' and
            digits[i - 1] < '7') ):
            count[i] += count[i - 2];
 
    return count[n];
 
# Driver Code
digits = "1101111107210";
n = len(digits);
print("Count is", countDecodingDP(digits, n)); # Otra manera que encontré en internet

myStr = "1101111107210"
print(numDecodings(myStr)) #Este lo vi en internet
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
print(myNumDecoding(myStr)) #Este es el código que hice por mi cuenta