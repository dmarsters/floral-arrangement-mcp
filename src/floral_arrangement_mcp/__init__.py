"""
Floral Arrangement Aesthetics MCP Server

Dual-purpose server providing:
1. Prompt enhancement with professional floral vocabulary
2. ComfyUI workflow generation for floral imagery

Three-layer architecture:
- Layer 1: Deterministic taxonomy (arrangement styles, flowers, techniques)
- Layer 2: Structural mapping (balance, proportion, movement)
- Layer 3: Cultural/aesthetic context synthesis
"""

__version__ = "1.0.0"

from .server import main

__all__ = ["main"]
