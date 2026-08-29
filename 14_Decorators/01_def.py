# Python Decorators — Definition

# A decorator in Python is a function that takes another function as input, adds or changes its behavior, and returns the modified function without changing the original function’s code.

# Important things to remember

# Decorators use functions as arguments.
# A decorator wraps another function.
# They follow the DRY principle — write common functionality once and reuse it.
# Decorators are based on first-class functions.
# Decorators commonly use nested functions.
# The @decorator_name syntax is called decorator syntax or syntactic sugar.
# @decorator above a function means the function is automatically passed to that decorator.
# A decorator can execute code before and/or after the original function.
# A decorator can modify the arguments, return value, or behavior of a function.
# Multiple decorators can be applied to the same function.
# Decorators can be used with *args and **kwargs to support functions with different arguments.
# functools.wraps is commonly used inside decorators to preserve the original function’s name, docstring, and metadata.
# Common uses
# Logging
# Authentication/authorization
# Timing functions
# Access control
# Caching
# Validation
# Error handling
# Performance monitoring
# One-line interview definition

# A decorator is a Python function that modifies or extends the behavior of another function or class without permanently changing its source code.