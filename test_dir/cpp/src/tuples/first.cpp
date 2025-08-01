#include "tuples\first.h"
#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <any>

void _inline_tuple(PyTup<double, PyStr> tup) { print(tup); }

PyTup<int, double> _get_tup() { return PyTup(1, 2.0); }

void _argument_unpacking(int a, double b) { print(a, b); }

void _arg_unpacking_fail(int a, int b, int c) { print(a, b, c); }

void tuples_fn() {
    print(PyStr("TUPLE RESULTS:"));
    PyTup<int, double, PyStr> a = PyTup(1, 1.2, PyStr("a"));
    print(to_pystr(a.count(2)));
    print(to_pystr(a.index(1.2)));
    int b = a.get<0>();
    print(to_pystr(b));
    print(to_pystr(PyTup(1, 2) == PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) != PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) < PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) <= PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) > PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) >= PyTup(1, 2)));
    print(PyTup(1, 2));
    print(PyTup(1, 2, PyStr("a")));
    print(to_pystr(PyTup(1, 2).len()));
    _inline_tuple(PyTup(1.2, PyStr("z")));
    auto [x, y, z] = a;
    print(x, y, z);
    auto [u, v] = _get_tup();
    print(u, v);
    std::apply(_argument_unpacking, _get_tup().raw());
    PyList<int> c = PyList({1, 2, 3});
    PyTup<int, PyList<int>> d = PyTup(1, std::move(c));
    print(d);
    print(PyStr("below will be [1, 2, 3] for Python, but [] for C++ because "
                "the list was moved:"));
    print(c);
}
