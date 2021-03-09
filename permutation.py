""" You are given one integer n (n>1).
Recall that a permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. For 
example, [2,3,1,5,4] is a permutation of length 5, but [1,2,2] is not a permutation (2 appears twice in the array) and
[1,3,4] is also not a permutation (n=3 but there is 4 in the array).
Your task is to find a permutation p of length n that there is no index i (1≤i≤n) such that pi=i (so, for all i from 1
to n the condition pi≠i should be satisfied).
You have to answer t independent test cases.
If there are several answers, you can print any. It can be proven that the answer exists for each n>1."""
import random

t = int(input('number of test cases: '))
permutation = []
n_array = []


def n_input(tests_cases):
    for i in range(tests_cases):
        n = int(input('n: '))
        n_array.append(n)
    return n_array


def make_permutation(array_n):
    for n in array_n:
        for i in range(n):
            permutation.append(i+1)
        random.shuffle(permutation)
        print(*permutation, sep=' ')
        permutation.clear()


def play(test_cases):
    array_n = n_input(test_cases)
    make_permutation(array_n)


play(t)

