import sys

def main():
    from struct import unpack, pack
    if len(sys.argv) != 3:
        print("Usage: LANoire_obj2mesh.py obj_file mesh_file")
        return

    obj_file = sys.argv[1]
    chunk_file = sys.argv[2]
    
    stride = 0x18
    face_count = 0
    vert_count = 0

    with open(chunk_file, "rb+") as f:
        
        f.read(8)
        vert_offset = unpack('<i', f.read(4))[0]
        f.seek(0x240)
        vert_size = unpack('<i', f.read(4))[0]
        face_offset = vert_offset + vert_size
        f.read(12)
        f.read(4)  # face size
        max_vert = unpack('<i', f.read(4))[0]
        max_face = unpack('<i', f.read(4))[0]

        # fill faces with 0s
        f.seek(face_offset)
        for _ in range(max_face):
            f.write(pack('<hhh', 0, 0, 0))

        with open(obj_file, 'r') as fo:
            while True:
                line = fo.readline()
                if not line:
                    break
                parts = line.strip().split(' ')
            
                if parts[0] == 'f':
                    indices = []
                    for p in parts[1:]:
                        idx = p.split('/')[0]
                        index_value = int(idx) - 1
                        indices.append(index_value)
                
                    if face_count >= max_face:
                        print(f"Error. Too many faces. Max = {max_face}")
                        return
                    
                    f.seek(face_offset + face_count * 6)
                    f.write(pack('<hhh', indices[0], indices[1], indices[2]))
                    face_count += 1
                
                elif parts[0] == 'v':
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                
                    if vert_count >= max_vert:
                        print(f"Error. Too many vertices. Max = {max_vert}")
                        return
                
                    f.seek(vert_offset + vert_count * stride)
                    f.write(pack('<hh', int(x*256), int(y*256)))
                    vert_count += 1

    print(f"Mesh convert OK.")

if __name__ == "__main__":
    main()
