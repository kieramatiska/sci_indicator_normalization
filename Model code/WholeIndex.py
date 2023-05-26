# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:13:59
"""
import arcpy
from sys import argv

def WholeIndex(all_spots_unverified_Buffer_complete="all_spots_unverified_Buffer_complete", Biodiversity_SubIndex="Biodiversity SubIndex", Social_SubIndex="Social SubIndex", Response_Index="Response Index", Surf_SubIndex="Surf SubIndex"):  # WholeIndex

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    Field_Type = "DOUBLE"
    Field_Type_2_ = "DOUBLE"
    Field_Type_3_ = "DOUBLE"

    # Process: Biodiversity Join Field (Join Field) (management)
    biodiversity_join = arcpy.management.JoinField(in_data=all_spots_unverified_Buffer_complete, in_field="ID", join_table=Biodiversity_SubIndex, join_field="ID", fields=["normalized_biodiversity"])[0]

    # Process: Social Join Field (Join Field) (management)
    social_join = arcpy.management.JoinField(in_data=biodiversity_join, in_field="ID", join_table=Social_SubIndex, join_field="ID", fields=["normalized_social_values"])[0]

    # Process: Response Join Field (Join Field) (management)
    response_join = arcpy.management.JoinField(in_data=social_join, in_field="ID", join_table=Response_Index, join_field="ID", fields=["normalized_response"])[0]

    # Process: All Normalized Join Field (Join Field) (management)
    all_normalized_join = arcpy.management.JoinField(in_data=response_join, in_field="ID", join_table=Surf_SubIndex, join_field="ID", fields=["pressure_index", "normalized_overlapping_spots"])[0]

    # Process: Added Normalized Scores Calculate Field (Calculate Field) (management)
    added_normalized_values = arcpy.management.CalculateField(in_table=all_normalized_join, field="added_normalized_values", expression="!normalized_overlapping_spots! + !pressure_index! + !normalized_response! + !normalized_social_values! + !normalized_biodiversity!", expression_type="PYTHON3", code_block="", field_type=Field_Type)[0]

    # Process: Subtracted Normalized Values Calculate Field (Calculate Field) (management)
    subtracted_normalized_values = arcpy.management.CalculateField(in_table=added_normalized_values, field="Subtracted_normalized", expression="!added_normalized_values! - 0.927685", expression_type="PYTHON3", code_block="", field_type=Field_Type_2_)[0]

    # Process: Whole Model Normalized Calculate Field (Calculate Field) (management)
    whole_model_normalized = arcpy.management.CalculateField(in_table=subtracted_normalized_values, field="whole_index_normalized", expression="!Subtracted_normalized! / 2.034034", expression_type="PYTHON3", code_block="", field_type=Field_Type_3_)[0]

    return whole_model_normalized

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        WholeIndex(*argv[1:])
