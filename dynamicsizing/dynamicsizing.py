import bpy
import bmesh
from __future__ import division
import math
import pandas as pd

bpyscene = bpy.context.scene #create scene

def createobject(relsize, position, name):
	# Create an empty mesh and the object.
	mesh = bpy.data.meshes.new(name)
	basic_cube = bpy.data.objects.new(name, mesh)
	# Add the object into the scene.
	bpyscene.objects.link(basic_cube)
	bpyscene.objects.active = basic_cube
	basic_cube.select = True
	# Construct the bmesh cube and assign it to the blender mesh.
	bm = bmesh.new()
	bmesh.ops.create_cube(bm, size=relsize)
	bm.to_mesh(mesh)
	bm.free()
	#change location
	basic_cube.select = True
	basic_cube.location = position


#def calculatedistance(objectsize, x_axes):
	#alongthesame axis

def calculatesize(dataarray, datavalue):
	x= dataarray
	normalized = (datavalue-min(x))/(max(x)-min(x))*100
	if normalized > 1:
		normalizednew = math.log(normalized)
	else:
		normalizednew = math.log(10)
	return normalizednew

#proportional difference - as a % of the project

rawdata = { "finance": [268100], "manufacturing": [207500], "high tech": [199800] }
rawdatavalues = [268100, 207500, 199800] #create automatically from dictionaty

if __name__ == "__main__":
	xaxes = 0
	for datapoint in rawdata:
		size = calculatesize(rawdatavalues, rawdata[datapoint][0])
		print(size)
		xaxes = xaxes + size + 1
		print(xaxes)
		createobject(size, (xaxes, 0, 0), datapoint)



df = pd.read_csv('./data/sectors.csv')
df1 = pd.read_csv('./data/functions.csv')

def normalize(valuescolumn, data):
	values = data[valuescolumn].tolist()
	scaled = [float(i)/max(values) for i in values]
	data["scaled"] = (pd.Series(scaled)).values
	data.loc[:,'scaled'] *= 3 #multiple all values by 3, since max size of object is going to be 3
	return data

normalize('active_audience', df)
normalize('active_audience', df1)
# normalize(3000, floor, ceiling)
# norm = [float(i)/max(rawdatavalues) for i in rawdatavalues]


createobject(3, (xaxes, 0, 0), 'test1')
createobject(10, (xaxes+1, 0, 0), 'test3')

createobject(3, (-6, -6, 1.5), 'test0')
createobject(2.8, (-1.6, -6, 1.4), 'test1')

def calculate_position(objectsize, objectnumber):
	global position, x, y, globalx, globaly
	x = x + objectsize/2 + 0.5
	if objectnumber == 0:
		y = globaly + objectsize/2
		globaly = globaly + objectsize + 1 #1 accounts for margins
		print globaly
	z = objectsize/2
	position = [x, y, z]
	x = x+objectsize #after position is calculated, add the object for next iteration
	print position, x, globaly

xaxes = -7.5
yaxes = -7.5
startpoint = ()

calculate_position(2.8)

for every data point:
	get size
	calculate position
	create object & name it

globalx = -7.5
globaly = -7.5
x = globalx
for rownum, row in df.iterrows():
	print(row['scaled'])
	if x < 8:
		calculate_position(row['scaled'], rownum)
	else:
		print('reset')
		x = globalx
		y = globaly
		globaly = globaly + row['scaled'] + 1
		calculate_position(row['scaled'], rownum)
	command = str('createobject(' + str(row['scaled'])+ ',' + str(position) + ',\''+ str(row['definition']) + '\')')
	print(command)	
#need to create as doctionary, because blender doesn't understand pandas
