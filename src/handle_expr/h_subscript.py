import ast

from src.d_types import CppInclude
from src.mapping.subscript_value import lookup_cpp_subscript_value_type
from src.util.inner_strings import calc_inside_rd


def handle_subscript(
    node: ast.Subscript, ret_imports: set[CppInclude], handle_expr
) -> str:
    value_cpp_str = handle_expr(node.value, ret_imports)
    slice_cpp_str: str = handle_expr(node.slice, ret_imports)
    if slice_cpp_str.startswith("PyTup(") and slice_cpp_str.endswith(")"):
        slice_cpp_str = calc_inside_rd(slice_cpp_str)
    v1, v2 = lookup_cpp_subscript_value_type(value_cpp_str)
    return v1 + slice_cpp_str + v2
