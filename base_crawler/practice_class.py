class PracticeClass():

	def __init__(self, name, url):
		self.name = name
		self.url = url

	def sit(self):
		print(self.url + " Is my url")

my_dog = PracticeClass('willie', 'www.6.com')

my_dog.sit()