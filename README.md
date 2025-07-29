# L.A. Noire_obj2mesh
**This script lets you swap the main menu text in L.A. Noire for any model you want**

On PC, the main menu is just a static image. But in the original console version, it was animated: like a shadow on a wall that changed when selecting options, moving, as if switching slides. This wasn't done with textures or fonts, but with 3D models. 

This script takes a flat 3D model from an OBJ file and inserts it into the PS4 version’s model file. This way, you can replace game files to translate the menu into another language or even replace text with an image.

## Usage:

python LANoire_obj2mesh.py obj_file mesh_file

## Example:

python LANoire_obj2mesh.py test.obj text_continue.normal_lod.chunk

## Notes:
The OBJ file template made in Blender is included. Replace the text with your own and convert it to a mesh.

For some unknown reason, the "NEW" menu line has a different vertex stride than all the others. To convert the "NEW" file, change the "stride" variable from 0x18 to 0x14.  

The script can only replace a model with the same (or fewer) vertices/faces as the original. If you try to convert a mesh with more vertices or faces, the script will give an error message and stop. In that case, reduce the number of vertices or polygons and try again.

