import json,sys,getopt
from pprint import pprint
def main(argv):
	state_id = ''
	# print("ENTER")
	try:
		opts, args = getopt.getopt(argv, "hs:", ["state="])
	except getopt.GetoptError:
		print("test.py -s <state_id>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("test.py -s <state_id>")
			sys.exit()
		elif opt in ('-s', '--state'):
			state_id = arg

	infile = 'zips-by_state.json'

	with open(infile, encoding='utf-8') as data_file:
	    data = json.loads(data_file.read())
	# with open(infile, 'r') as data_file:
	# 	data = json.loads(data_file)
		# data = json.load(infile)
		# for line in infile :
		# 	print line
	State_Zip = data[state_id]
response = []

for zip in State_Zip:
	# print(zip)
	count = 0
	for row in data["features"]:
		if(row['properties']['GEOID10'] == zip['Zip']):
			# print(row)
			count = 1
			response.append(row)

zips  = [{
	"type": "FeatureCollection",
	"features" : response
}]

with open("state_filtered_zip"+state_id+".json", "a") as myfile:
	myfile.write(json.dumps(zips))
    		
if __name__=="__main__":
	main(sys.argv[1:])
