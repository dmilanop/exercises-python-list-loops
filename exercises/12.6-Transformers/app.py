incoming_ajax_data = [
	{ "name": 'Mario', "last_name": 'Montes' },
	{ "name": 'Joe', "last_name": 'Biden' },
	{ "name": 'Bill', "last_name": 'Clon' },
	{ "name": 'Hilary', "last_name": 'Mccafee' },
	{ "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:
def data_transformer(data):
	# valor = f'{data["name"]} {data["last_name"]}'

	return f'{data["name"]} {data["last_name"]}'

new_list = list(map(data_transformer, incoming_ajax_data))

print(new_list)
