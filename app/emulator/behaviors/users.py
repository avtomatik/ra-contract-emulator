from app.schemas.responses import UsersResponse


def list_users(request, state, dataset):
    return UsersResponse(items=dataset.users, links={"next": None})
