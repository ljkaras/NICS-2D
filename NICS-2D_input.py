print("...............................................................................")
print(".                                                                             .")
print(".                Input file generator for NICS-2D calculations                .")
print(".                         Aug. 31 2022 (Lucas Karas)                          .")
print(".                                                                             .")
print("...............................................................................")

#Modules
import sys
import numpy as np

#Input Keywords: 
input_name = input("\nName your NICS-2D input file (e.g., benzene.com): \n")

method = input("Enter the DFT method: ")
disp_ans = input("Do you want to add dispersion [y/n]? ")
if disp_ans == "Yes" or disp_ans == "yes" or disp_ans == "Y" or disp_ans == "y" or disp_ans == "YES":
    dispersion = "EmpiricalDispersion=GD3"
else:
    dispersion = ""
basis_set = input("Enther the basis set: ")

charge = input("Enter molecule charge: ")
spin = input("Enter molecule spin: ")

f = open(input_name, "w+")
f.write("{a} {b} {c} {d}".format(a="#N SCF=(qc,symm) NMR IOp(10/46=1) geom=connectivity", b=method, c=dispersion, d=basis_set))
f.write("\n\ncomment line")
f.write("\n\n")
f.write("{e} {f}".format(e=charge, f=spin))
f.write("\n")

print("\nInput keywords successfully entered!\n")
print("...............................................................................")
#Input Geometry: 

print("Enter xyz geometry and then press ctrl+dd: ")
geometry = sys.stdin.read()
#geometry = input("Enter xyz geometry: ")
geometry_split = geometry.split()
geom = ""
for i in range(0,len(geometry_split),4):
    geom += str(geometry_split[i:i +4])
    
geom_1 = geom.replace("[","")
geom_2 = geom_1.replace("'","")
geom_final = geom_2.replace("]","\n")
geom_final_2 = geom_final.replace(",,",",")
f.write(geom_final_2)

print("\nInput geometry successfully entered!\n")
print("...............................................................................")

#Generating the 2D Bq grid: 

x_input = input("Enter the grid range in x in Å (e.g., -1 1): ")
x_str = x_input.split()
x_int = [eval(i) for i in x_str]
x_max = x_int[1]+0.01

y_input = input("Enter the grid range in y in Å (e.g., -1 1): ")
y_str = x_input.split()
y_int = [eval(i) for i in x_str]
y_max = y_int[1]+0.01

spacing = float(input("Enter the spacing between the Bq atoms in Å (e.g., 0.25): "))

NICS_dist = float(input("Enter the Bq atom distance to the ring plane in Å: "))

for a in np.arange(x_int[0],x_max,spacing):
    for b in np.arange(y_int[0],y_max,spacing):
        f.write("{g} {h} {i} {j}".format(g="Bq", h=a, i=b, j=NICS_dist))
        f.write("\n")

print("\n2D grid successfully generated!")
print("...............................................................................")

f.close()

#Writing the connectivity:

print("\nWriting connectivity.")

f = open(input_name, "r+")
lines = len(f.readlines())
total_lines = lines-4 
for i in range(1,total_lines):
    f.write("{a} {b}".format(a="\n", b=i))
f.write("\n\n")

f.close()

print("\nConnectivity done!")
print("...............................................................................")
print("\nInput Saved. Normal Termination.")
print("...............................................................................")

