
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
for filename in os.listdir('/content/drive/My Drive/resume'):
	if filename.endswith('.txt'):
		cleanFileNames=CleanFileNames(filename)

		with open(os.path.join('/content/drive/My Drive/resume', filename)) as searchfile:
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
plt.show()