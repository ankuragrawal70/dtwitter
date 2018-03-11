from django.core.validators import RegexValidator


class SimpleTweetValidator(RegexValidator):
	regex = r'^[\w.@+-]+$'
	message = (
		'Enter a valid username. This value may contain only letters, '
		'numbers, and @/./+/-/_ characters.'
	)