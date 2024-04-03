from .setup import get_models
from sqlalchemy.exc import IntegrityError

class Sql:
	def sql_get(self, unit, as_dict=True, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return None

		if as_dict == False:
			return instance

		return self.get_instance_as_dict(instance) 

	def sql_set(self, data, *, unit):
		model = self.get_model(unit)
		try:
			instance = model.objects.create(**data)
			instance.save()
		except IntegrityError as e:
			print(e)
			return None

	def sql_update(self, unit, data, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return self.sql_set(unit=unit, data=data)

		instance.__dict__.update(data)
		instance.save()

	def sql_delete(self, *, unit, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return False
		instance.delete()

		return True

	def get_instance(self, *, unit, **kwargs): 
		pass
		# model = self.get_model(unit)

		# try:
		# 	data = model.objects.get(**kwargs)

		# 	return data
		# except model.DoesNotExist:
		# 	return None

		# return model.objects.get(id=unique_id)

	def get_model(self, unit): return get_models(unit)

	def sql_get_all(self, *, unit):
		pass
		# model = self.get_model(unit)
		# return list(model.objects.values())
			
	def sql_get_query(self, *, unit, **kwargs):
		pass
	    # model = self.get_model(unit)
	    
	    # values = model.objects.filter(**kwargs)
	    
	    # return list(values)