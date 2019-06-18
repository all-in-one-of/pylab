import unreal

directory_path = "/Game/Content"
directory = unreal.EditorAssetLibrary()

def makeDirectory():
    if directory.does_directory_exist == True:
        print str(directory_path)+' already exists'
    else:
        directory.make_directory(directory_path)
        print str(directory_path)+' created'

makeDirectory()
