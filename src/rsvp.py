from collections import Counter
from typing import List, Optional, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """
    Deduplicate emails case-insensitively, but preserve the order
    and keep the first-seen original casing.
    Non-email strings (no '@') are skipped.
    """
    seen = set()
    result = []
    for e in emails:
        if "@" not in e:
            continue
        lower = e.casefold()
        if lower not in seen:
            seen.add(lower)
            result.append(e)
    return result


def first_with_domain(emails: List[str], domain: str) -> Optional[int]:
    """
    Return the index of the first email whose domain matches `domain`,
    ignoring case. Return None if not found.
    """
    d_cf = domain.casefold()
    for i, e in enumerate(emails):
        if "@" not in e:
            continue
        _, _, dom = e.rpartition("@")
        if dom.casefold() == d_cf:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """
    Count valid email domains case-insensitively.
    Returns a list of (domain, count) sorted by domain name.
    """
    counter = Counter()
    for e in emails:
        if "@" not in e:
            continue
        _, _, dom = e.rpartition("@")
        counter[dom.casefold()] += 1
    return sorted(counter.items())
