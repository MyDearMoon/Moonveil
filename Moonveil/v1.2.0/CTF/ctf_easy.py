def main():
    flag = input("Enter the flag: ").strip()
    if len(flag) != 32 or not flag.startswith("CTF{") or not flag.endswith("}"):
        print("Incorrect!")
        return

    target = [96, 38, 43, 125, 74, 86, 80, 97, 54, 36, 38, 60, 7, 4, 10, 18, 34, 225, 229, 230, 235, 217, 248, 201, 212, 200, 166]
    inner = flag[4:-1]

    valid = True
    for i, c in enumerate(inner):
        val = (ord(c) ^ (i * 7 + 13)) % 256
        if val != target[i]:
            valid = False
            break

    if valid:
        print("Correct!")
    else:
        print("Incorrect!")

if __name__ == "__main__":
    main()
