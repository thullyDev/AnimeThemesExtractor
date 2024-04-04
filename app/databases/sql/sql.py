from typing import Dict, Any, Sequence, Type, Union
from sqlmodel import Session, select, SQLModel
from sqlalchemy.exc import IntegrityError
from . import get_models, get_model
from .setup import engine

class Sql:
	def sql_set(self, data: Dict[str, Any], *, unit: str) -> SQLModel:
		model = get_model(unit)
		with Session(engine) as session:
			instance = model.model_validate(**data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_get(self, *, unit: str, **kwargs) -> Union[SQLModel, None]:
		model = get_model(unit)
		with Session(engine) as session:
			instance = session.get(model, **kwargs)
			if not instance:
				return None
			return instance

	def sql_update(self, *, unit: str, data: Dict[str, Any], **kwargs) -> Union[SQLModel, None]:
		model = get_model(unit)
		with Session(engine) as session:
			instance = session.get(model, **kwargs)

			if not instance:
				return None

			instance.sqlmodel_update(data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_delete(self, *, unit: str, **kwargs) -> bool:
		model = get_model(unit)
		with Session(engine) as session:
			instance = session.get(model, **kwargs)

			if not instance:
				return False

			session.delete(instance)
			session.commit()
			return True

	def sql_get_all(self, *, unit: str) -> Sequence:
		model = get_model(unit)
		with Session(engine) as session:
			data = session.exec(select(model)).all()
			return data
			
	def sql_get_query(self, *, unit: str, **kwargs) -> Sequence:
		model = get_model(unit)
		with Session(engine) as session:
			data = session.exec(select(model).filter(**kwargs)).all()
			return data
