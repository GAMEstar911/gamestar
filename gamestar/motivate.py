from __future__ import annotations

import random
from typing import Optional, Sequence


DEFAULT_MESSAGES: Sequence[str] = (
    "You are building something powerful.",
    "Every expert was once a beginner.",
    "Your skills are growing every day.",
    "Gamestar believes in you.",
    "You are closer than you think.",
)


def motivate(messages: Optional[Sequence[str]] = None) -> str:
    selection_pool = tuple(messages) if messages is not None else DEFAULT_MESSAGES
    if not selection_pool:
        raise ValueError("messages must contain at least one entry")

    message = random.choice(selection_pool)
    print("Gamestar says:")
    print(message)
    return message
