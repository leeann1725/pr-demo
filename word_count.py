"""Simple word counting utility."""


def count_words(text):
    """Return a dict mapping each word in ``text`` to its occurrence count."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:\"'()")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        content = f.read()

    for word, count in sorted(count_words(content).items()):
        print(f"{word}: {count}")
