with open("data/sequence.fasta") as file:
    sequence = "".join(line.strip() for line in file if not line.startswith(">"))

for unit_length in range(3, 6):
    i = 0
    while i + unit_length <= len(sequence):
        unit = sequence[i:i + unit_length]
        count = 1
        while sequence[i + count * unit_length:i + (count + 1) * unit_length] == unit:
            count += 1
        total = count * unit_length
        if count >= 2 and 6 <= total <= 10 and unit not in (unit + unit)[1:-1]:
            print(f"Position {i + 1}: {unit} x {count} = {sequence[i:i + total]} ({total} bases)")
        i += total if count >= 2 else 1
