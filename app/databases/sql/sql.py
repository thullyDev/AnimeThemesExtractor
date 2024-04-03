from . import get_models
# from django.forms.models import model_to_dict
# from django.db import IntegrityError


class Sql:
	def sql_get(self, unit, as_dict=True, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return None

		data = self.get_instance_as_dict(instance) if as_dict else instance

		return data

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
		model = self.get_model(unit)

		try:
			data = model.objects.get(**kwargs)

			return data
		except model.DoesNotExist:
			return None

		return model.objects.get(id=unique_id)

	def get_model(self, unit):
		unit = get_models(unit)
		return unit

	def get_instance_as_dict(self, instance):
		return model_to_dict(instance)

	def sql_get_all(self, unit):
		model = self.get_model(unit)
		return list(model.objects.values())
			
	def sql_get_query(self, *, unit, **kwargs):
	    model = self.get_model(unit)
	    
	    values = model.objects.filter(**kwargs)
	    
	    return list(values)