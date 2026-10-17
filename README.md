
## Projects

### [Error correction](error-correction/)

Simulation of binary message transmission using three methods:

- Parity bit.
- Triple repetition with majority-vote decoding.
- Hamming (7,4) code.

Includes random single-bit errors and a comparison of detection and recovery results.

### [Integer representation](integer-representation/)

Conversion of integers to sign-magnitude, ones' complement, and two's complement representations.

Includes:

- Configurable bit width and range checks.
- Conversion back to integers with automatic verification.
- Comparison of 4-bit, 8-bit, and 16-bit ranges.
- Demonstration of how retaining only the lowest bits changes out-of-range values.

## Running

Tested with Python 3.14.7. No external dependencies are needed.

Run either program from the repository root:

```bash
python error-correction/main.py
python integer-representation/main.py
```
