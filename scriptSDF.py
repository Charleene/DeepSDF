from mesh_to_sdf import sample_sdf_near_surface

import trimesh
import pyrender
import numpy as np
import argparse, sys, os
from numpy import asarray
from numpy import save

parser = argparse.ArgumentParser(description='Renders given obj file by rotation a camera around it.')
parser.add_argument(
    '--points_number', type=int, default=150000,
    help='number of points to be computed')
parser.add_argument(
    'obj', type=str,
    help='Path to the obj file to be rendered.')
parser.add_argument(
    '--output_folder', type=str, default='/tmp',
    help='The path the output will be dumped to.')

argv = sys.argv[sys.argv.index("--") + 1:]
args = parser.parse_args(argv)

mesh = trimesh.load(args.obj)

points, sdf = sample_sdf_near_surface(mesh, number_of_points=int(args.points_number))

# Save to npy file
os.makedirs(args.output_folder, exist_ok=True)

save(os.path.join(os.path.abspath(args.output_folder), 'sdf.npy'), sdf)
save(os.path.join(os.path.abspath(args.output_folder), 'pos.npy'), points)

# Display on GUI
#colors = np.zeros(points.shape)
#colors[sdf < 0, 2] = 1
#colors[sdf > 0, 0] = 1
#cloud = pyrender.Mesh.from_points(points, colors=colors)
#scene = pyrender.Scene()
#scene.add(cloud)
#viewer = pyrender.Viewer(scene, use_raymond_lighting=True, point_size=2)