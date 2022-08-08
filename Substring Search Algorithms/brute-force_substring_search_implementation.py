#Brute-Force Substring Search Implementation

def naive_search(pattern, text):

    m = len(pattern)
    n = len(text)

    for i in range(n-m+1):
        j = 0

        while j < m:

            if text[i+j] != pattern[j]:
                break

            j = j + 1

        if j == m:
            print('Found a match at index %s' % i)


# Testing
if __name__ == '__main__':
    naive_search('abcd','abcdefabcabcd')
