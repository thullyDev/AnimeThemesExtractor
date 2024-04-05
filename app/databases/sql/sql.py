from typing import Dict, Any, Sequence, Union
from sqlmodel import Session, select, SQLModel
from .setup import engine

class Sql:
	def __init__(self, model) -> None:
		self.model = model

	def sql_set(self, data: Dict[str, Any], *, unit: str) -> SQLModel:
		with Session(engine) as session:
			instance = self.model.model_validate(**data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_set_all(self, data: list[Dict[str, Any]], *, unit: str) -> None:
		for item in data:
			with Session(engine) as session:
				instance = self.model.model_validate(**data)
				session.add(instance)
				session.commit()
				session.refresh(instance)

	def sql_get(self, *, unit: str, **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)
			if not instance:
				return None
			return instance

	def sql_update(self, *, unit: str, data: Dict[str, Any], **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)

			if not instance:
				return None

			instance.sqlmodel_update(data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_delete(self, *, unit: str, **kwargs) -> bool:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)

			if not instance:
				return False

			session.delete(instance)
			session.commit()
			return True

	def sql_get_all(self, *, unit: str) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(self.model)).all()
			return data
			
	def sql_get_query(self, *, unit: str, **kwargs) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(self.model).filter(**kwargs)).all()
			return data
