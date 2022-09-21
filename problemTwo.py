def find3Numbers(A, arr_size, sum):
    for i in range( 0, arr_size-2):
        for j in range(i + 1, arr_size-1):
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                     return (A[i], ", ", A[j], ", ", A[k])
                          


A = list(map(int, input().split()))
sum = 22
arr_size = len(A)
triplet = find3Numbers(A, arr_size, sum)


if sum(triplet) == 0:
    print(triplet)