#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the MOHigherEd shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\MOHigherEd.shp"

#Name of new field
fieldNew = "Full-Addr"

#Validating new field name 
fieldNew = arcpy.ValidateFieldName(fieldNew)

#Checking to see if a field with the same name already exists and deleting if necessary
fields = arcpy.ListFields(inputFC, fieldNew)
for fld in fields:
    if fld.name == fieldNew:
        arcpy.DeleteField_management(inputFC, fld.name)
arcpy.AddField_management(inputFC, fieldNew, "TEXT", "", "", 50)

#Creating a list of necessary fields 
fieldList = ["Address", "City", "State", "ZIP", fieldNew, "Facility"]

#Creating update cursor for feature class
with arcpy.da.UpdateCursor(inputFC, fieldList) as upCursor:
    #Iterating through each row
    for row in upCursor:

        #Updating the new row with full address 
        strFullAdr = row[0] + ", " + row[1] + ", " + row[2] + " " + row[3]
        row[4] = strFullAdr
        upCursor.updateRow(row)
        print("Update address for: {0}".format(row[5]))

#Printing final message to indicate the completion of update
print("Update complete")
