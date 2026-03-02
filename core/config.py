import os

class Settings:
    API_KEYS = {
        k.strip()
        for k in os.environ.get("PAYKX_API_KEYS", "paykx-demo-key-001").split(",")
    }

    GO_THRESHOLD = 0.60
    VOLATILITY_THRESHOLD = 0.25
    COOLDOWN_SECONDS = 90
    PROBE_WEIGHTS = {
        'behavioral': 0.4,
        'network': 0.3,
        'historical': 0.3
    }
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "")
    RECAPTCHA_SECRET = os.environ.get("RECAPTCHA_SECRET", "")
    ADMIN_EMAIL = "taseenrayed@paykx.co.uk"

settings = Settings()
