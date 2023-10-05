import numpy as np
import pygltflib

points = np.array(
    [
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5],
        [0.5, -0.5, -0.5],
        [-0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
    ],
    dtype="float32",
)
triangles = np.array(
    [
        [0, 1, 2],
        [3, 2, 1],
        [1, 0, 4],
        [5, 4, 0],
        [3, 1, 6],
        [4, 6, 1],
    ],
    dtype="uint8",
)
triangles2 = np.array(
    [
        [2, 3, 7],
        [6, 7, 3],
        [0, 2, 5],
        [7, 5, 2],
        [5, 7, 4],
        [6, 4, 7],
    ],
    dtype="uint8",
)

triangles_binary_blob = triangles.flatten().tobytes()
triangles2_binary_blob = triangles2.flatten().tobytes()
points_binary_blob = points.tobytes()

gltf = pygltflib.GLTF2(
    scene=0,
    scenes=[pygltflib.Scene(nodes=[0,1])],
    nodes=[pygltflib.Node(mesh=0),
           pygltflib.Node(mesh=1)],
    textures=[pygltflib.Texture(source=0)],
    materials=[
        pygltflib.Material(
            alphaMode=pygltflib.MASK,
            pbrMetallicRoughness=
            pygltflib.PbrMetallicRoughness(baseColorFactor=[0,1,0,1])
        ),
        pygltflib.Material(
            alphaMode=pygltflib.MASK,
            pbrMetallicRoughness=
            pygltflib.PbrMetallicRoughness(baseColorFactor=[1,0,0,1],
                                           baseColorTexture=
                                           pygltflib.TextureInfo(index=0,texCoord=0)
                                           )
        )
    ],
    meshes=[
        pygltflib.Mesh(
            primitives=[
                pygltflib.Primitive(
                    material=0,
                    indices=0,
                    attributes=pygltflib.Attributes(POSITION=2)
                )
            ]
        ),
        pygltflib.Mesh(
            primitives=[
                pygltflib.Primitive(
                    material=1,
                    indices=1,
                    attributes=pygltflib.Attributes(POSITION=2,
                                                    TEXCOORD_0=1)
                )
            ]
        )
    ],
    accessors=[
        pygltflib.Accessor(
            bufferView=0,
            componentType=pygltflib.UNSIGNED_BYTE,
            count=triangles.size,
            type=pygltflib.SCALAR,
            max=[int(triangles.max())],
            min=[int(triangles.min())],
        ),
        pygltflib.Accessor(
            bufferView=1,
            componentType=pygltflib.UNSIGNED_BYTE,
            count=triangles2.size,
            type=pygltflib.SCALAR,
            max=[int(triangles2.max())],
            min=[int(triangles2.min())],
        ),
        pygltflib.Accessor(
            bufferView=2,
            componentType=pygltflib.FLOAT,
            count=len(points),
            type=pygltflib.VEC3,
            max=points.max(axis=0).tolist(),
            min=points.min(axis=0).tolist(),
        ),
    ],
    bufferViews=[
        pygltflib.BufferView(
            buffer=0,
            byteLength=len(triangles_binary_blob),
            target=pygltflib.ELEMENT_ARRAY_BUFFER,
        ),
        pygltflib.BufferView(
            buffer=0,
            byteOffset=len(triangles_binary_blob),
            byteLength=len(triangles2_binary_blob),
            target=pygltflib.ELEMENT_ARRAY_BUFFER,
        ),
        pygltflib.BufferView(
            buffer=0,
            byteOffset=len(triangles_binary_blob)+len(triangles2_binary_blob),
            byteLength=len(points_binary_blob),
            target=pygltflib.ARRAY_BUFFER,
        ),
    ],
    buffers=[
        pygltflib.Buffer(
            byteLength=len(triangles_binary_blob)+
            len(triangles2_binary_blob)+
            len(points_binary_blob)
        )
    ],
)
gltf.set_binary_blob(triangles_binary_blob+triangles2_binary_blob+
                     points_binary_blob)

image=pygltflib.Image()
image.uri="texture.png"
gltf.images.append(image)
gltf.convert_images(pygltflib.ImageFormat.DATAURI)

# save to file
gltf.save("test7.gltf")
gltf.save("test7.glb")
