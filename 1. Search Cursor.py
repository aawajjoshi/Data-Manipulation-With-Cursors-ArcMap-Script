#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the States shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\States.shp"

#Creating empty list for appending later
fieldList = []
fields = arcpy.ListFields(inputFC, "", "String")

#Iterating through the fields 
for fld in fields:
    print("The field name is: {0}".format(fld.name))
    fieldList.append(fld.name)

#creating a new cursor object named srCursor
with arcpy.da.SearchCursor(inputFC, fieldList) as srCursor:
    #Iterating through each row
    for row in srCursor:
        i = 0
        for fld in fields:
            print("{0}: {1}".format(fld.name, row[i]))
            i = i + 1