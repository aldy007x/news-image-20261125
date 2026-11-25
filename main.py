# THE WORLD TODAY — Wednesday 25 November 2026, one-page newspaper front page.
#
# Entry for the make.fun bounty "Sum up 25 November's world news in one image"
# (news-image-20261125). The front page is a single image generated in this
# session for the bounty and shipped in the repository as assets/entry.jpg.
# This program (Python 3.13, standard library only, no network) copies it
# byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png, verifying the gate's limits
# first: a whole JPEG, at most 1 MiB, 1024 by 1024 pixels.
#
# Deterministic: the same input bytes are written on every run, so two runs
# produce identical output. The output file is left world-readable (0644) so
# the grader can collect it.
import os
import shutil
import stat
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.jpg")
MAX_BYTES = 1048576  # 1 MiB, the bounty cap.
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def jpeg_dimensions(data):
    """Return (width, height) from a JPEG's first SOF marker, or None."""
    # JPEG markers: 0xFFD8 SOI, then segments 0xFF <marker> <len:2> <payload>.
    # SOF0 (0xC0), SOF1 (0xC1) and SOF2 (0xC2) carry height then width.
    i = 2
    while i + 9 <= len(data):
        if data[i] != 0xFF:
            return None
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = (data[i + 5] << 8) | data[i + 6]
            width = (data[i + 7] << 8) | data[i + 8]
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2  # standalone markers carry no length field
            continue
        seg_len = (data[i + 2] << 8) | data[i + 3]
        i += 2 + seg_len
    return None


def main():
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    # Gate checks, done here so a bad image fails loudly instead of
    # submitting a file the scorer would refuse.
    if len(data) < 2 or data[0] != 0xFF or data[1] != 0xD8:
        raise SystemExit("entry image is not a JPEG (bad SOI marker)")
    if len(data) > MAX_BYTES:
        raise SystemExit(
            "entry image is %d bytes, over the 1 MiB cap" % len(data)
        )
    # A whole image: the JPEG must run through to its end marker (EOI).
    if data[-2] != 0xFF or data[-1] != 0xD9:
        raise SystemExit("entry image is truncated (no JPEG EOI marker)")
    dims = jpeg_dimensions(data)
    if dims is None:
        raise SystemExit("could not read JPEG dimensions")
    if dims != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            "entry image is %dx%d, expected %dx%d"
            % (dims[0], dims[1], EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)
    # World-readable, as the grader collects the file as another user.
    os.chmod(out_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print("wrote %s %d bytes (%dx%d)" % (out_path, len(data), dims[0], dims[1]))


if __name__ == "__main__":
    main()
