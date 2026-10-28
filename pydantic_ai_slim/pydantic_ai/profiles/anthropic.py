from __future__ import annotations as _annotations

from contextvars import ContextVar
from typing import Literal, TypeAlias

from ..native_tools import (
    AdvisorTool,
    CodeExecutionTool,
    MCPServerTool,
    MemoryTool,
    WebFetchTool,
    WebSearchTool,
)
from ..native_tools._tool_search import ToolSearchTool
from ..settings import ThinkingEffort, ThinkingLevel
from . import ModelProfile
from .._json_schema import JsonSchema, JsonSchemaTransformer
