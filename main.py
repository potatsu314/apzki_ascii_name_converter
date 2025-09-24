print("Input names separated by spaces")

names = input("> ").strip().split(" ")

def name_to_int(name: str) -> list[int]:
    return [ord(c) for c in name]

def name_to_binary(name: str) -> list[str]:
    return [f"{ord(c):b}" for c in name]

def name_to_hex(name: str) -> list[str]:
    return [f"{hex(ord(c))}" for c in name]

names_int = [name_to_int(i) for i in names]

names_binary = [name_to_binary(i) for i in names]

names_hex = [name_to_hex(i) for i in names]

print(names_int)
print(names_binary)
print(names_hex)