import os

REQUIRED_VARS = [
      "AUTH_TOKEN",
      "SECRET_KEY",
      "GITHUB_TOKEN",
      "QODER_PERSONAL_ACCESS_TOKEN",
  ]

def load_config():
      missing = [v for v in REQUIRED_VARS if not os.environ.get(v)]
      if missing:
          raise RuntimeError(f"Missing env vars: {missing}")
      return {v: os.environ[v] for v in REQUIRED_VARS}

