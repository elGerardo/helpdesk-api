from config.database import get_session
from starlette.exceptions import HTTPException

async def first_or_fail(session = None, query = None, error_message="Row not found"):
    if session is None:
        session = next(get_session())

    if query is None:
        raise ValueError("Query must be provided")
    
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail=error_message)
    
    result = result.model_dump(mode='json')
    
    return result

async def get(session = None, query = None): 
    if session is None:
        session = next(get_session())

    if query is None:
        raise ValueError("Query must be provided")
    
    result = session.exec(query).all()

    result = [result.model_dump(mode='json') for result in result]

    return result