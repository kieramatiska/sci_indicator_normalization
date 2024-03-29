# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:13:47
"""
import arcpy
from sys import argv

def ResponseIndex(new_all_surf_spots_response="new_all_surf_spots_response", normalized_response_1_csv="normalized_response (1).csv"):  # ResponseIndex

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False


    # Process: Join Field (Join Field) (management)
    Response_Index = arcpy.management.JoinField(in_data=new_all_surf_spots_response, in_field="id", join_table=normalized_response_1_csv, join_field="id", fields=["normalized_heritage", "normalized_priority", "normalized_wsr", "normalized_protected", "normalized_bandeira", "normalized_ramsar", "response_added", "response_index"])[0]

    return Response_Index

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        ResponseIndex(*argv[1:])
