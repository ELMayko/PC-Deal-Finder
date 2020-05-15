def find_char_index(title, delimiter):
	position = title.find(delimiter)
	return position

def item_price(title):
	position = find_char_index(title, '$')
	
	if position == -1:
		return

	price = get_number(title, position+1)
	if not price:
		return

	return price

#get number substring present starting at word[index] if it exists 
def get_number(word, index):
	result = ""
	while (index < len(word)):
		if not str.isdigit(word[index]) and word[index] != '.':
			break
		result += word[index]
		index += 1
	
	return result

#returns component name from title with structure '[Component] Description $Price'
def get_component(title):
	start = find_char_index(title, '[')
	end = find_char_index(title, ']')

	if start == -1 or end == -1:
		return

	return title[start + 1: end]

#returns list of posts which contain the given component and fall below the target price
def find_matches(component, target_price, post_list):
	matches = []
	component = component.lower()
	for title in post_list:
		lower_title = title.lower()
		cost = item_price(lower_title)
		post_component = get_component(title).lower()
		if post_component == component and cost:
			float_cost = float('%.2f' % float(cost))
			if float_cost <= target_price:
				matches.append(formatTitle(title, cost))
	return matches

def formatTitle(title, cost):
	return 'Title: {} Price: ${}'.format(title, cost)
