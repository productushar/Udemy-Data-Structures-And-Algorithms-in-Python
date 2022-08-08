#Z Substring Search Implementation

class ZAlgorithm:

    def __init__(self, pattern, text):
        
        self.pattern = pattern
        self.text = text
        # Concatenating the pattern and text
        self.S = pattern + text
        self.Z = [0 for _ in range(len(self.S))]

    def construct_z_table(self):

        self.Z[0] = len(self.S)
        # First and last items in the Z box
        left = 0
        right = 0

        # Considering all the letters of the S string
        for k in range(1, len(self.S)):

            #Case 1: Not within a Z box (naive approach)
            if k > right:
                n = 0

                while n + k < len(self.S) and self.S[n] == self.S[n+k]:
                    n = n + 1

                self.Z[k] = n

                if n > 0:
                    left = k
                    right = k

            else:
                p = k - left

                # Case 2: When we can copy the values of Z
                if self.Z[p] < right - k + 1:
                    self.Z[k] = self.Z[p]

                # Case 3: When we cannot copy the values
                else:
                    i = right + 1

                    while i < len(self.S) and self.S[i] == self.S[i - k]:
                        i = i + 1

                    self.Z[k] = i - k
                    left = k
                    right = i - 1

    def search(self):
        self.construct_z_table()
        print(self.Z)

        for i in range(1,len(self.Z)):
            if self.Z[i] >= len(self.pattern):
                print("Match found at index %s" % (i - len(self.pattern)))


# Testing
if __name__ == '__main__':
    algorithm = ZAlgorithm('aabza','abzcaabzaabza')
    algorithm.search()
