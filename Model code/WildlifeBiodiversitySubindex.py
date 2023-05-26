# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-05-26 15:11:46
"""
import arcpy
from arcpy.sa import *
from sys import argv

def WildlifeBiodiversitySubindex(mammals_corrected="Biodiversity SubIndex Variables\\mammals_corrected", birds_corrected="Biodiversity SubIndex Variables\\birds_corrected", amphi_corrected="Biodiversity SubIndex Variables\\amphi_corrected", terr_rich="G:\\Brazil_SCI\\Brazil_SCI.gdb\\ZonalSt_biodive1", marine_rich="G:\\Brazil_SCI\\Brazil_SCI.gdb\\ZonalSt_biodive2", marine_species_richness_clip="marine_species_richness_clip", biodiversity_5km_buffer="biodiversity_5km_buffer"):  # WildlifeBiodiversitySubindex

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("ImageExt")


    # Process: Average Terr Species Richness Raster Calculator (Raster Calculator) (sa)
    ave_terr_richness = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\ave_terr_richness"
    Average_Terr_Species_Richness_Raster_Calculator = ave_terr_richness
    ave_terr_richness = (mammals_corrected + birds_corrected + amphi_corrected) / 3
    ave_terr_richness.save(Average_Terr_Species_Richness_Raster_Calculator)


    # Process: Change 0 to NODATA Reclassify (Reclassify) (sa)
    ave_terr_reclassified = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\ave_terr_reclassified"
    Change_0_to_NODATA_Reclassify = ave_terr_reclassified
    ave_terr_reclassified = arcpy.sa.Reclassify(in_raster=ave_terr_richness, reclass_field="VALUE", remap="0 NODATA", missing_values="DATA")
    ave_terr_reclassified.save(Change_0_to_NODATA_Reclassify)


    # Process: Average Terr Species Resample (Resample) (management)
    ave_terr_resample = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\ave_terr_resample"
    arcpy.management.Resample(in_raster=ave_terr_reclassified, out_raster=ave_terr_resample, cell_size="1000 1000", resampling_type="NEAREST")
    ave_terr_resample = arcpy.Raster(ave_terr_resample)

    # Process: Terrestrial Species Zonal Statistics as Table (Zonal Statistics as Table) (sa)
    arcpy.sa.ZonalStatisticsAsTable(in_zone_data=biodiversity_5km_buffer, zone_field="id", in_value_raster=ave_terr_resample, out_table=terr_rich, ignore_nodata="DATA", statistics_type="MEAN", process_as_multidimensional="CURRENT_SLICE", percentile_values=90)
    .save(Terrestrial_Species_Zonal_Statistics_as_Table)


    # Process: Resample (Resample) (management)
    marine_species_richness_resample = "G:\\Brazil_SCI\\Brazil_SCI.gdb\\marine_species_richness_resample"
    arcpy.management.Resample(in_raster=marine_species_richness_clip, out_raster=marine_species_richness_resample, cell_size="1262.77611782025 1263.7446990789", resampling_type="NEAREST")
    marine_species_richness_resample = arcpy.Raster(marine_species_richness_resample)

    # Process: Marine Species Zonal Statistics as Table (Zonal Statistics as Table) (sa)
    arcpy.sa.ZonalStatisticsAsTable(in_zone_data=biodiversity_5km_buffer, zone_field="id", in_value_raster=marine_species_richness_resample, out_table=marine_rich, ignore_nodata="DATA", statistics_type="MEAN", process_as_multidimensional="CURRENT_SLICE", percentile_values=90)
    .save(Marine_Species_Zonal_Statistics_as_Table)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\Brazil_SCI\Brazil_SCI.gdb", workspace=r"G:\Brazil_SCI\Brazil_SCI.gdb"):
        WildlifeBiodiversitySubindex(*argv[1:])