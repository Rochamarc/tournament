import json

def get_json_obj(json_file):
	''' Return the object of the json file that correspons to the api '''
	
	with open(f'json/{json_file}', 'r') as file:
		data = file.read()

	obj = json.loads(data)
	return obj 

if __name__ == 	"__main__":	
	print(get_json_obj('trophy.json')) # this is a object