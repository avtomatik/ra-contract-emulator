from dataclasses import dataclass
from typing import Any, Callable

Handler = Callable[[dict, Any, Any], Any]


@dataclass(frozen=True)
class Route:
    method: str
    path: str
    handler: Handler


class EmulatorRouter:
    def __init__(self, routes):
        self.routes = routes

    def match(self, method, path):
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
