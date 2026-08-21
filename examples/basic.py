"""Minimal example for MovieDiary."""

from moviediary import moviediary


def main():
 runner = moviediary({"name": "MovieDiary", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()