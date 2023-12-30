import bpy
import os.path

camera_locations = {
    0: (2.576395273208618, -4.465750694274902, 1.094475507736206),
    1: (-0.573695343202619, -1.863753624223357, 1.094235453632562)
}

bpy.ops.import_scene.gltf(filepath='/Users/awsteiner2/wcs/int9/bayes/test.gltf')

# Scene variables
scn = bpy.context.scene
cam = scn.camera
output_path = scn.render.filepath

# Iterate through the dict, set the locations and render
for k, v in camera_locations.items():
    # Set the locations
    cam.location = v
    # Assemble the path (.jpg is a placeholder)
    scn.render.filepath = os.path.join(output_path, "cam_{}.jpg".format(k))
    # Call the render operator
    bpy.ops.render.render(write_still=True)

# Reset the output path to "/tmp/"
bpy.context.scene.render.filepath = output_path
