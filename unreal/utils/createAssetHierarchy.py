import unreal

asset_name = "BP_Actor"
asset_directory = "/Game/Content"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)

def makeBPActor():
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    my_new_asset = asset_tools.create_asset(asset_name, asset_directory, None, factory)

    unreal.EditorAssetLibrary.save_loaded_asset(my_new_asset)

makeBPActor()