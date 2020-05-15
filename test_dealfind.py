import unittest
import json
from dealfind import item_price, get_number, find_matches, formatTitle

test_file = open('test_values.json')
data = json.load(test_file)

class TestCase(unittest.TestCase):

	def test_item_price(self):
		self.assertEqual("104", item_price("[Ram] [B-Die] Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory ($104)"))
		self.assertNotEqual("104", item_price("[Ram] [B-Die] Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory ($)"))
		self.assertNotEqual("104", item_price("[Ram] [B-Die] Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory ($200)"))
		self.assertNotEqual("0", item_price(""))
		self.assertEqual(None, item_price(""))
		self.assertEqual(None, item_price("$"))
		self.assertNotEqual("0", item_price("[Ram] [B-Die] Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory"))
		self.assertEqual("104", item_price("[Ram] [B-Die] ($104) Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory"))
		self.assertEqual("104", item_price("[Ram] [B-Die] Patriot Viper Steel Series DDR4 4000 19-19-19 2 x 8GB Memory $104"))
	
	def test_get_number(self):
		self.assertEqual("0", get_number("0",0))
		self.assertNotEqual("0", get_number("0",1))
		self.assertNotEqual("1", get_number("1234",1))
		self.assertNotEqual("1", get_number("234",1)) 
		self.assertNotEqual("1", get_number("1",4)) #test index > stringlength

	def test_get_matches(self):
		deallist = data['sample_list']
		test_cases = data['cases']

		for i in range(len(test_cases)):
			with self.subTest(i=i):
				component = test_cases[i]['component']
				price = float('%.2f' % float(test_cases[i]['price']))
				result = test_cases[i]['result']
				matches = find_matches(component, price, deallist)

				self.assertEqual(result , matches)
		
if __name__ == "__main__":
	unittest.main()