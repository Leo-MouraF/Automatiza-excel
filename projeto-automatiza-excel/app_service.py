import csv


def write_csv(data, rows, columns):
	"""
	Faz o processamento dos dados inseridos pelo usuário, escrevendo um arquivo
	no formato CSV.
	data: Nome do arquivo;
	rows: É o session['rows'], as linhas inseridas;
	columns: É o session['columns'], o identificador dos dados.
	"""
	filename = f'{data}.csv'
	with open(filename, 'w', newline='') as file:
		dados = csv.writer(file)
		dados.writerow(columns)
		for dado in rows:
			dados.writerow(dado)