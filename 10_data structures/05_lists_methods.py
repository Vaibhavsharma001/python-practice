                                  # append()
# Adds one element to the end.

a = [10, 20, 30]
a.append(40)
print(a)


                                  # extend()
# Adds multiple elements from another list.

b = [10, 20]
b.extend([30, 40])
print(b)


                                # insert()
# Inserts an item at a given index.

c = [10, 20, 30]
c.insert(1, 15)
print(c)


                                # remove()
# Removes the first occurrence of a value.

d = [10, 20, 30]
d.remove(20)
print(d)

                                        # pop()
# Removes an item by index.
e = [10, 20, 30]
e.pop()
print(e)

                                         # clear()
# Removes all items.
f = [10, 20, 30]
f.clear()
print(f)

                                           # index()
# Returns the index of an item.
g = [10, 20, 30]
print(g.index(20))


                                            # count()
# Counts how many times an item appears.
h = [10, 20, 10, 30, 10]
print(h.count(10))


                                              # sort()
# Sorts the list in ascending order.
i = [40, 10, 30, 20]
i.sort()
print(i)

#desending order
i.sort(reverse=True)
print(i)

                                                   # reverse()
# Reverses the order of the list.
j = [10, 20, 30]
j.reverse()
print(j)


                                                     # copy()
# Creates a copy of the list.
k = [10, 20, 30]
new_list = k.copy()
print(new_list)