import math
import random
import matplotlib.pyplot as plt

with open("data/sequence.fasta") as file:
    sequence = "".join(line.strip() for line in file if not line.startswith(">"))

samples = []
for _ in range(10):
    length = random.randint(100, min(3000, len(sequence)))
    start = random.randint(0, len(sequence) - length)
    samples.append(sequence[start:start + length])

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_facecolor("black")

for lane, sample in enumerate(samples, 1):
    distance = math.log(3000 / len(sample)) / math.log(3000 / 100) * 100
    print(f"Lane {lane}: {len(sample)} bases, migrated {distance:.1f}%")
    ax.plot([lane - 0.35, lane + 0.35], [distance, distance], color="white", linewidth=4)
    ax.text(lane, distance + 4, f"{len(sample)} bp", color="white", ha="center", fontsize=8)

ax.set_xlim(0.4, 10.6)
ax.set_ylim(108, -3)
ax.set_xticks(range(1, 11))
ax.set_xlabel("Lane")
ax.set_ylabel("Migration distance from well (%)")
ax.set_title("Simulated gel electrophoresis")
plt.savefig("gel.png", dpi=150)
plt.show()
