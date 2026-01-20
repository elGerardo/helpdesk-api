from app.utils.serializer import Serializer
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

async def get(
        session = None, 
        query = None,
        fields_to_serialize: list|bool = None
    ):
    if session is None:
        session = next(get_session())

    if query is None:
        raise ValueError("Query must be provided")
    
    result = session.exec(query).all()

    if fields_to_serialize is not None:
        if fields_to_serialize is True:
            fields_to_serialize = []
        result = Serializer.serialize(result, fields_to_serialize=fields_to_serialize)

    return result