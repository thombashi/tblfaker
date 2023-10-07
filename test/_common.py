import sys


def print_test_result(expected, actual, error=None):
    print(f"[expected]\n{expected}\n")
    print(f"[actual]\n{actual}\n")

    if error:
        print(error, file=sys.stderr)
