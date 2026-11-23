from pathlib import Path

LINE = "My parrot learned to say 'meeting in five minutes' from my calls, and now the whole office stands up whenever the bird clears its throat."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
