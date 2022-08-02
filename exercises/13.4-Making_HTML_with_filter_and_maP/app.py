all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color_true):
	return color_true["sexy"] == True

filter_list = list(filter(filter_colors, all_colors))

def generate_li(items):
	return f'<li>{items["label"]}</li>'

new_list_map = list(map(generate_li, all_colors))

print(new_list_map)
