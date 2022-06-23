"Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters."
"For example, given s = 'abcba' and k = 2, the longest substring with k distinct characters is 'bcb'."

def longestSubstring(s, k):
    longestSubstring = ''

    for i in range(len(s)):
        chars = [s[i]]*k
        count = 1
        tempSubstring = chars[0]

        for j in range(i+1, len(s), 1):
            if (s[j] in chars):
                tempSubstring = tempSubstring + s[j]
            elif count < k:
                chars[count] = s[j]
                count = count + 1
                tempSubstring = tempSubstring + s[j]
            else:
                break
            
        if len(tempSubstring) > len(longestSubstring):
            longestSubstring = tempSubstring

    return longestSubstring

s = "abcbcbcbcaba"
k = 2
print(longestSubstring(s, k))
