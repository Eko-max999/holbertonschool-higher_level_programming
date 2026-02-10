#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Modulun içindəki bütün adları list şəklində alırıq
    names = dir(hidden_4)

    # Adları əlifba sırası ilə düzürük və __ ilə başlamayanları seçirik
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
