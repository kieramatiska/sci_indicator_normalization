# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:11:27
"""
import arcpy
from sys import argv

def MarineEcosystemWeighted(all_spots_unverified_Buffer_marine_ecosystem="all_spots_unverified_Buffer_marine_ecosystem", normalized_seagrass="Biodiversity SubIndex Variables\\normalized_seagrass", normalized_mangrove="Biodiversity SubIndex Variables\\normalized_mangrove", normalized_coral_reef="Biodiversity SubIndex Variables\\normalized_coral_reef"):  # MarineEcosystemWeighted

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    Field_Type = "DOUBLE"
    Field_Type_2_ = "DOUBLE"

    # Process: Mangrove Join Field (Join Field) (management)
    mangrove_join = arcpy.management.JoinField(in_data=all_spots_unverified_Buffer_marine_ecosystem, in_field="ID", join_table=normalized_mangrove, join_field="ID", fields=["normalized_mangrove"])[0]

    # Process: Seagrass Join Field (Join Field) (management)
    seagrass_join = arcpy.management.JoinField(in_data=mangrove_join, in_field="ID", join_table=normalized_seagrass, join_field="ID", fields=["normalized_seagrass"])[0]

    # Process: All Marine Ecosystems Join Field (Join Field) (management)
    all_marine_ecosystems_join = arcpy.management.JoinField(in_data=seagrass_join, in_field="ID", join_table=normalized_coral_reef, join_field="ID", fields=["normalized_coral_reef"])[0]

    # Process: Added Marine Ecosystems Calculate Field (Calculate Field) (management)
    added_marine_ecosystems_values = arcpy.management.CalculateField(in_table=all_marine_ecosystems_join, field="added_marine", expression="!normalized_mangrove! + !normalized_seagrass! + !normalized_coral_reef!", expression_type="PYTHON3", code_block="", field_type=Field_Type)[0]

    # Process: Normalized Marine Ecosystems Scores Calculate Field (Calculate Field) (management)
    normalized_marine_ecosystesm_score = arcpy.management.CalculateField(in_table=added_marine_ecosystems_values, field="normalized_marine_ecosystem", expression="!added_marine! / 1.906572", expression_type="PYTHON3", code_block="", field_type=Field_Type_2_)[0]

    return normalized_marine_ecosystesm_score

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        MarineEcosystemWeighted(*argv[1:])
