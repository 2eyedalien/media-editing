"""Utility helpers for media editing practice.

Note: File I/O functions expect generic placeholder paths. Replace with your own paths
when running locally.
"""

from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

def ensure_dir(p: PathLike) -> Path:
    p = Path(p)
    p.mkdir(parents=True, exist_ok=True)
    return p
