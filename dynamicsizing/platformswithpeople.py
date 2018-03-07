# dynamic platfroms


# take a csv with data
# calculate how many platforms to create -> size them accordingly
# Create. platforms in blender

#now size populations and decided how many humans to create
# refferencing another template with blender check - like superwamn/batman

# now for every platform create tablet on top and create dynamic text metadata
# export as a file and pass to unity


# programmatically open as a unity object?

import bpy
import bmesh
from __future__ import division
import math
import pandas as pd

bpyscene = bpy.context.scene #create scene

df = pd.read_csv('./data/samplesizing_sectors.csv')

def normalize(valuescolumn, data):
	values = data[valuescolumn].tolist()
	scaled = [float(i)/max(values) for i in values]
	data["scaled"] = (pd.Series(scaled)).values
	data.loc[:,'scaled'] *= 3 #multiple all values by 3, since max size of object is going to be 3
	return data

normalize('active_audience', df)

def calculateplatforms():
	'''currently works for only one row of platforms '''
global platform_side
audiences = list(df.audience.unique())	
#considering the platform is 16 blocks -2 for margins so working with space 14*14 = 196
xplatform = 14/(len(audiences)+ 0.5*(len(audiences)-1))
#yplatform = #if platforms fir into 1 row, then loose margins, if not, create multiple rows
Yplatform = xplatform
size = 14/(len(audiences)+ 0.5*(len(audiences)-1))
platform_side = size

x = -7
y = -7


def createplatforms(name, size):
	global x, y
	newx = x + size
	newy = y + size
	#
	#Define vertices and faces
	verts = [(x,y,0),(x,newy,0),(newx,newy,0),(newx,y,0)]
	faces = [(0,1,2,3)]
	 #
	# Define mesh and object variables
	mymesh = bpy.data.meshes.new(name)
	myobject = bpy.data.objects.new(name, mymesh)  
	 #
	#Set location and scene of object
	myobject.location = bpy.context.scene.cursor_location
	bpy.context.scene.objects.link(myobject)
	 #
	#Create mesh
	mymesh.from_pydata(verts,[],faces)
	mymesh.update(calc_edges=True)
	#update new coordinate
	x = x + size + 0.5
	y = y + size + 0.5

createplatforms('test', 2.54)
createplatforms('test2', 2.54)
createplatforms('test3', 2.54)

x = 0 
y = 0
newx = x + size
newy = y + size
name = 'test'

verts = [(x,y,0),(x,newy,0),(newx,newy,0),(newx,y,0)]
faces = [(0,1,2,3)]
mymesh = bpy.data.meshes.new(name)
myobject = bpy.data.objects.new(name, mymesh) 
myobject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myobject)
mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)


# bpy.ops.wm.append(filename='batman.blend', directory='./')

# blendfile = '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/batman.blend'
# # section   = '\\BatmanArmoured_root\\'
# objects    = ['BatmanArmoured_root'] ###<-- Add the name of objects you want to append

# directory = blendfile #+ section

# for obj in objects:  
#     filename  = obj
#     bpy.ops.wm.append(filename=filename, directory=directory)

# with bpy.data.libraries.load("./batman.blend") as (df, dt):
# 	dt.groups = ['BatmanArmoured_root']

# filepath = '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/batman.blend'
# with bpy.data.libraries.load(filepath) as (data_from, data_to):
#     data_to.meshes = data_from.meshes


# import bpy
# scn = bpy.context.scene
# filepath = "/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/batman.blend"

# #append object from .blend file
# with bpy.data.libraries.load(filepath) as (data_from, data_to):
#     data_to.objects = data_from.objects

# #link object to current scene
# for obj in data_to.objects:
#     if obj is not None:
#         scn.objects.link(obj)

# bpy.ops.wm.open_mainfile('/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/batman.blend')

# bpy.ops.import_scene.fbx(filepath = 'batman.fbx', directory= '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/dynamicsizing/')

bpy.ops.import_scene.fbx("EXEC_DEFAULT", filepath= '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/dynamicsizing/batman.fbx')
bpy.ops.import_scene.fbx("EXEC_DEFAULT", filepath= '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/dynamicsizing/iron-man.fbx')
obj = bpy.data.objects['Bip01_LCalfTwist1.001']
obj = bpy.data.objects['Ironman']
# obj.scale = (0.5, 0.5, 0.5) # will return all dimensions to their original value obj.scale = (1, 1, 1) 


def calculatepeople
#just round the scale to nearest one & size to fit the square

# devide the platform into equal sizes
platform_side = size
objectsize = platform_side/3
# objectsize = 0.8484848484848485
obj.scale = (objectsize, objectsize, objectsize)
obj.scale = (0.2, 0.2, 0.2)


#wird response to object group
obj = bpy.data.objects['Ironman']
obj.location = (objectsize, objectsize, 0)


anotherhex = obj.copy()
anotherhex.location = (2*objectsize, 2*objectsize, 0)


if morethanoneperson:
superhero = bpy.data.objects['Ironman']
# me = bpy.context.object.data # use current object's data
superhero2 = superhero.copy()
ob = bpy.data.objects.new("Ironman2", superhero2)
ob.location = (2*objectsize, 2*objectsize, 0)


bpy.data.objects['Ironman'].select = True
# to select the object in the 3D viewport,
# this way you can also select multiple objects

# additionally you can use
bpy.context.scene.objects.active = bpy.data.objects['Ironman']
# to make it the active selected object


def createduplicates()

me = bpy.context.object.data # use current object's data
me_copy = me.copy()
ob = bpy.data.objects.new("Mesh Copy", me_copy)
ob.location = (1,2,3)
scene = bpy.context.scene
scene.objects.link(ob)
scene.update()


bpy.context.scene.objects.active = bpy.data.objects['Mesh Copy']
obj = bpy.data.objects['Mesh Copy']
obj.location = (2*objectsize, 2*objectsize, 0)

for obj in bpy.context.selected_objects:
    obj.name = "Test1"



# group_name = "Batman"
# for o in bpy.context.selected_objects:
# 	bpy.data.groups[group_name].objects.link(o)


# list objects
for ob in bpy.data.objects:
    print (ob.name)
    try:
        ob.material_slot_remove()
        print ("removed material from " + ob.name)
    except:
        print (ob.name + " does not have materials.")


batman = bpy.data.objects['Test1']
# me = bpy.context.object.data # use current object's data
batman_copy = obj.copy()

ob = bpy.data.objects.new("Test2", batman_copy)
ob.location = (1,2,3)



#make all batmans as children of the platform
#give the platform the name of target group and 


dynamicobject

drawinblender

createtooltips():
#for the new coordinates - find center


#rewrite pandas to dictionary