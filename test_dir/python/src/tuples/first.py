from test_dir.python.pypp.ownership import Valu
from test_dir.python.pypp.tuple_get import tg


def _inline_tuple(tup: Valu(tuple[float, str])):
    print(tup)


def _get_tup() -> tuple[int, float]:
    return 1, 2.0


def _argument_unpacking(a: int, b: float):
    print(a, b)


def _arg_unpacking_fail(a: int, b: int, c: int):
    print(a, b, c)


def tuples_fn():
    print("TUPLE RESULTS:")
    a: tuple[int, float, str] = (1, 1.2, "a")
    # count
    print(str(a.count(2)))
    # index
    print(str(a.index(1.2)))
    # print(a.index(1.1))  # Throws error
    # access
    b: int = tg(a, 0)
    print(str(b))
    # comparisons
    print(str((1, 2) == (1, 2)))
    print(str((1, 2) != (1, 2)))
    print(str((1, 2) < (1, 2)))
    print(str((1, 2) <= (1, 2)))
    print(str((1, 2) > (1, 2)))
    print(str((1, 2) >= (1, 2)))
    # printing
    print((1, 2))
    print((1, 2, "a"))
    # length
    print(str(len((1, 2))))
    # inline passing
    _inline_tuple((1.2, "z"))
    # unpacking elements
    x, y, z = a
    print(x, y, z)
    # unpacking elements from a function
    u, v = _get_tup()
    print(u, v)
    # argument unpacking
    _argument_unpacking(*_get_tup())
    # argument unpacking only works if it is the only argument to the call.
    # arg_unpacking_fail(1, *get_tup())

    # variables that are passed to tuples are moved
    c: list[int] = [1, 2, 3]
    d: tuple[int, list[int]] = (1, c)
    print(d)
    print(
        "below will be [1, 2, 3] for Python, but [] for C++ because the list was moved:"
    )
    print(c)
