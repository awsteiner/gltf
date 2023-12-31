import bpy
import os.path
import numpy

bpy.ops.import_scene.gltf(filepath='/Users/awsteiner2/wcs/int9/bayes/test.gltf')

# Scene variables
scn=bpy.context.scene
cam=scn.camera

output_path=scn.render.filepath
cam.rotation_mode='XYZ'
scn.world.node_tree.nodes["Background"].inputs[0].default_value=(0,0,0,0)

# Iterate through the dict, set the locations and render
for i in range(0,20):
    
    ang=numpy.pi*2.0/20.0*i
    x=3.8*numpy.cos(ang)
    y=3.8*numpy.sin(ang)
    
    # Set the camera location
    cam.location=[x+0.5,y+0.5,0.5]
    cam.rotation_euler=[numpy.pi/2.0,0,numpy.pi/2.0+ang]
    print([x,y,0.5])
    print([numpy.pi/2.0,0,ang+numpy.pi/2.0])
    
    # Assemble the path (.png is a placeholder)
    scn.render.filepath=os.path.join(output_path,"cam_{}.png".format(i))
    
    # Call the render operator
    bpy.ops.render.render(write_still=True)

# Reset the output path to "/tmp/"
bpy.context.scene.render.filepath=output_path

