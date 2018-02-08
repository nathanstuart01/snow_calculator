class ScraperLib():

	def __init__(self):

		self.area_dict_template = area_dict_template = {
			'name': '',
			'url': '',
			'base_selector': '',
			'base_selector_index': '',
			'twenty_four_hr_selector': '',
			'twenty_four_hr_index': '',
			}

		self.area_selector_library = [
			{ 
			'name' : 'alta', 
			'url': 'https://www.alta.com/', 
			'base_selector' : 'class_="value"',
			'base_selector_index' : '[3].contents[0].text',
			'twenty_four_hr_selector': 'class_="value"',
			'twenty_four_hr_index' : '[2].contents.text',
			},

			{ 

			'name' : 'snowbird', 
			'url': 'https://www.snowbird.com/', 
			'base_selector' : '(class_="sb-condition_value")', 
			'base_selector_index' : '[4].text',
			'twenty_four_hr_selector': '(class_="sb-condition_value")',
			'twenty_four_hr_index' : '[2].text', 
			},

			{
			'name': 'brighton',
			'url': 'http://www.brightonresort.com/mountain/snow-report/',
			'base_selector': 'h2',
			'base_selector_index': '[3].contents[0].replace(""", "")',
			'twenty_four_hr_selector': 'find_all("p")',
			'twenty_four_hr_index': '[3].contents[0].replace("\r\n\t\t\t\t\t\tLast 24hr: ", " "").replace(""", " ")',
			},

			{
			'name': 'solitude',
			'url': 'https://solitudemountain.com/',
			'base_selector': 'find_all(class_="type")',
			'base_selector_index': '[2].text.replace("Base ", '').replace(""", '')',
			'twenty_four_hr_selector': 'find_all(class_="type")',
			'twenty_four_hr_index': '[0].text.replace("24 Hrs ", '').replace(""", '')',
			},

			{
			'name': 'park city',
			'url': 'https://www.parkcitymountain.com/the-mountain/mountain-conditions/snow-and-weather-report.aspx',
			'base_selector': "script",
			'base_selector_index': '1',
			'twenty_four_hr_selector': "soup.find_all('script', type='text/javascript')[1]",
			'twenty_four_hr_index': '',
			},

			{
			'name': 'deer valley',
			'url': 'http://www.deervalley.com/',
			'base_selector': 'conditions',
			'base_selector_index': 'findChildren()[8].contents[0].replace(""", " ")',
			'twenty_four_hr_selector': "find(id='home-mountain-info')",
			'twenty_four_hr_index': 'findChildren()[2].contents[0].replace(""", " ")',
			},

			{
			'name': 'snow basin',
			'url': 'https://www.snowbasin.com/',
			'base_selector': '.find(class_="snow-report-grid")',
			'base_selector_index': '.find_all(class_="right")[2].contents[0].replace(""", '')',
			'twenty_four_hr_selector': '.find(class_="snow-report-grid")',
			'twenty_four_hr_index': '.find_all(class_="right")[0].contents[0].replace(""", '')',
			},

			{
			'name': 'powder mountain',
			'url': 'http://www.powdermountain.com/en/',
			'base_selector': '.find_all(class_="gmad-third-col")',
			'base_selector_index': '[0].findChildren()[2].text.replace("", '')',
			'twenty_four_hr_selector': '.find_all(class_="gmad-third-col")',
			'twenty_four_hr_index': '[2].findChildren()[2].text.replace(""", '')',
			},

			{
			'name': 'beaver mountain',
			'url': 'http://www.skithebeav.com/',
			'base_selector': '.find_all("table")[0]',
			'base_selector_index': '.findChildren()[7].text.replace(""", '')',
			'twenty_four_hr_selector': '.find_all("table")[0]',
			'twenty_four_hr_index': '.findChildren()[3].text.replace(""", '')',
			},

			{
			'name': 'cherry peak',
			'url': 'http://skicherrypeak.com/rpt/?snow-report',
			'base_selector': '.find_all(class_="xr_tl xr_kern Normal_text")',
			'base_selector_index': '[2].contents[1]',
			'twenty_four_hr_selector': '',
			'twenty_four_hr_index': '[5].contents[1]',
			},

			{
			'name': 'brian head',
			'url': 'http://www.brianhead.com/Current-Weather',
			'base_selector': 'text-left',
			'base_selector_index': '[7].text.replace(""", '')',
			'twenty_four_hr_selector': '.find_all(class_="text-left")',
			'twenty_four_hr_index': '[3].text.replace(""", '')',
			},

			{
			'name': 'eagle point',
			'url': 'http://www.eaglepointresort.com/winter',
			'base_selector': 'stat winter',
			'base_selector_index': '[1].contents[1].text.replace(""", '')',
			'twenty_four_hr_selector': '.find_all(class_="stat winter")',
			'twenty_four_hr_index': '[0].contents[1].text.replace(""", '')',
			},

			{
			'name': 'sundance',
			'url': 'https://sheetsu.com/apis/v1.0/5603400dbbf4?limit=1',
			'base_selector': '0',
			'base_selector_index': "base",
			'twenty_four_hr_selector': 'sundance_data[0]',
			'twenty_four_hr_index': "['24_hour']",
			},

			{
			'name': 'nordic valley',
			'url': 'https://nordicvalley.com/',
			'base_selector': 'td',
			'base_selector_index': '[6].text.replace(""", '')',
			'twenty_four_hr_selector': '.find_all("td")',
			'twenty_four_hr_index': '[4].text.replace(""", '')',
			},

			]







