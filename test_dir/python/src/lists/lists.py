from test_dir.python.pypp.lists import list_reserve
from test_dir.python.pypp.ownership import mov, Valu, Ref


def _test_fn(arg1: Valu(list[str])):
    print(arg1)


def list_fn():
    print("LIST RESULTS:")
    # Declaration
    a: list[int] = [1, 2, 3, 4, 5]
    print(a)
    # Assigning element
    a[0] = 10
    print(a)
    # Append
    a.append(11)
    print(a)
    # Accessing - indices
    print(str(a[-1]))
    # Showing reassigning a reference behaviour
    # BIG NOTE: you shouldn't do this in pypp. This results in inconsistent behavior
    #  between the Python and C++ executions. In python when you reassign the original
    #  stays the same without modification, and in C++ when you reassign the original
    #  changes as well.
    b: int = a[-1]
    print(str(b))
    b = 20
    print(str(b))
    print(a)
    # Len
    print(str(len(a)))
    # reverse
    a.reverse()
    print(a)
    # count
    print(str(a.count(2)))
    # index
    print(str(a.index(2)))
    # remove
    a.remove(2)
    print(a)
    # insert
    a.insert(4, 2)
    print(a)
    # insert with mov
    ins_val: int = 2
    a.insert(4, mov(ins_val))
    print(a)
    # pop
    popped_val: int = a.pop()
    print(str(popped_val))
    print(a)
    popped_val2: int = a.pop(1)
    print(str(popped_val2))
    print(a)
    # clear
    a.clear()
    print(a)
    # lexicographical comparisons
    print(str([1, 2] == [1, 2]))
    print(str([1, 2] < [1, 2]))
    print(str([1, 2] <= [1, 2]))
    print(str([1, 2] > [1, 2]))
    print(str([1, 2] >= [1, 2]))
    print(str([1, 2] != [1, 2]))
    # concatenation
    c: list[int] = [1, 2] + [3, 4]
    print(c)
    c += [5, 6]
    print(c)
    # repetition
    d: list[int] = c * 3
    print(d)
    c *= 3
    print(c)
    # slicing
    print(c[1:4])
    print(c[1 : len(c) - 1 : 2])
    print(c[1::2])
    print(c[1:])
    print(c[:4])
    print(c[::2])
    print(c[:])
    print(c[len(c) - 2 : 5])
    print(c[len(c) - 4 : len(c) - 1])
    print(c[5:1:-1])
    # slice setting. Note: This is not supported in the transpiled C++ right now, and
    #  no error is thrown either!
    # c[1:4] = [-2, -2, -2, -2]
    # print(c)
    # list of strings
    e: list[str] = ["a", "b"]
    print(e)
    # initialize empty
    f: list[int] = []
    print(f)
    # reserve
    list_reserve(e, 10)
    # modifying references
    g: list[list[int]] = [[1, 2], [3, 4]]
    g_0: Ref(list[int]) = g[0]
    g_0.append(99)
    print(g)
    g[1].append(98)
    print(g)
    # test passing a list inline
    _test_fn(["1", "2"])
