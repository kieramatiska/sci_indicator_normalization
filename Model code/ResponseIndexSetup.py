# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:13:33
"""
import arcpy
from sys import argv

def ResponseIndexSetup(Protected_Area_MMA_2022_Clipped="Response Index Variables\\Protected_Area_MMA_2022__Clipped", ramsar_clipped_="Response Index Variables\\ramsar_clipped_", RB_Mata_Atlantica="Response Index Variables\\RB_Mata_Atlantica", world_heritage_combined="Response Index Variables\\world_heritage_combined", guarda_wsr_="Response Index Variables\\guarda_wsr_", bandeira_azul_="Response Index Variables\\bandeira_azul_", world_heritage_percent_area="G:\\Brazil_SCI\\Brazil_SCI.gdb\\world_heritage_surf_area", protected_atl_forest_percent_area="G:\\Brazil_SCI\\Brazil_SCI.gdb\\priority_atlantic_forest_surf_area", wsr_percent_area="G:\\Brazil_SCI\\Brazil_SCI.gdb\\wsr_surf_area", protected_percent_area="G:\\Brazil_SCI\\Brazil_SCI.gdb\\protected_surf_area", ramsar_percent_area="G:\\Brazil_SCI\\Brazil_SCI.gdb\\ramsar_surf_area", bandeira_azul_buffer="G:\\Brazil_SCI\\Brazil_SCI.gdb\\bandeira_surf_spots", response_1km_buffer="response_1km_buffer", response_1km_buffer_3_="response_1km_buffer", response_1km_buffer_4_="response_1km_buffer"):  # ResponseIndexSetup

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Analysis Tools.tbx")
    Field_Type_2_ = "DOUBLE"
    Field_Type_3_ = "DOUBLE"
    Field_Type = "DOUBLE"
    Field_Type_8_ = "DOUBLE"
    Field_Type_10_ = "DOUBLE"

    # Process: Protected Area Buffer Summarize Within (Summarize Within) (analysis)
    protected_buffer = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\protected_surf_area"
    Output_Grouped_Table_2_ = ""
    arcpy.analysis.SummarizeWithin(in_polygons=response_1km_buffer_3_, in_sum_features=Protected_Area_MMA_2022_Clipped, out_feature_class=protected_buffer, keep_all_polygons="KEEP_ALL", sum_fields=[], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREKILOMETERS", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table_2_)

    # Process: RAMSAR Buffer Summarize Within (Summarize Within) (analysis)
    ramsar_buffer = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\ramsar_surf_area"
    Output_Grouped_Table_3_ = ""
    arcpy.analysis.SummarizeWithin(in_polygons=response_1km_buffer_4_, in_sum_features=ramsar_clipped_, out_feature_class=ramsar_buffer, keep_all_polygons="KEEP_ALL", sum_fields=[], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREKILOMETERS", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table_3_)

    # Process: Protected Percent Area Calculate Field (Calculate Field) (management)
    protected_percent_area = arcpy.management.CalculateField(in_table=protected_buffer, field="protected_percent_area", expression="!SUM_Area_SQUAREKILOMETERS! / (!Shape_Area! / 1000000)", expression_type="PYTHON3", code_block="", field_type=Field_Type_2_)[0]

    # Process: RAMSAR Percent Area Calculate Field (Calculate Field) (management)
    ramsar_percent_area = arcpy.management.CalculateField(in_table=ramsar_buffer, field="ramsar_percent_area", expression="!SUM_Area_SQUAREKILOMETERS! / (!Shape_Area! / 1000000)", expression_type="PYTHON3", code_block="", field_type=Field_Type_3_)[0]

    # Process: WSR Summarize Within (Summarize Within) (analysis)
    wsr_buffer = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\wsr_surf_area"
    Output_Grouped_Table = ""
    arcpy.analysis.SummarizeWithin(in_polygons=response_1km_buffer_3_, in_sum_features=guarda_wsr_, out_feature_class=wsr_buffer, keep_all_polygons="KEEP_ALL", sum_fields=[], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREKILOMETERS", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table)

    # Process: WSR Percent Area Calculate Field (Calculate Field) (management)
    wsr_percent_area = arcpy.management.CalculateField(in_table=wsr_buffer, field="wsr_percent_area", expression="!SUM_Area_SQUAREKILOMETERS! / (!Shape_Area! / 1000000)", expression_type="PYTHON3", code_block="", field_type=Field_Type)[0]

    # Process: Protected Atlantic Forest Summarize Within (Summarize Within) (analysis)
    protected_atlantic_forest_buffer = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\priority_atlantic_forest_surf_area"
    Output_Grouped_Table_4_ = ""
    arcpy.analysis.SummarizeWithin(in_polygons=response_1km_buffer, in_sum_features=RB_Mata_Atlantica, out_feature_class=protected_atlantic_forest_buffer, keep_all_polygons="KEEP_ALL", sum_fields=[], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREKILOMETERS", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table_4_)

    # Process: Protected Atl Forest Percent Area Calculate Field (Calculate Field) (management)
    protected_atl_forest_percent_area = arcpy.management.CalculateField(in_table=protected_atlantic_forest_buffer, field="protected_atl_forest_area", expression="!SUM_Area_SQUAREKILOMETERS! / (!Shape_Area! / 1000000)", expression_type="PYTHON3", code_block="", field_type=Field_Type_8_)[0]

    # Process: World Heritage Summarize Within (Summarize Within) (analysis)
    world_heritage_buffer = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\world_heritage_surf_area"
    Output_Grouped_Table_5_ = ""
    arcpy.analysis.SummarizeWithin(in_polygons=response_1km_buffer, in_sum_features=world_heritage_combined, out_feature_class=world_heritage_buffer, keep_all_polygons="KEEP_ALL", sum_fields=[], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREKILOMETERS", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table_5_)

    # Process: World Heritage Percent Area Calculate Field (Calculate Field) (management)
    world_heritage_percent_area = arcpy.management.CalculateField(in_table=world_heritage_buffer, field="world_heritage_percent_area", expression="!SUM_Area_SQUAREKILOMETERS! / (!Shape_Area! / 1000000)", expression_type="PYTHON3", code_block="", field_type=Field_Type_10_)[0]

    # Process: Bandeira Azul Spatial Join (Spatial Join) (analysis)
    arcpy.analysis.SpatialJoin(target_features=response_1km_buffer_4_, join_features=bandeira_azul_, out_feature_class=bandeira_azul_buffer, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="", match_option="INTERSECT", search_radius="", distance_field_name="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        ResponseIndexSetup(*argv[1:])
