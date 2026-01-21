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
        fields_to_serialize: list|bool = None,
        pagination: dict = None
    ) -> list|dict:
    if session is None:
        session = next(get_session())

    if query is None:
        raise ValueError("Query must be provided")

    
    total_records = 0
    total_pages = 0
    page = 0
    limit = 10
    
    if pagination is not None:
        page = pagination.get('page', 0)
        limit = pagination.get('limit', 10)

        rows = session.exec(query).all()
        total_records = len(rows)

        query = query.offset(page * limit).limit(limit)

        if limit >= total_records:
            total_pages = 1
        else:
            total_pages = round(total_records / limit if limit > 0 else 1)

        if total_records < 1:
            total_pages = 0

        
    result = session.exec(query).all()

    if fields_to_serialize is not None:
        if fields_to_serialize is True:
            fields_to_serialize = []
        result = Serializer.serialize(result, fields_to_serialize=fields_to_serialize)

    meta = {
        "total_pages": total_pages,
        "total_records": total_records,
        "page": page,
        "limit": limit,
    }

    if pagination is not None:
        return {
            "meta": meta,
            "data": result
        }

    return result