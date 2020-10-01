import json
x=[]
res=[]
with open('plates.json') as json_file:
        data = json.load(json_file)

        for i in range(len(data)-1):
        	#print(data[i])
        	#print('\n')
        	for key,value in data[i].items():
        		#print(key,value)
        		if key=='results':
        			for key1,value1 in value[0].items():
        				#print('key1:',key1,value1)
        				if key1=='plate':
        					print("plate:",value1)
        					x.append(value1)
        					#print('\n')
        			[res.append(i) for i in x if i not in res]
        print(res)