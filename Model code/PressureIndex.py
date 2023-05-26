# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:10:47
"""
import arcpy
from sys import argv

def PressureIndex(new_all_surf_spots_pressure="new_all_surf_spots_pressure", normalized_pressure_1_csv="normalized_pressure (1).csv"):  # PressureIndex

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False


    # Process: Pressure Index Join Field (Join Field) (management)
    Pressure_Index = arcpy.management.JoinField(in_data=new_all_surf_spots_pressure, in_field="id", join_table=normalized_pressure_1_csv, join_field="id", fields=["normalized_built_area", "normalized_human_mod", "normalized_pop_change", "normalized_ports", "normalized_roads", "added_pressure", "pressure_index"])[0]

    return Pressure_Index

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        PressureIndex(*argv[1:])