fecha = "1/2/1999"

if (fecha[1] == '/'):
    dia = fecha[0]
else:
	dia = (int(fecha[0]) * 10) + int(fecha[1])

if (fecha[-7] == '/'):
    mes = int(fecha[-6])
else:
     mes = (int(fecha[-7]) * 10) + int(fecha[-6])

año = int(fecha[-4::])

print(dia, mes, año)