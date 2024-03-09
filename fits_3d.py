#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:02:03 2024

@author: mrodruck
"""

import numpy as np
from stl import mesh

from astropy.io import fits
image = fits.getdata("exo_img.fit")/10

image = image - np.median(image) / 2

image = image[333:398,708:808]/10



vertices = []
faces = []
i = 0
#loop over each vertex, increasing by 1 step in 'x' each time
for row in range(image.shape[0]):
    for col in range(image.shape[1]):
       vertices.extend([
           [-1 + 2 * row, -1 + 2 * col, 0], #bottom of cube is at 0
           [+1 + 2 * row, -1 + 2 * col, 0],
           [+1 + 2 * row, +1 + 2 * col, 0],
           [-1 + 2 * row, +1 + 2 * col, 0],
           [-1 + 2 * row, -1 + 2 * col, image[row,col]], #height of cube
           [+1 + 2 * row, -1 + 2 * col, image[row,col]],
           [+1 + 2 * row, +1 + 2 * col, image[row,col]],
           [-1 + 2 * row, +1 + 2 * col, image[row,col]]])
       faces.extend([
               [0 + 8 * (i),3 + 8 * (i),1 + 8 * (i)], #creates faces for each cube
               [1 + 8 * (i),3 + 8 * (i),2 + 8 * (i)],
               [0 + 8 * (i),4 + 8 * (i),7 + 8 * (i)],
               [0 + 8 * (i),7 + 8 * (i),3 + 8 * (i)],
               [4 + 8 * (i),5 + 8 * (i),6 + 8 * (i)],
               [4 + 8 * (i),6 + 8 * (i),7 + 8 * (i)],
               [5 + 8 * (i),1 + 8 * (i),2 + 8 * (i)],
               [5 + 8 * (i),2 + 8 * (i),6 + 8 * (i)],
               [2 + 8 * (i),3 + 8 * (i),6 + 8 * (i)],
               [3 + 8 * (i),7 + 8 * (i),6 + 8 * (i)],
               [0 + 8 * (i),1 + 8 * (i),5 + 8 * (i)],
               [0 + 8 * (i),5 + 8 * (i),4 + 8 * (i)]])
       i += 1

    


#converts array to mesh
mesh_data = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        mesh_data.vectors[i][j] = vertices[face[j]]

# Write the mesh to file
mesh_data.save('testimg_4.stl')