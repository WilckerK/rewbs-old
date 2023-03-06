import os

for f in os.listdir('routes'):
	if(os.path.isfile(os.path.join('routes', f))):
		print(f)