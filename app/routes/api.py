from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from app.http.controllers.auth_controller import AuthController
from app.http.controllers.user_controller import UserController

async def homepage(_):
    return JSONResponse({'service': 'help-desk', 'version': 1.0})
    
routes = [
    Mount('/api', routes=[
        Route('/live', homepage, methods=['GET']),
        
        Mount('/auth', routes=[
            Route('/login', AuthController.login, methods=['POST']),
            Route('/me', AuthController.me, methods=['GET']),
        ]),
        
        Mount('/users', routes=[
            Route('/', UserController.store, methods=['POST']),
            Route('/{user_name}', UserController.findOrStore, methods=['POST'])
        ])
    ])
]