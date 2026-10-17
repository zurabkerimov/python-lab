def binary(number: int, bits: int) -> str:
    """Convert the absolute value to a zero-padded binary string."""
    if not (bits >= 1):
        raise ValueError("Invalid bit value.")
    if not (abs(number) < 2**bits):
        raise ValueError("Number is out of range.")
    return format(abs(number), f"0{bits}b")


def sign_magnitude(number: int, bits: int) -> str:
    """Convert to binary by sign-magnitude."""
    if not (bits >= 2):
        raise ValueError("Invalid bit value.")
    if not (abs(number) < 2 ** (bits - 1)):
        raise ValueError("Number is out of range.")
    code = binary(number, bits - 1)
    sign = "1" if number < 0 else "0"
    return sign + code


def r_sign_magnitude(code: str) -> int:
    """Convert sign-magnitude to decimal."""
    sign = 1 if code[0] == "0" else -1
    value = int(code[1:], 2)
    return value * sign


def ones_complement(number: int, bits: int) -> str:
    """Convert to binary by one's complement."""
    code = sign_magnitude(abs(number), bits)
    if number >= 0:
        return code
    else:
        return "".join("1" if bit == "0" else "0" for bit in code)


def r_ones_complement(code: str) -> int:
    """Convert one's complement to decimal."""
    if code[0] == "0":
        return int(code, 2)
    else:
        inverted = "".join("1" if bit == "0" else "0" for bit in code)
        return int(inverted, 2) * -1


def twos_complement(number: int, bits: int) -> str:
    """Convert to binary by two's complement."""
    if not (bits >= 2):
        raise ValueError("Invalid bit value.")
    if not (-(2 ** (bits - 1)) <= number <= 2 ** (bits - 1) - 1):
        raise ValueError("Number is out of range.")
    if number >= 0:
        return sign_magnitude(number, bits)
    else:
        return format((1 << bits) + number, f"0{bits}b")


def r_twos_complement(code: str) -> int:
    """Convert two's complement to decimal."""
    if code[0] == "0":
        return int(code, 2)
    else:
        n_value = int(code, 2) - 1
        n_code = format(n_value, f"0{len(code)}b")
        inverted = "".join("1" if bit == "0" else "0" for bit in n_code)
        return int(inverted, 2) * -1


def task_9(n: int) -> None:
    print("=" * 60)
    print("Task 9")
    print("=" * 60)
    print(f"Input number: {n}")
    while True:
        try:
            b = int(input("Enter a bit value: "))
            break
        except ValueError:
            print("Invalid input for Task 9. Please enter integers.")
    print("-" * 30)

    converters = [
        ("Sign-magnitude", sign_magnitude, r_sign_magnitude),
        ("One's complement", ones_complement, r_ones_complement),
        ("Two's complement", twos_complement, r_twos_complement),
    ]

    for name, converter, r_converter in converters:
        try:
            code = converter(n, b)
            restored_number = r_converter(code)
        except ValueError as error:
            print(f"{name}: {error}")
        else:
            print(f"{name}: {code}")
            print(f"Restored signed value: {restored_number}")
            print(f"Check result: {restored_number == n}")
            if restored_number != n:
                print(f"{name}: ERROR: Restored number differs from input.")
        print("-" * 30)


def task_10(n: int) -> None:
    print("=" * 60)
    print("Task 10")
    print("=" * 60)
    print(f"Input number: {n}")
    bits = [4, 8, 16]
    name = "Two's complement"
    for bit in bits:
        minval = -(2 ** (bit - 1))
        maxval = 2 ** (bit - 1) - 1
        print(f"\n--- {bit}-bit signed integer ---")
        print(f"Minimum value: {minval}")
        print(f"Maximum value: {maxval}")
        if minval <= n <= maxval:
            try:
                add_code = twos_complement(n, bit)
                restored_number = r_twos_complement(add_code)
            except ValueError as error:
                print(f"{name}: {error}")
            else:
                print(f"{name}: {add_code}")
                print(f"Restored signed value: {restored_number}")
                print(f"Check result: {restored_number == n}")
                if restored_number != n:
                    print(
                        f"{name}: ERROR: Restored number differs from input."
                    )
        else:
            print(
                f"{name}: ERROR: number is out of range [{minval}, {maxval}]"
            )
            stored_bits = format(n % (2**bit), f"0{bit}b")
            restored_number = r_twos_complement(stored_bits)
            print(f"Stored bits: {stored_bits}")
            print(f"Restored signed value: {restored_number}")


def main() -> None:
    print()
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input for Task 9. Please enter integers.")
    task_9(n)
    print()
    task_10(n)
    print()


if __name__ == "__main__":
    main()
