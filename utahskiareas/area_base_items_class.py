class SkiArea():
	"""A ski area class and attributes"""

	def __init__(self, current_base, location, yearly_snowfall):
		"""initialize ski area"""
			
		# daily crawled base value
		self.current_base = current_base
		# user defined mountain range location 
		self.location = location 
		# downloaded and crawled historical snowfall
		self.yearly_snowfall = yearly_snowfall

	# method to calculate mean yearly snowfall from downloaded and crawled data, 
	def mean_yearly_snow_fall_calculator(self):
		return self.yearly_snowfall

	# method to calculate std of yearly snowfall from downloaded and crawled data
	def std_yearly_snow_fall_calculator(self):
		return self.yearly_snowfall

	# method to calculate 24 snowfall total from daily crawled data
	def twenty_four_hour_snow_fall(self):
		return self.current_base