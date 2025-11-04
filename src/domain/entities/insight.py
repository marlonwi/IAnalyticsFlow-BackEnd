from dataclasses import dataclass
from typing import Any

@dataclass
class Insight:
    prompt: str
    sql: str
    result: Any
    summary: str = ""
    chart_config: dict | None = None
