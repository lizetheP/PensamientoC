import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def promedio_salarioxregion(reporte):
    pass
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    print(reporte)
    promedio_salarioxregion(reporte)
            
main()