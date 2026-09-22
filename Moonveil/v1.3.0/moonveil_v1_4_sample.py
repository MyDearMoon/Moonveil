"""
Source program intended to be processed by the Moonveil obfuscator.

This deterministic sample exercises arithmetic, bitwise operations, loops,
branches, function calls, exception handling, nested state, and string/constant
handling without using filesystem, network, or process-control behavior.
"""

VERSION = "1.4.0"
PAYLOAD = (
    "moonveil",
    "lazy",
    "reconstruction",
    "partial",
    "materialization",
    "shadow",
    "state",
)

BASE_SEED = 0x5A17C3
MASK32 = 0xFFFFFFFF


def rotl32(value: int, shift: int) -> int:
    shift &= 31
    value &= MASK32
    return ((value << shift) | (value >> (32 - shift))) & MASK32


def mix32(value: int, salt: int) -> int:
    value &= MASK32
    value ^= salt & MASK32
    value = (value * 0x45D9F3B) & MASK32
    value ^= value >> 16
    value = (value * 0x45D9F3B) & MASK32
    value ^= value >> 16
    return value & MASK32


def make_transformer(seed: int):
    state = mix32(seed, 0x13579BDF)

    def transform(value: int, index: int) -> int:
        nonlocal state
        state = rotl32(state ^ (index * 0x1F1F1F1F), (index % 7) + 1)
        state = mix32(state, 0x2468ACE1 ^ index)
        return (value ^ state ^ rotl32(seed, index % 11)) & MASK32

    return transform


def encode_word(word: str, seed: int, index: int) -> int:
    acc = (seed ^ (index * 0x10203)) & MASK32

    for position, char in enumerate(word):
        code = ord(char)
        acc ^= (code + position * 17) & MASK32
        acc = rotl32(acc, (position % 5) + 3)
        acc = (acc + 0x9E3779B9 + index + position) & MASK32

        if code & 1:
            acc ^= 0xA5A5A5A5
        else:
            acc = (acc + 0x3C6EF372) & MASK32

    return mix32(acc, len(word) ^ (index << 8))


def weighted_checksum(values: list[int]) -> int:
    total = 0

    for index, value in enumerate(values, start=1):
        weighted = (value * (index * 3 + 1)) & MASK32

        if value & 0x8000:
            weighted ^= 0xDEAD
        elif value & 0x100:
            weighted = rotl32(weighted, 5)
        else:
            weighted = (weighted + 0xBEEF) & MASK32

        total ^= weighted
        total = rotl32(total, (index % 9) + 1)

    return total & MASK32


def classify(value: int) -> str:
    remainder = value % 11

    if remainder in (0, 3, 7):
        return "prime-like"
    if remainder in (1, 5, 9):
        return "ascending"
    if remainder in (2, 4, 8):
        return "balanced"
    if remainder == 6:
        return "rotated"
    return "residual"


def guarded_ratio(left: int, right: int) -> int:
    try:
        return (left * 97) // right
    except ZeroDivisionError:
        return 0x404


def build_profile(words: tuple[str, ...], seed: int) -> dict[str, int]:
    transformer = make_transformer(seed)
    encoded = []

    for index, word in enumerate(words):
        raw = encode_word(word, seed ^ (index * 0x55AA), index)
        encoded.append(transformer(raw, index))

    checksum = weighted_checksum(encoded)
    ratio = guarded_ratio(checksum & 0xFFFF, len(words))
    return {
        "checksum": checksum,
        "ratio": ratio,
        "count": len(encoded),
    }


def derive_message(profile: dict[str, int], words: tuple[str, ...]) -> str:
    checksum = profile["checksum"]
    ratio = profile["ratio"]
    count = profile["count"]

    selector = (checksum ^ ratio ^ (count * 0x1234)) % len(words)
    category = classify(checksum)

    parts = [
        VERSION,
        category,
        words[selector],
        f"{checksum:08X}",
        f"{ratio:04X}",
    ]

    fold = 0xC001D00D
    for index, part in enumerate(parts):
        for char in part:
            fold ^= ord(char) + index
            fold = rotl32(fold, 3)
            fold = (fold + 0x7F4A7C15) & MASK32

    if fold & 1:
        suffix = "READY"
    elif fold & 2:
        suffix = "ENTANGLED"
    else:
        suffix = "STABLE"

    return "|".join(parts + [suffix])


def main() -> None:
    profile = build_profile(PAYLOAD, BASE_SEED)
    message = derive_message(profile, PAYLOAD)
    print(message)


if __name__ == "__main__":
    main()
