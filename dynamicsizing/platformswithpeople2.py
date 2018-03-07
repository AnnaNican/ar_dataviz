import bpy
import bmesh
from __future__ import division
import math

global x, y

bpyscene = bpy.context.scene #create scene
humanpath = '/Users/anna.nicanorova/Annalect/repos/prototypes_2017/holograms/dynamicsizing/iron-man.fbx'
humanname = 'Ironman' #the way it's name as original


groupname = 'hightech'
scaledvalue = 9 #subtract one from original

def create_platfrom(name, size):
	x = 0 
	y = 0
	newx = x + size
	newy = y + size
	verts = [(x,y,0),(x,newy,0),(newx,newy,0),(newx,y,0)]
	faces = [(0,1,2,3)]
	mymesh = bpy.data.meshes.new(name)
	myobject = bpy.data.objects.new(name, mymesh) 
	myobject.location = bpy.context.scene.cursor_location
	bpy.context.scene.objects.link(myobject)
	mymesh.from_pydata(verts,[],faces)
	mymesh.update(calc_edges=True)

create_platfrom(groupname, 2.54)

peoplecounter = 0
def create_people(groupname, numberpeople, size, peoplecounter):
	############
	#create first object
	peoplecounter += 1
	objectsize = size/3-(0.2*2)
	x = objectsize 
	y = objectsize
	bpy.ops.import_scene.fbx("EXEC_DEFAULT", filepath= humanpath) #create first human
	bpy.context.scene.objects.active = bpy.data.objects[humanname]
	for obj in bpy.context.selected_objects:
		obj.name = str(groupname + '1')
	obj = bpy.data.objects[str(groupname + '1')]
	obj.scale = (objectsize, objectsize, objectsize) #resize
	obj.location = (x, y, 0) #move
	while peoplecounter<numberpeople:
		peoplecounter += 1
		#select 1st object
		bpy.context.scene.objects.active = bpy.data.objects[groupname + '1']
		human_mesh = bpy.context.object.data # use current object's data
		human_mesh_copy = human_mesh.copy()
		obj = bpy.data.objects.new(str((groupname + str(peoplecounter))), human_mesh_copy)
		#calculate right position : if not divisible by 3, then keep the same y, and add only to x, otherwise, reset x and add to y
		if peoplecounter % 3 ==1:
			x = objectsize
			y = y + objectsize + 0.2
		else:
			x = x + objectsize + 0.2
		obj.location = (x,y,0)
		bpyscene.objects.link(obj)
		bpyscene.update()
		obj.scale = (objectsize, objectsize, objectsize) #resize

create_people(groupname, scaledvalue, 2.54, 0)


def createmetadata(groupname, website, audiencesize):
bpyscene.cursor_location = (0.0, 0.0, 0.0)
x = 0 
y = 0
z = 2*size
name = str(groupname+ '_meta')
newx = x + size
newy = y + size
verts = [(x,y,z),(x,newy,z),(newx,newy,z),(newx,y,z)]
faces = [(0,1,2,3)]
mymesh = bpy.data.meshes.new(name)
myobject = bpy.data.objects.new(name, mymesh) 
myobject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myobject)
mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)
#need to reset local

bpy.ops.object.text_add(location=(i*1.05, 0, 3.0), rotation=(0, 0, 0))
    tx=bpy.context.object
    tx.name = 'Letter_{}'.format(c)
    tx.data.body = c
    tx.data.font = fnt
    tx.location=(i*1.05, 0.0, 1.0)

def groupobjectsandmove():
	# group objects and move platform



# for everyadueicne :
	

