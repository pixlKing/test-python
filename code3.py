def CleanFileNames(file):
	return file.split('.')[0].lower()

# Read all source data files
for filename in os.listdir('/content/drive/My Drive/resume'):
	if filename.endswith('.txt'):
		cleanFileNames=CleanFileNames(filename)

		# with open(os.path.join('/content/drive/My Drive/resume', filename)) as f:
		# 	doc = f.read()
		# 	print(doc)
		with open(os.path.join('/content/drive/My Drive/resume', filename)) as searchfile:
			for line in searchfile:
				if 'HTML' in line:
					print(line)
#######################################
df=pd.DataFrame({
    'name':['Ana','Braulio','Carlos','Ana','Ana'],
    'skills':['HTML','CSS','JS','CSS','CSS'],
})
print(df)

# Render graphic
df.groupby(['name','skills'])['count'].size().unstack().plot(kind='bar',stacked=True, title='Skills')
plt.ylabel('Count')
plt.show()