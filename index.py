data={
	0:{
		"name": "Matias",
		"lastName": "Campa",
		"count": 5
	},
	1:{
		"name": "Roberto",
		"lastName": "Sanchez",
		"count": 10
	},
	2:{
		"name": "Mica",
		"lastName": "Suares",
		"count": 2
	}
}

archivo="/content/drive/My Drive/result/result.csv"
csv=open(archivo, "w")
tituloR="index, Nombre, Apellido \n"
csv.write(tituloR)


for i in data.keys():

	name 	= data[i]['name']
	lastName= data[i]['lastName']
	count   = data[i]['count']
	filas   = str(i) + "," + name + "," + lastName + ","+ str(count) + "\n"

	csv.write(filas)
	print(filas)

### RENDER MAP ###

datos=pd.read_csv(archivo)
df=pd.DataFrame(datos)

df.plot(kind='bar', title='Skills')
plt.ylabel('Count')
