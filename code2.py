data={
	0:{
		"name": "Matias",
		"skills": "HTML",
		"count": 5
	},
	1:{
		"name": "Roberto",
		"skills": "CSS",
		"count": 10
	},
	2:{
		"name": "Mica",
		"skills": "JS",
		"count": 2
	},
	3:{
		"name": "Matias",
		"skills": "CSS",
		"count": 2
	}
}

# Create Empty CSV
file="/content/drive/My Drive/result/result4.csv"
csv=open(file, "w")
headersTitles="index, name, skills, count \n"
csv.write(headersTitles)

# Fill rows for CSV
for i in data.keys():

	name 	= data[i]['name']
	skills= data[i]['skills']
	count   = data[i]['count']
	filas   = str(i) + "," + name + "," + skills + "," + str(count) + "\n"

	csv.write(filas)

# Read CSV to create dataFrame for graphic
datos=pd.read_csv(file)
df=pd.DataFrame({
    'name':['Ana','Braulio','Carlos','Ana','Ana'],
    'skills':['HTML','CSS','JS','CSS','CSS'],
    'count':[1,1,1,1,1]
})
print(df)

# Render graphic
df.groupby(['name','skills'])['count'].size().unstack().plot(kind='bar',stacked=True, title='Skills')
plt.ylabel('Count')
plt.show()

# df.plot(kind='bar', title='Skills')


# {
#     'index':[0,1,2],
#     'name':['Ana','Braulio','Carlos'],
#     'skills':['HTML','CSS','JS'],
#     'count':[20,10,50]
# }