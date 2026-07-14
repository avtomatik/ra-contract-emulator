from app.behaviors.user.get import GetUserBehavior
from app.behaviors.user.list import ListUsersBehavior
from app.emulator.router import Route

user_routes = [
    Route("GET", "/api/ra/users", ListUsersBehavior.execute),
    Route("GET", "/api/ra/users/{id}", GetUserBehavior.execute),
]
