import unreal

'''
Series of small snippets for querying asset names & paths
'''

DIR_PATH = '/Game/'

# Prints entire AssetData Struct
def printAssetData():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset

# Prints just the asset name
def printAssetName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.asset_name

# Prints the asset class type
def printAssetClass():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.asset_class
    
# Prints the package path of the uassets in DIR_PATH
def printPackagePath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.package_path

# Prints the package name of the uassets in DIR_PATH
def printPackageName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.package_name

# Prints the object path for each uasset in DIR_PATH
def printObjectPath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.object_path
