def union(a, b):
    return [i for i in a if i not in b] + b

print "union([1, 2, 3, 7], [7, 2, 3, 4]):"
print union([1, 2, 3, 7], [7, 2, 3, 4])

def intersection(a, b):
    return [ i for i in a if i in b]

print "intersection([1, 2, 3, 7], [7, 2, 3, 4]):"
print intersection([1, 2, 3, 7], [7, 2, 3, 4])

def setdifference(a, b):
    return [ i for i in a if i not in b]

print "setdifference([1, 9, 2, 3, 7], [7, 3, 4]):"
print setdifference([1, 9, 2, 3, 7], [7, 3, 4])

def symmetricdiff(a, b):
    return [i for i in a if i not in b] + [i for i in b if i not in a] 

print "symmetricdiff([1, 2, 9, 3, 7], [7, 2, 3, 4]):"
print symmetricdiff([1, 2, 9, 3, 7], [7, 2, 3, 4])

def cartesian(a, b):
    return [[i,x] for i in a for x in b]   

print "cartesian([1, 3, 7], [7, 2, 3]):"
print cartesian([1, 3, 7], [7, 2, 3])

