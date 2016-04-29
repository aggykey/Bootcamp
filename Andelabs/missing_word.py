def find_missing(A, B):
    if A == B:
        return 0

    if A != B:
        for i in A:
            for j in B:
                a = []
                if i not in B:
                    a.append(i)
                if j not in A:
                    a.append(j)
    return a
print find_missing([1, 2, 3], [1, 2, 3, 4])