"""Packet Lantern - defensive DNS-query baseline checker."""
from collections import Counter


def find_rare_domains(domains, minimum=2):
    counts = Counter(domains)
    return [domain for domain, count in counts.items() if count < minimum]


if __name__ == "__main__":
    queries = ["example.org", "example.org", "unexpected.test"]
    print("Rare domains:", find_rare_domains(queries))
