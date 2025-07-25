from first import return_something
from imports_test.first import imports_test_fn
from imports_test.second import imports_test_fn2
from second import return_friend
from third import using_inline_string
from fourth import string_as_argument
from if_elif_else.if_elif_else import if_elif_else_fn
from lists.lists import list_fn
from strings.first import string_ops
from numbers_test.first import number_ops
from lists.as_arg import list_as_arg, list_as_mutable_arg
from dicts.first import dict_fn
from tuples.first import tuples_fn
from sets.first import set_fn
from loops.for_ import for_loop_fn
from loops.while_ import while_loop_fn
from excpetions.throw_ import throw_fn
from dicts.exceptions import dict_exceptions_fn
from lists.exceptions import list_exceptions_fn
from sets.exceptions import set_exceptions_fn
from strings.exceptions import string_exceptions_fn
from tuples.exceptions import tuple_exceptions_fn
from file_io.first import file_io_fn
from strings.escape_characters import string_esc_chars_fn
from strings.f_strings import f_strings_fn
from ranges.first import ranges_fn
from slices.first import slices_fn
from inconsistent_behviour.editing_a_reference import editing_a_reference_fn
from loops.enumerate_ import enumerate_fn
from printing.first import printing_fn
from loops.zip_ import zip_fn
from loops.reversed_ import reversed_fn
from lists.comprehensions import list_comprehension_fn
from sets.comprehensions import set_comprehension_fn
from dicts.comprehensions import dict_comprehension_fn
from excpetions.assert_ import assert_fn
from type_aliases import type_aliases_fn
from yields.first import yield_fn
from math_library.first import math_library_fn
from time_library.first import time_library_fn
from sets.of_tuples import set_of_tuples_fn
from ref_vars import ref_vars_fn
from dataclasses_test.first import dataclass_fn
from dataclasses_test.with_methods import dataclass_with_methods_fn
from classes.first import classes_fn
from classes.inheritance import class_inheritance_fn
from interfaces.first import interfaces_fn
from operations import operations_fn
from fn_as_vars.first import fn_as_vars_fn
from default_dict.first import default_dict_fn
from pypp_union.first import pypp_union_fn
from constants import constant_fn
from number_types import number_types_fn

if __name__ == "__main__":
    print(return_something(1, 9))
    print(return_friend())
    print(using_inline_string())
    print(string_as_argument("hello"))
    print(if_elif_else_fn(6, 6))
    number_ops()
    my_list: list[int] = [1, 2, 3, 4]
    list_as_arg(my_list)
    list_as_mutable_arg(my_list)
    print(my_list)
    str_list: list[str] = ["ab", "cd"]
    print(str_list)
    string_ops()
    set_fn()
    for_loop_fn()
    while_loop_fn()
    throw_fn()
    dict_exceptions_fn()
    list_exceptions_fn()
    set_exceptions_fn()
    string_exceptions_fn()
    tuple_exceptions_fn()
    string_esc_chars_fn()
    f_strings_fn()
    ranges_fn()
    slices_fn()
    editing_a_reference_fn()
    enumerate_fn()
    printing_fn()
    zip_fn()
    reversed_fn()
    file_io_fn()
    set_comprehension_fn()
    dict_comprehension_fn()
    list_comprehension_fn()
    assert_fn()
    type_aliases_fn()
    yield_fn()
    math_library_fn()
    time_library_fn()
    tuples_fn()
    set_of_tuples_fn()
    ref_vars_fn()
    dict_fn()
    list_fn()
    dataclass_fn()
    dataclass_with_methods_fn()
    classes_fn()
    class_inheritance_fn()
    interfaces_fn()
    operations_fn()
    fn_as_vars_fn()
    default_dict_fn()
    pypp_union_fn()
    constant_fn()
    imports_test_fn()
    imports_test_fn2()
    number_types_fn()
