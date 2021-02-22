# Problem01:
# Given an array, X, N of integers, calculate and print the respective mean, median, and mode on separate lines
# If your array contains more than one modal value, choose the numerically smallest one
# Constraints : 10 <= N <=2500
# Constraints : 0 < X [i] < 10^5, that means each element will consist of 5 digits
# The code starts here:

N = int (input())
mean1 = 0
sum1 = 0
sum2 = 0
i = 0
X = list (map(int,input().strip().split())) [:N]
def Mean ():
    while i < N :
        sum2 = sum1 + X [i]
        sum1 = sum2
        mean1 = sum1/N
print (mean1)

Mean ()