import ast

from src.handle_stmt.h_class_def.for_class.for_class import handle_class_def_for_class
from src.handle_stmt.h_class_def.for_configclass.for_configclass import (
    handle_class_def_for_configclass,
)
from src.handle_stmt.h_class_def.for_dataclasses.for_dataclasses import (
    handle_class_def_for_dataclass,
)
from src.handle_stmt.h_class_def.for_interface.for_interface import (
    handle_class_def_for_interface,
)
from src.util.ret_imports import RetImports


def handle_class_def(
    node: ast.ClassDef,
    ret_imports: RetImports,
    ret_h_file: list[str],
    handle_stmt,
    handle_expr,
) -> str:
    _do_common_assertions(node)
    if len(node.decorator_list) == 1:
        decorator_name = _get_decorator_name(node)
        if decorator_name == "dataclass":
            is_frozen: bool = _do_dataclass_assertions(node)
            return handle_class_def_for_dataclass(
                node, ret_imports, ret_h_file, handle_stmt, handle_expr, is_frozen
            )
        else:  # configclass
            dtype: ast.expr = _do_configclass_assertions(node)
            return handle_class_def_for_configclass(
                node, ret_imports, ret_h_file, handle_expr, handle_stmt, dtype
            )

    if _is_interface_def(node):
        _do_interface_assertions(node)
        # This is a struct, which is a special case of a class.
        # Note: structs are not supported yet.
        return handle_class_def_for_interface(
            node, ret_imports, ret_h_file, handle_expr
        )
    return handle_class_def_for_class(
        node, ret_imports, ret_h_file, handle_stmt, handle_expr
    )


def _is_interface_def(node: ast.ClassDef) -> bool:
    return (
        len(node.bases) == 1
        and isinstance(node.bases[0], ast.Name)
        and node.bases[0].id == "ABC"
    )


def _do_common_assertions(node: ast.ClassDef) -> None:
    assert len(node.type_params) == 0, "type parameters for classes are not supported"
    assert len(node.keywords) == 0, "keywords for classes are not supported"


def _get_decorator_name(node: ast.ClassDef) -> str:
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        assert isinstance(decorator.func, ast.Name), (
            "only @dataclass and @configclass decorators supported for classes"
        )
        if decorator.func.id not in {"dataclass", "configclass"}:
            raise Exception(
                "only @dataclass and @configclass decorators supported for classes"
            )
        assert len(decorator.args) == 0, (
            "only keyword args for class decorators are supported"
        )
        return decorator.func.id
    else:
        assert isinstance(decorator, ast.Name), "something wrong with class decorator"
        if decorator.id not in {"dataclass", "configclass"}:
            raise Exception(
                "only @dataclass and @configclass decorators supported for classes"
            )
        return decorator.id


def _do_configclass_assertions(node: ast.ClassDef) -> ast.expr | None:
    assert len(node.bases) == 0, "inheritance for configclass is not supported"
    decorator = node.decorator_list[0]
    if isinstance(decorator, ast.Call):
        keywords: list[ast.keyword] = decorator.keywords
        error_str: str = (
            "only 'dtype' keyword arg for configclass decorator is supported"
        )
        assert len(keywords) == 1, error_str
        assert keywords[0].arg == "dtype", error_str
        return keywords[0].value
    return None


def _do_dataclass_assertions(node: ast.ClassDef) -> bool:
    assert len(node.bases) == 0, "inheritance for dataclass is not supported"
    decorator = node.decorator_list[0]
    is_frozen: bool = False
    if isinstance(decorator, ast.Call):
        is_frozen = _check_dataclass_keywords(decorator.keywords)
    return is_frozen


def _check_dataclass_keywords(nodes: list[ast.keyword]) -> bool:
    assert len(nodes) <= 2, (
        "only 'frozen' and 'slots' keyword args for dataclass decorator are supported"
    )
    frozen: bool = False
    for node in nodes:
        if node.arg == "frozen":
            assert isinstance(node.value, ast.Constant), "frozen must be a boolean"
            assert isinstance(node.value.value, bool), "frozen must be a boolean"
            frozen = node.value.value
        elif node.arg != "slots":
            # slots is just ignored.
            raise NotImplementedError(f"unsupported dataclass keyword: {node.arg}")
    return frozen


def _do_interface_assertions(node: ast.ClassDef) -> None:
    # assert that only methods/functions are defined in node.body and that each of them
    # has an 'abstractmethod' decorator
    for item in node.body:
        assert isinstance(item, ast.FunctionDef), (
            f"only methods are supported in interface definitions, got {type(item).__name__}"
        )
        assert (
            len(item.decorator_list) == 1
            and isinstance(item.decorator_list[0], ast.Name)
            and item.decorator_list[0].id == "abstractmethod"
        ), (
            f"method {item.name} in interface {node.name} must be decorated only with @abstractmethod"
        )
