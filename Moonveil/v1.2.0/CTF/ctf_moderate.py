import hashlib

def _transform(s):
    out = []
    for i, ch in enumerate(s):
        out.append(((ord(ch) * 65 + i * 31) ^ 0x5C) & 0xFF)
    return bytes(out)

def main():
    flag = input("Enter the flag: ").strip()
    if len(flag) != 32 or not flag.startswith("CTF{") or not flag.endswith("}"):
        print("Incorrect!")
        return

    inner = flag[4:-1]
    transformed = _transform(inner)
    digest = hashlib.sha256(transformed).hexdigest()

    expected = "37113f77d172d2a6e07df9200ff08f6b1a4d5d8334e3d8c4a0e03ae18bd93e95"

    if digest == expected:
        print("Correct!")
    else:
        print("Incorrect!")

if __name__ == "__main__":
    main()
