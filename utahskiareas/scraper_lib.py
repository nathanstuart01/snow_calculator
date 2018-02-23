class ScraperLib():

	def __init__(self, area_name):

		self.area_name = area_name

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
			'base_selector' : 'value',
			'base_selector_index' : 3,
			'twenty_four_hr_selector': 'value',
			'twenty_four_hr_index' : 2,
			},

			{ 

			'name' : 'snowbird', 
			'url': 'https://www.snowbird.com/', 
			'base_selector' : 'sb-condition_value', 
			'base_selector_index' : 4,
			'twenty_four_hr_selector': 'sb-condition_value',
			'twenty_four_hr_index' : 2, 
			},

			{
			'name': 'brighton',
			'url': 'http://www.brightonresort.com/mountain/snow-report/',
			'base_selector': 'h2',
			'base_selector_index': 3,
			'twenty_four_hr_selector': 'h2',
			'twenty_four_hr_index': 2,
			},

			{
			'name': 'solitude',
			'url': 'https://solitudemountain.com/',
			'base_selector': 'type',
			'base_selector_index': 2,
			'twenty_four_hr_selector': 'type',
			'twenty_four_hr_index': 0,
			},

			{
			'name': 'park city',
			'url': 'https://www.parkcitymountain.com/the-mountain/mountain-conditions/snow-and-weather-report.aspx',
			'base_selector': 'script',
			'base_selector_index': 1,
			'twenty_four_hr_selector': 'script',
			'twenty_four_hr_index': 1,
			},

			{
			'name': 'deer valley',
			'url': 'http://www.deervalley.com/',
			'base_selector': 'conditions',
			'base_selector_index': 0,
			'twenty_four_hr_selector': 'conditions',
			'twenty_four_hr_index': 0,
			},

			{
			'name': 'snowbasin',
			'url': 'https://www.snowbasin.com/',
			'base_selector': 'snow-report-grid',
			'base_selector_index': 3,
			'twenty_four_hr_selector': 'snow-report-grid',
			'twenty_four_hr_index': 1,
			},

			{
			'name': 'powder mountain',
			'url': 'http://www.powdermountain.com/en/',
			'base_selector': 'gmad-third-col',
			'base_selector_index': 2,
			'twenty_four_hr_selector': 'gmad-third-col',
			'twenty_four_hr_index': 0,
			},

			{
			'name': 'beaver mountain',
			'url': 'http://www.skithebeav.com',
			'base_selector': 'td',
			'base_selector_index': 3,
			'twenty_four_hr_selector': 'td',
			'twenty_four_hr_index': 1,
			},

			{
			'name': 'cherry peak',
			'url': 'http://skicherrypeak.com/rpt/?snow-report',
			'base_selector': 'xr_tl xr_kern Normal_text',
			'base_selector_index': 2,
			'twenty_four_hr_selector': 'xr_tl xr_kern Normal_text',
			'twenty_four_hr_index': 5,
			},

			{
			'name': 'brian head',
			'url': 'http://www.brianhead.com/Current-Weather',
			'base_selector': 'text-left',
			'base_selector_index': 7,
			'twenty_four_hr_selector': 'text-left',
			'twenty_four_hr_index': 3,
			},

			{
			'name': 'eagle point',
			'url': 'http://www.eaglepointresort.com/winter',
			'base_selector': 'stat winter',
			'base_selector_index': 1,
			'twenty_four_hr_selector': 'stat winter',
			'twenty_four_hr_index': 0,
			},

			{
			'name': 'sundance',
			'url': 'https://sheetsu.com/apis/v1.0/5603400dbbf4?limit=1',
			'base_selector': 0,
			'base_selector_index': 'base',
			'twenty_four_hr_selector': 0,
			'twenty_four_hr_index': '24_hour',
			},

			{
			'name': 'nordic valley',
			'url': 'https://nordicvalley.com/',
			'base_selector': 'td',
			'base_selector_index': 6,
			'twenty_four_hr_selector': 'td',
			'twenty_four_hr_index': 4,
			},

			]







