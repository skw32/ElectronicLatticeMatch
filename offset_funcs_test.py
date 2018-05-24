
### CURRENT STATUS: output format bit of a mess

################################################################################################################################################################

import els as els
import sys
import time

# Args of energy_align: IP, EA, window_up=max positive offset allowed, window_down=max negative offset allowed, gap=cut-off Eg (above which contact considered insulating)

#ETL, HTL = els.energy_align(5.8, 4.3, window_up=0.4, window_down=-0.1, gap=3.0)
#print(ETL)
EA = 3.5
IP = 5.2
CBO_lowlim = -0.3
CBO_uplim = 0.0
VBO_lowlim = 0.0
VBO_uplim = 0.3

ETL = els.CBO_scan(EA, CBO_lowlim, CBO_uplim, 3.0, output_file="CBO_cliff.dat") 
print(ETL)
HTL = els.VBO_scan(IP, VBO_lowlim, VBO_uplim, 3.0, output_file="VBO_cliff.dat") 
print(HTL)


print("")
print("Please find cif structure files for your candidates and move on to step 2 to find which junction partners should produce the least strain at the interface!\n")
