"""Base autonomous agent with ReAct reasoning."""
from typing import Any, List, Optional, Callable
from dataclasses import dataclass, field
import vertexai
from vertexai.generative_models import GenerativeModel, Tool, FunctionDeclaration

@dataclass
class AgentMemory:
    short_term: List[dict] = field(default_factory=list)
    episodic: List[dict] = field(default_factory=list)
    max_short_term: int = 20

    def add(self, role: str, content: str):
        self.short_term.append({"role": role, "content": content})
        if len(self.short_term) > self.max_short_term:
            self.short_term.pop(0)

class AutonomousAgent:
    def __init__(self, name: str, model: str = "gemini-1.5-pro-002",
                 tools: Optional[List[Callable]] = None, system_prompt: str = ""):
        self.name = name
        self.memory = AgentMemory()
        self.tools = tools or []
        self.model = GenerativeModel(model, system_instruction=system_prompt,
                                      tools=[self._build_tool_spec(t) for t in self.tools])
        self.iterations = 0
        self.max_iterations = 15

    def run(self, task: str) -> str:
        self.memory.add("user", task)
        while self.iterations < self.max_iterations:
            response = self.model.generate_content(
                [m["content"] for m in self.memory.short_term])
            if response.candidates[0].finish_reason.name == "STOP":
                result = response.text
                self.memory.add("assistant", result)
                return result
            # Handle tool calls
            tool_result = self._execute_tool_call(response)
            self.memory.add("tool", str(tool_result))
            self.iterations += 1
        return "Max iterations reached."

    def _build_tool_spec(self, fn: Callable) -> Tool:
        return Tool(function_declarations=[FunctionDeclaration.from_func(fn)])

    def _execute_tool_call(self, response) -> Any:
        fc = response.candidates[0].content.parts[0].function_call
        fn_map = {t.__name__: t for t in self.tools}
        return fn_map[fc.name](**dict(fc.args)) if fc.name in fn_map else "Tool not found"
