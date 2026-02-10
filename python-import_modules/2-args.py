#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # sys.argv-nin uzunluğunu tapırıq (proqramın adını çıxırıq)
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Argumentləri tək-tək dövrlə (loop) çap edirik
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
