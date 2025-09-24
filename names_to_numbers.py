# бригада 4

names = ["Sukhotierin Yehor", "Spasyba Serhii", "Slynko Nazar"]

def name_to_int(name: str) -> list[int]:
    return [ord(c) for c in name]

def name_to_binary(name: str) -> list[str]:
    return [f"{ord(c):08b}" for c in name]

def name_to_hex(name: str) -> list[str]:
    return [f"{hex(ord(c))}" for c in name]

names_int = [name_to_int(i) for i in names]

names_binary = [name_to_binary(i) for i in names]

names_hex = [name_to_hex(i) for i in names]

names_num_pairs = {}
for i, name in enumerate(names):
    names_num_pairs[name] = {
        "int": names_int[i],
        "binary": names_binary[i],
        "hex": names_hex[i],
    }

for i in names_num_pairs:
    print(i)
    for pos, c in enumerate(i):
        print(f"{c} -> {names_num_pairs[i]["int"][pos]} -> {names_num_pairs[i]["hex"][pos]} -> {names_num_pairs[i]["binary"][pos]}")

    print("\n\n")