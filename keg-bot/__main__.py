import sys
from sample import blink

def main(args=None):
  """Keg-Bot entry-point."""
  if args is None:
    args = sys.argv[1:]

    print("Keg-Bot")

    # Blink sample
    blink()

if __name__ == "__main__":
  main()
