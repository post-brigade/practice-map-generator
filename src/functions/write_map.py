

def write_map(map: str, map_path: str):
     with open(map_path, "x") as file:
         file.write(map)
