from typing import Dict, Any, Sequence, Union
from sqlmodel import Session, select, SQLModel
from .setup import engine

class Sql:
	def __init__(self, *, model) -> None:
		self.model = model

	def sql_set(self, data: Dict[str, Any]) -> SQLModel:
		with Session(engine) as session:
			instance = self.model.model_validate(**data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_set_all(self, data: list[Dict[str, Any]]) -> None:
		for item in data:
			with Session(engine) as session:
				instance = self.model.model_validate(**item)
				session.add(instance)
				session.commit()
				session.refresh(instance)

	def sql_get(self, **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)
			if not instance:
				return None
			return instance

	def sql_update(self, data: Dict[str, Any], **kwargs) -> Union[SQLModel, None]:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)

			if not instance:
				return self.sql_set(data)

			instance.sqlmodel_update(data)
			session.add(instance)
			session.commit()
			session.refresh(instance)
			return instance

	def sql_delete(self, **kwargs) -> bool:
		with Session(engine) as session:
			instance = session.get(self.model, **kwargs)

			if not instance:
				return False

			session.delete(instance)
			session.commit()
			return True

	def sql_get_all(self) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(self.model)).all()
			return data
			
	def sql_get_query(self, **kwargs) -> Sequence:
		with Session(engine) as session:
			data = session.exec(select(self.model).filter(**kwargs)).all()
			return data
