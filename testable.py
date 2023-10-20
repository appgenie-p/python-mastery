import os


def get_var():
    return var if (var := os.getenv("PYTHONPATH")) else "NONE"


if __name__ == "__main__":
    print("\n", "PYTHONPATH=", get_var(), sep="")
