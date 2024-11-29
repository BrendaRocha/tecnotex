import pandas as pd

def excel_a_csv():
    #leer el archivo excel
    excel_file= "NUMERO DE ORDEN TINTORERIA.xlsx"
    df = pd.read_excel(excel_file)
    #guardar a csv
    df.to_csv("NUMERO DE ORDEN TINTORERIA.csv",index=False)


    


