from sqlmodel import SQLModel
from starlette.responses import JSONResponse

def _serialize_model(model: SQLModel) -> dict:
    """Serialize a SQLModel instance including relationships"""
    # Get base model data
    data = model.model_dump()
    
    # Get all relationship fields
    for field_name, field_info in model.model_fields.items():
        if hasattr(model, field_name):
            value = getattr(model, field_name)
            print(field_name)
            # Check if it's a relationship (SQLModel or list of SQLModel)
            if isinstance(value, SQLModel):
                data[field_name] = value.model_dump()
            elif isinstance(value, list) and value and isinstance(value[0], SQLModel):
                data[field_name] = [item.model_dump() for item in value]
    
    return data

def created(data: dict | SQLModel):
    if isinstance(data, SQLModel):
        data = data.model_dump()
        #data = _serialize_model(data)
    return JSONResponse({"data": data}, status_code=201)

def updated(data: dict | SQLModel):
    if isinstance(data, SQLModel):
        data = _serialize_model(data)
    return JSONResponse({"data": data}, status_code=202)

def ok(data: dict | SQLModel | list):
    if isinstance(data, SQLModel):
        data = _serialize_model(data)
    return JSONResponse({"data": data}, status_code=200)

def deleted():
    return JSONResponse(status_code=204)