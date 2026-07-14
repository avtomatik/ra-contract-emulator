from dataclasses import dataclass
from typing import Protocol

from app.behaviors.context import BehaviorContext


class Handler(Protocol):
    def __call__(self, request: dict, context: BehaviorContext) -> object: ...


@dataclass(frozen=True)
class Route:
    method: str
    path: str
    handler: Handler


class EmulatorRouter:
    def __init__(self, routes):
        self.routes = routes

    def match(self, method: str, path: str) -> tuple[Handler, dict[str, str]]:
        for route in self.routes:
            params = self._match_path(route.path, path)
            if route.method == method and params is not None:
                return route.handler, params

        raise KeyError(f"No route {method} {path}")

    def _match_path(self, pattern, path):
        p = pattern.split("/")
        a = path.split("/")

        if len(p) != len(a):
            return None

        params = {}

        for x, y in zip(p, a):
            if x.startswith("{"):
                params[x[1:-1]] = y
            elif x != y:
                return None

        return params
