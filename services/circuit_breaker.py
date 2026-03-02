import time
from core.config import settings

cooldown_state = {}

def is_in_cooldown(corridor: str):
    data = cooldown_state.get(corridor)
    if not data:
        return False
    return time.time() < data["expires_at"]

def activate_cooldown(corridor: str):
    cooldown_state[corridor] = {
        "expires_at": time.time() + settings.COOLDOWN_SECONDS
    }
