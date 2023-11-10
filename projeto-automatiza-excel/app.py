from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from openpyxl import Workbook

app = Flask(__name__)
CAMINHO_EXCEL = Path(__file__) / 'arquivos-excel/'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		try:
			data = request.form
			columns = int(data['number_of_columns'])
			return render_template('add_columns_names.html', columns=columns, name=name_sheet)
		except ValueError as e:
			return f'Por favor, digitar um número. Erro: {e}'
	return render_template('index.html')

@app.route('/columns_name', methods=['GET', 'POST'])
def columns_name():
	if request.method == 'POST':
		data = request.form.to_dict()
		input = []
		for name, value in data.items():
			input.append(value)
			print(input)
		
		# wb = Workbook()
		# with open()
	return 'Depois de adicionar o nome das colunas.'


@app.route('/row_values', methods=['GET', 'POST'])
def row_values():
	if request.method == 'POST':
		data = request.form
		pass
	return redirect(request.referrer)