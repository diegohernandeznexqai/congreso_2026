import pandas as pd 
import os
os.chdir(r"C:\Users\Diego\Desktop\Proyectos_python\Congreso_2026")
Congreso_2014=pd.read_excel("2014_elecciones.xlsx", sheet_name=None)
print(Congreso_2014)