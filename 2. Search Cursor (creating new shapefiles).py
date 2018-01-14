#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the States shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\States.shp"

#Creating list of necessary fields 
fieldList = ["Region"]
arcpy.env.workspace = arcpy.Describe(inputFC).path

#Creating new empty lists for appending later
regionList = []
outputName = []

#Creating search cursor for feature class
with arcpy.da.SearchCursor(inputFC, fieldList) as srCursor:
    #Iterating through each row
    for row in srCursor:

        #Appending value to regionList if not already in it
        if row[0] not in regionList:
            regionList.append(row[0])
            outputName.append(row[0].replace(" ", "").rstrip("Region"))

#Iterating through the regionList
for idx in range(0, len(regionList)):
    query = "\"{0}\" = '{1}'".format(fieldList[0], regionList[idx])
    out_layer = outputName[idx] + "_lyr"

    #Copying and deleting features
    arcpy.MakeFeatureLayer_management(inputFC, out_layer, query)
    print("Create new shapefile - {0}.shp".format(outputName[idx]))
    arcpy.CopyFeatures_management(out_layer, outputName[idx])
    arcpy.Delete_management(out_layer)