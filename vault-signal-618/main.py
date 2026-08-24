"""Vault Signal - defensive file-integrity baseline checker."""
import hashlib
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


if __name__ == "__main__":
    print("Usage: import sha256 and compare a known-good checksum to a file checksum.")
