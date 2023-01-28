# #%% leer archivo linea a linea
# archivo = open('./Python/Clase10_IA_Script/IA/archivo.txt')
# for line in archivo.readlines():
#     print(line)
# archivo.close()
#%% Escribir el archivo
archivo = open('./Python/Clase10_IA_Script/IA/archivo.txt','a')
archivo.write(f'\nEsta linea viene de donde')
archivo.close()

