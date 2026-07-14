from app.emulator.routes.certificate import certificate_routes
from app.emulator.routes.certificate_request import request_routes
from app.emulator.routes.user import user_routes

ROUTES = certificate_routes + request_routes + user_routes
