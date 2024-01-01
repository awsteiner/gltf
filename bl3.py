import bpy
import os.path
import numpy

# Scene variable
scene=bpy.context.scene

# Delete default objects
for o in scene.objects:
    o.select_set(True)
    print('Deleting object named"'+o.name+'".')
    bpy.ops.object.delete()

# Set world background to black
scene.world.node_tree.nodes["Background"].inputs[0].default_value=(0,0,0,0)

# Create camera
camera_data=bpy.data.cameras.new(name='camera')
camera=bpy.data.objects.new('camera',camera_data)
scene.collection.objects.link(camera)
camera.rotation_mode='XYZ'

# Set the camera object as the active camera
scene.camera=camera

# Create lights
light_dist=6

light_data=bpy.data.lights.new(name='light', type='POINT')
light_data.energy=1000
light=bpy.data.objects.new(name='light',object_data=light_data)
bpy.context.collection.objects.link(light)
light.location=(light_dist,light_dist,light_dist)

light_data=bpy.data.lights.new(name='light2', type='POINT')
light_data.energy=1000
light=bpy.data.objects.new(name='light2',object_data=light_data)
bpy.context.collection.objects.link(light)
light.location=(light_dist,-light_dist,light_dist)

light_data=bpy.data.lights.new(name='light3', type='POINT')
light_data.energy=1000
light=bpy.data.objects.new(name='light3',object_data=light_data)
bpy.context.collection.objects.link(light)
light.location=(-light_dist,light_dist,light_dist)

light_data=bpy.data.lights.new(name='light4', type='POINT')
light_data.energy=1000
light=bpy.data.objects.new(name='light4',object_data=light_data)
bpy.context.collection.objects.link(light)
light.location=(-light_dist,-light_dist,light_dist)

# Import GLTF file
bpy.ops.import_scene.gltf(filepath='/Users/awsteiner2/wcs/int9/bayes/test.gltf')

output_path=scene.render.filepath

# Delete default objects
for o in scene.objects:
    print(o.name)
    
# Iterate through the dict, set the locations and render
for i in range(0,20):
    
    ang=numpy.pi*2.0/20.0*i
    x=3.8*numpy.cos(ang)
    y=3.8*numpy.sin(ang)
    
    # Set the camera location
    camera.location=[x+0.5,y+0.5,0.5]
    camera.rotation_euler=[numpy.pi/2.0,0,numpy.pi/2.0+ang]
    print([x,y,0.5])
    print([numpy.pi/2.0,0,ang+numpy.pi/2.0])
    
    # Assemble the path
    scene.render.filepath=os.path.join(output_path,('cam_%02d.png' % i))
    
    # Call the render operator
    bpy.ops.render.render(write_still=True)

# Reset the output path to "/tmp/"
scene.render.filepath=output_path

