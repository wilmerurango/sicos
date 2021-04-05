import pypandoc
salida = pypandoc.convert_file("C:/Users/ANALISTA_COSTOS/OneDrive - FUNDACION CLINICA DEL RIO/2021/LIQUIDACION/ENVIO_EMAILS/GRUPO_1/Eligio Álvarez/LILIANA TORRES.xlsx", 'pdf', outputfile='liliana_torres.pdf')
assert salida == ""