from __future__ import annotations

from typing import TYPE_CHECKING, Callable

__all__ = ['normalize_parameter']

if TYPE_CHECKING:
    from .keyword_processor import KeywordProcessor


def normalize_parameter(*params: str) -> Callable:
    """
    Instead of doing this at the beginning of each function:
    if not self.case_sensitive:
        word = word.lower()

    We can just decorate the function with: `@normalize_parameter('parameter_name')`

    :param params: parameter names
    """
    def decorator(func):
        def wrapper(*args, **kwargs):

            kwargs.update(dict(zip(func.__code__.co_varnames, args)))  # convert all args to kwargs
            self: KeywordProcessor = kwargs['self']
            if not self._case_sensitive:
                for p in params:
                    kwargs[p] = kwargs[p].lower()

            return func(**kwargs)
        return wrapper
    return decorator