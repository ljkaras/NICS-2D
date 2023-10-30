print("...............................................................................")
print(".                                                                             .")
print(".                              NICS-2D extractor                              .")
print(".                         Sept. 01 2022 (Lucas Karas)                         .")
print(".                                                                             .")
print("...............................................................................")

#Modules
import sys 

print("\nReading the Gaussian output file:\n")

name = input("Enter the output name: \n")
f = open(name, "r")
f_lines = f.readlines()

print("\nChecking the output file...")

NMR_found = False
for line in f_lines:
    if "NMR" in line or "nmr" in line:
        NMR_found = True
        break
if NMR_found == True:
    print("NMR keyword found in the output. Proceed.")
else:
    sys.exit("No NMR keyword found in the output file. Stop.")
    
Bq_found = False
for line in f_lines:
    if "Bq" in line:
        Bq_found = True
        break
if Bq_found == True:
    print("Bq atom found in the output. Proceed.")
else:
    sys.exit("No Bq atom found in the output file. Stop.")

# Bq atoms xyz coordinates:
xy_split = []
for line in f_lines:
    if "Bq" in line and line.count('.') == 3:
        xy_split += line.split()

print("\nBq coordinates successfully archived.\n")

#Isotropic and ZZ shielding:

shielding_iso = []
shielding_zz = []

for index, line in enumerate(f_lines):
    if "Bq" in line and "Isotropic" in line:
        shielding_iso += line.split()
        shielding_zz += f_lines[index+3].split()

print("Magnetic shieldings successfully archived.\n")

f.close()

print("Gaussian output closed! :D\n")

#saving the Bq xy coordinates:

xy_values = []
for i in range(0,len(xy_split),4):
    xy_values.append(xy_split[i+1:i+3])

#extracting the Isotropic Shielding values: 

shielding_iso_values = []
for i in range(0,len(shielding_iso),8):
    shielding_iso_values.append(shielding_iso[i+4])

shielding_zz_values = []
for i in range(0,len(shielding_zz),6):
    shielding_zz_values.append(shielding_zz[i+5])

#extracting NICSiso and NICSzz
iso_float = [float(x) for x in shielding_iso_values]
zz_float = [float(x) for x in shielding_zz_values]
def Convert(lst):
    return [ -i for i in lst ]
NICSiso_float = Convert(iso_float)
NICSiso_values = [str(x) for x in NICSiso_float]
NICSzz_float = Convert(zz_float)
NICSzz_values = [str(x) for x in NICSzz_float]

print("...............................................................................")
Data = input("Choose between (1) IMS; (2) MSzz; (3) NICSiso; or (4) NICSzz: \n")
final_name = input("\nName your NICS-2D file (e.g., benzene): ")

if Data == "1":
    print("\nPreparing the Isotropic Magnetic Shielding data.")
    IMS_list = ["x","y","NICS"]
    for i in range(0,len(xy_values)):
        IMS_list += xy_values[i]
        IMS_list.append(shielding_iso_values[i])

    IMS_name = final_name+"_IMS.txt"
    f_IMS = open(IMS_name,"w")
    IMS_str = ""
    for i in range(0,len(IMS_list),3):
        IMS_str += str(IMS_list[i:i+3])
    IMS_1 = IMS_str.replace("[","")
    IMS_2 = IMS_1.replace("'","")
    IMS_3 = IMS_2.replace("]","\n")
    IMS_final = IMS_3.replace(",","\t")
    f_IMS.write(IMS_final)
    f_IMS.close()
elif Data == "2":
    print("\nPreparing the Magnetic Shielding (zz) data.")
    ZZ_list = ["x","y","NICS"]
    for i in range(0,len(xy_values)):
        ZZ_list += xy_values[i]
        ZZ_list.append(shielding_zz_values[i])
    
    ZZ_name = final_name+"_MSzz.txt"
    f_ZZ = open(ZZ_name,"w")
    ZZ_str = ""
    for i in range(0,len(ZZ_list),3):
        ZZ_str += str(ZZ_list[i:i+3])
    ZZ_1 = ZZ_str.replace("[","")
    ZZ_2 = ZZ_1.replace("'","")
    ZZ_3 = ZZ_2.replace("]","\n")
    ZZ_final = ZZ_3.replace(",","\t")
    f_ZZ.write(ZZ_final)
    f_ZZ.close()

elif Data == "3":
    print("\nPreparing the NICSiso data.")
    NICSiso_list = ["x","y","NICS"]
    for i in range(0,len(xy_values)):
        NICSiso_list += xy_values[i]
        NICSiso_list.append(NICSiso_values[i])
    
    NICSiso_name = final_name+"_NICSiso.txt"
    f_NICSiso = open(NICSiso_name.txt,"w")
    NICSiso_str = ""
    for i in range(0,len(NICSiso_list),3):
        NICSiso_str += str(NICSiso_list[i:i+3])
    NICSiso_1 = NICSiso_str.replace("[","")
    NICSiso_2 = NICSiso_1.replace("'","")
    NICSiso_3 = NICSiso_2.replace("]","\n")
    NICSiso_final = NICSiso_3.replace(",","\t")
    f_NICSiso.write(NICSiso_final)
    f_NICSiso.close()

elif Data == "4":
    print("\nPreparing the NICSzz data.")
    NICSzz_list = ["x","y","NICS"]
    for i in range(0,len(xy_values)):
        NICSzz_list += xy_values[i]
        NICSzz_list.append(NICSzz_values[i])
    
    NICSzz_name = final_name+"_NICSzz.txt"
    f_NICSzz = open(NICSzz_name,"w")
    NICSzz_str = ""
    for i in range(0,len(NICSzz_list),3):
        NICSzz_str += str(NICSzz_list[i:i+3])
    NICSzz_1 = NICSzz_str.replace("[","")
    NICSzz_2 = NICSzz_1.replace("'","")
    NICSzz_3 = NICSzz_2.replace("]","\n")
    NICSzz_final = NICSzz_3.replace(",","\t")
    f_NICSzz.write(NICSzz_final)
    f_NICSzz.close()

print("\nNormal Termination!")
print("...............................................................................")

