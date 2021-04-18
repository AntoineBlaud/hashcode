
def minPartition(S):
 
    # Find the sum of all elements
    total = sum(S)
 
    # Create a boolean table to store solutions to subproblems
    T = [[False]*(total + 1) for _ in range(len(S) + 1)]
 
    # Fill the lookup table in a bottom-up manner
    for i in range(len(S) + 1):
 
        # elements with zero-sum are always true
        T[i][0] = True
 
        j = 1
        while i > 0 and j <= total:
 
            # exclude the i'th element
            T[i][j] = T[i - 1][j]
 
            # include the i'th element
            if S[i - 1] <= j:
                T[i][j] |= T[i - 1][j - S[i - 1]]
 
            j = j + 1
 
    # Find the maximum value of `j` between 0 and `sum/2` for which the
    # last row is true
    j = total // 2
    while j >= 0 and not T[len(S)][j]:
        j = j - 1
 
    return total - 2*j
 
 
if __name__ == '__main__':
 
    # Input: a set of items
    S = [10, 20, 15, 5, 25]
 
    print("The minimum difference is", minPartition(S))