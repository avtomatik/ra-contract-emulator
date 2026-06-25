from dataclasses import dataclass
from typing import Any, Callable

Handler = Callable[[dict, Any, Any], Any]


@dataclass(frozen=True)
class Route:
    method: str
    path: str
    handler: Handler


class EmulatorRouter:
    def __init__(self, routes: list[Route]):
        self.routes = routes

    def match(self, method: str, path: str) -> Handler:
        for route in self.routes:
            if route.method == method and self._match_path(route.path, path):
                return route.handler

        raise KeyError(f"No route for {method} {path}")

    def _match_path(self, pattern: str, path: str) -> bool:

        if pattern == path:
            return True

        if "{" in pattern:
            p_parts = pattern.split("/")
            a_parts = path.split("/")

            if len(p_parts) != len(a_parts):
                return False

            for p, a in zip(p_parts, a_parts):
                if p.startswith("{") and p.endswith("}"):
                    continue
                if p != a:
                    return False

            return True

        return False
