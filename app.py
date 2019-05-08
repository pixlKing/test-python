import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
app = Flask(__name__)



# Create dictionary
dictionary = ['HTML','CSS','JS']

# Define empty object to use later for graphic
OBJ = {
	'name':[],
	'skills':[]
}

def CleanFileNames(file):
	return file.split('.')[0].lower()

# Read all source data files
for filename in os.listdir('./data'):
	if filename.endswith('.txt'):
		cleanFileNames=CleanFileNames(filename)

		with open(os.path.join('./data', filename), encoding='utf-8') as searchfile:
			for line in searchfile:		# For each line of the source files
				for term in dictionary:	# For each term from dictionary in each line
					if term in line:
						OBJ['name'].append(cleanFileNames)
						OBJ['skills'].append(term)

# Create dataFrame for graphic
df=pd.DataFrame(OBJ)
print(df)

# Render graphic
df.groupby(['name','skills']).size().unstack().plot(kind='bar',stacked=True, title='Skills')
plt.ylabel('Count')
plt.savefig('./static/images/plot.png')
#plt.show()



###### ROUTES ######
@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)