
import requests

r = requests.get('http://ec2-54-68-118-89.us-west-2.compute.amazonaws.com/api/v2/ziagodb/_table/user1?api_key=c1a18cebddd4bc8c305e044c1f5a4d846f4b7e816211619a193375fcc4dbeae1'  )

	data = r.jason()
	assert(len(data['resource']))
	for CBC in data['user1']:
		machineType = CBC['machineType']	
		weight = CBC['weight']
		gender = CBC ['gender']
		age = CBC ['age']
		height = CBC ['gender']
		lname = CBC ['lname']
		fname = CBC ['Fname']
	
print (fname)
 
