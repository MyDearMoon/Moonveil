def _feistel_round(left, right, round_key):
    f = (((right * 0x9E3779B9) << 5) ^ (right >> 3)) + round_key
    new_right = (left ^ f) & 0xFFFFFFFF
    return right, new_right

def _block_mix(data):
    state = 0x50485942
    res = []
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        val = 0
        for b in chunk:
            val = (val << 8) | b
        l = (val >> 16) & 0xFFFF
        r = val & 0xFFFF
        for rnd, k in enumerate([0x1337, 0x5A5A, 0xC001, 0xCAFE]):
            l, r = _feistel_round(l, r, k + i * 17)
        combined = ((l << 16) | r) & 0xFFFFFFFF
        state = (((state ^ combined) * 0x7FED1429) + 0x1337BEEF + ((state >> 11) & 0x1FFFF)) & 0xFFFFFFFF
        res.append(state)
    return res

def _verify(flag):
    if not flag.startswith("CTF{") or not flag.endswith("}"):
        return False

    body = flag[4:-1].encode()
    if len(body) != 36:
        return False

    computed = _block_mix(body)
    expected = [181366726, 1417008666, 301693207, 3394238215, 1635253078, 1507017450, 2029189337, 2101878377, 177291373]

    score = 0
    for a, b in zip(computed, expected):
        score ^= (a ^ b)

    return score == 0

def main():
    flag = input("Enter the flag: ").strip()
    if _verify(flag):
        print("Correct!")
    else:
        print("Incorrect!")

if __name__ == "__main__":
    main()
