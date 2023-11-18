import csv

# from pathlib import Path

# CAMINHO_EXCEL = Path(__file__) / 'arquivos-excel/'

def write_csv(data, rows, columns):
	filename = f'{data}.csv'
	print(filename)
	with open(filename, 'w', newline='') as file:
		dados = csv.writer(file)
		dados.writerow(columns)
		for dado in rows:
			dados.writerow(dado)