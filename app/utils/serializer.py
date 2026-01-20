from sqlmodel import SQLModel

class Serializer:
    def serialize(model: SQLModel|list[SQLModel]|list[dict], fields_to_serialize: list) -> dict:
        if isinstance(model, list):
            data = [Serializer.serialize_rows(item, fields_to_serialize) for item in model]
        else:
            data = Serializer.serialize_rows(model, fields_to_serialize)

        return data

    def serialize_rows(model: SQLModel|dict, fields_to_serialize: list) -> list[dict]:
        
        if isinstance(model, dict):
            data = model
        else:
            data = model.model_dump(mode='json')

        for field in fields_to_serialize:
            value = getattr(model, field, None)
            if isinstance(value, SQLModel):
                data[field] = value.model_dump(mode='json')
            elif isinstance(value, list) and value and isinstance(value[0], SQLModel):
                data[field] = [item.model_dump(mode='json') for item in value]

        return data
        