
from typing import Type, Optional, Any
from sqlmodel import SQLModel, Field as SQLField, select
from pydantic import field_validator, ValidationInfo


_field_validations = {}

def Field(
    default: Any = ...,
    *,
    unique_in: Optional[Type[SQLModel]] = None,
    exists_in: Optional[Type[SQLModel]] = None,
    **kwargs
) -> Any:
    """Field extendido con validaciones de DB"""
    
    field_id = id(kwargs)
    
    if unique_in or exists_in:
        _field_validations[field_id] = {
            'unique_in': unique_in,
            'exists_in': exists_in
        }
    
    if 'description' in kwargs:
        kwargs['description'] = f"{kwargs['description']}|_fid:{field_id}"
    else:
        kwargs['description'] = f"_fid:{field_id}"
    
    if default is ...:
        return SQLField(**kwargs)
    else:
        return SQLField(default=default, **kwargs)
    

    
class ValidatedModel(SQLModel):
    """Clase base con validaciones automáticas de DB"""
    
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Crear validadores dinámicamente basados en metadata
        for field_name, field_info in cls.model_fields.items():
            # Buscar metadata de validación
            if hasattr(field_info, 'json_schema_extra') and field_info.json_schema_extra:
                extra = field_info.json_schema_extra
                
                # Validación unique
                if 'unique_in' in extra:
                    cls._add_unique_validator(field_name, extra['unique_in'])
                
                # Validación exists
                if 'exists_in' in extra:
                    cls._add_exists_validator(field_name, extra['exists_in'])
    
    @classmethod
    def _add_unique_validator(cls, field_name: str, model: Type[SQLModel]):
        """Añade validador de unique al campo"""
        def validator(v: Any, info: ValidationInfo) -> Any:
            if 'session' in info.context:
                session = info.context['session']
                statement = select(model).where(getattr(model, field_name) == v)
                existing = session.exec(statement).first()
                if existing:
                    raise ValueError(f'{field_name} already exists')
            return v
        
        # Registrar el validador usando el decorador de Pydantic
        validator_method = field_validator(field_name)(classmethod(validator))
        setattr(cls, f'_validate_{field_name}_unique', validator_method)
    
    @classmethod
    def _add_exists_validator(cls, field_name: str, model: Type[SQLModel]):
        """Añade validador de exists al campo"""
        def validator(v: Any, info: ValidationInfo) -> Any:
            if 'session' in info.context:
                session = info.context['session']
                statement = select(model).where(getattr(model, field_name) == v)
                existing = session.exec(statement).first()
                if not existing:
                    raise ValueError(f'{field_name} does not exist')
            return v
        
        validator_method = field_validator(field_name)(classmethod(validator))
        setattr(cls, f'_validate_{field_name}_exists', validator_method)