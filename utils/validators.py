from django.core.validators import RegexValidator


class SimpleTweetValidator(RegexValidator):
	"""
	validator to validare simple character field for dweet
	"""
	regex = r'^[\w.@+-]+$'
	message = (
		'Enter a valid username. This value may contain only letters, '
		'numbers, and @/./+/-/_ characters.'
	)