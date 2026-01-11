from sqlmodel import SQLModel

class Serializer:
    def serialize(model: SQLModel, fields_to_serialize: list) -> dict:
        
        data = model.model_dump()
        for field in fields_to_serialize:
            value = getattr(model, field, None)
            if isinstance(value, SQLModel):
                data[field] = value.model_dump()
            elif isinstance(value, list) and value and isinstance(value[0], SQLModel):
                data[field] = [item.model_dump() for item in value]

        return data