import sys
import absl.flags

def pytest_configure(config):
  try:
    absl.flags.FLAGS(sys.argv, known_only=True)
  except Exception:
    pass
