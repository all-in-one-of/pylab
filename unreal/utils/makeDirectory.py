import unreal
import json

project_name = "001_Test" 
prefix = ["SE", "SV"]
sub_directories = ["materials", "textures", "meshes", "blueprints"]

directory = unreal.EditorAssetLibrary()
directory_path = "/Game/" + prefix[0] + project_name

level = unreal.EditorLevelLibrary()
level_name = directory_path + prefix[1] + project_name

def make_directory():
    does_exist = True
    if directory.does_directory_exist == does_exist:
        print(str(directory_path) + ' already exists')
    else:
        directory.make_directory(directory_path)
        level.new_level(level_name)
        for i in sub_directories:
            directory.make_directory(directory_path)
        does_exist = True
        print(str(directory_path) + ' created')

# def make_level():
#     directory_exists = True
#     if directory.does_directory_exist == directory_exists:
#         level.new_level(level_name)
#     else:
#         level.new_level(directory_path) 
#         print(str(directory_path) + ' created')



make_directory()
