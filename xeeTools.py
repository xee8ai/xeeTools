#!/usr/bin/env python3

"""A module holding some functions frequently used by me."""

from pprint import pprint
import inspect
import sys
import traceback


################################################################################
def dd(*data):
    """Helper for fast debug view of each kind of data.
    Inspirated by Laravel's dd() function."""

    print()
    print(100 * "=")
    # get the caller's metadata: class and method
    print()
    print("Output of dd(), ", end="")

    # check if in class context
    stack = inspect.stack()
    if "self" in stack[1][0].f_locals:
        the_class = str(stack[1][0].f_locals["self"].__class__)
        the_class = the_class.split("'")[1]
        the_method = stack[1][0].f_code.co_name
        print("called by:")
        print(f"{str(the_class)}.{the_method}()")
    else:
        print("called from")

    # get the caller's metadata: file and line
    tb = traceback.extract_stack(limit=2)
    print(f"{tb[0][0]}, line {tb[0][1]}")
    print()

    # pretty print all given data
    for i, d in enumerate(data):
        print()
        print(80 * "=")
        print()
        the_type = f"Argument {i} is of type {type(d)}"
        print(the_type)
        print(len(the_type) * "-")
        pprint(d)
        print()

    print()
    print(100 * "=")
    print()
    print()

    # Exit with error to indicate non standard execution
    sys.exit(1)


################################################################################
def ex_to_str(ex):
    """Converts an exception to a human readable string containing relevant informations.
    Use e.g. to create meaningful log entries."""

    # get type and message of risen exception
    ex_type = f"{type(ex).__name__}"
    ex_args = ', '.join(ex.args)

    # get the command where the exception has been raised
    tb = traceback.extract_tb(sys.exc_info()[2], limit=2)
    ex_cmd = tb[0][3]
    ex_file = tb[0][0]
    ex_line = tb[0][1]

    # the string (one liner) to return
    nice_ex = f"{ex_type} ({ex_args}) raised executing '{ex_cmd}' in {ex_file}, line {ex_line}"

    return nice_ex


################################################################################
def seconds_to_timestring(seconds):
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = round(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


################################################################################
################################################################################
################################################################################
if __name__ == "__main__":

    # test the exception converter
    try:
        a = 3 - 3
        b = 1 / a
        c = a + b
    except Exception as ex:
        print(ex_to_str(ex))
        # raise

    # test dd last because it ends the script :-)
    l = ["foo", "bar", 42]
    dd("test", l)
