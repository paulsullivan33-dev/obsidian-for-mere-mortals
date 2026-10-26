#!/usr/bin/env python3
"""Draw the lab vault's garden plan as a small PNG.

No image library needed: a PNG is a
header, some compressed rows, and a
checksum. Each row here is a strip of
solid colour blocks standing in for
beds, paths and the shed.
"""
import struct
import zlib

WIDTH, HEIGHT = 240, 160

GREEN = (96, 160, 80)
DARK_GREEN = (64, 128, 60)
BROWN = (150, 110, 70)
GREY = (140, 140, 140)
PALE = (210, 220, 180)


def block(x, y):
    """Colour of the pixel at (x, y)."""
    if y < 30:                      # shed strip at the top
        return GREY if 90 < x < 150 else PALE
    if 30 <= y < 70:                # north bed
        return GREEN
    if 70 <= y < 110:               # middle bed
        return DARK_GREEN
    if 110 <= y < 150:              # south bed
        return BROWN
    return PALE                     # path at the bottom


def chunk(kind, data):
    out = struct.pack(">I", len(data)) + kind + data
    out += struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    return out


rows = bytearray()
for y in range(HEIGHT):
    rows.append(0)  # filter type 0 for every row
    for x in range(WIDTH):
        rows.extend(block(x, y))

png = b"\x89PNG\r\n\x1a\n"
png += chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0))
png += chunk(b"IDAT", zlib.compress(bytes(rows)))
png += chunk(b"IEND", b"")

out = "Attachments/garden-plan.png"
import os
os.makedirs("Attachments", exist_ok=True)
with open(out, "wb") as f:
    f.write(png)
print(f"wrote {out} ({len(png)} bytes, {WIDTH}x{HEIGHT})")
