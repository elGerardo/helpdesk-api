from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from app.http.controllers.auth_controller import AuthController
from app.http.controllers.user_controller import UserController
from app.http.controllers.user_workspaces_controller import UserWorkspacesController
from app.http.controllers.user_tickets_controller import UserTicketsController
from app.http.middleware.authorization_middleware import AuthorizationMiddleware
from starlette.middleware import Middleware
from app.http.controllers.guest_controller import GuestController

async def homepage(_):
    return JSONResponse({'service': 'help-desk', 'version': 1.0})
    
routes = [
    Mount('/api', routes=[
        Route('/live', homepage, methods=['GET']),
        
        Mount('/auth', routes=[
            Route('/login', AuthController.login, methods=['POST']),
            Route('/me', AuthController.me, methods=['GET'], middleware=[Middleware(AuthorizationMiddleware)]),
        ]),

        Mount('/guests', routes=[
            Route('/', GuestController.store, methods=['POST'])
        ]),

        Mount('/user-workspaces', routes=[
            Route('/', UserWorkspacesController.index, methods=['GET']),
        ], middleware=[Middleware(AuthorizationMiddleware)]),

        Mount('/user-tickets', routes=[
            Route('/', UserTicketsController.index, methods=['GET']),
        ], middleware=[Middleware(AuthorizationMiddleware)]),
        
        Mount('/users', routes=[
            Route('/', UserController.store, methods=['POST']),
            Route('/{user_name}', UserController.find, methods=['GET'])
        ], middleware=[Middleware(AuthorizationMiddleware)]),

    ])
]