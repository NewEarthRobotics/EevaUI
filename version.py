
current_gui_version = 6

# compatible versions of GUI (keys) and robot firmwares (values)
compatible_versions = {
    1 : [1],
    2 : [2],
    3 : [3, 4],
    4 : [5],
    5 : [6],
    6 : [7]
    }

# Return list of GUI versions that are compatible for a given firmware version
def list_compatible_gui_versions(firmware_version):
    compatible_gui_versions = []
    for gversion, fversions in compatible_versions.iteritems():
        if firmware_version in fversions:
            compatible_gui_versions.append(gversion)
    
    return compatible_gui_versions

assert current_gui_version in compatible_versions.keys()