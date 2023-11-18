from pathlib import Path

from app_service import write_csv
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
CAMINHO_EXCEL = Path(__file__) / 'arquivos-excel/'
app.secret_key = 'chave_secreta'

@app.before_request
def antes_da_solicitacao():
    session.modified = True

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		try:
			data = request.form
			columns = int(data['number_of_columns'])
			if not session:
				session['columns'] = []
				session['rows'] = []
			else:
				session.pop('columns', None)
				session.pop('rows', None)
				session['columns'] = []
				session['rows'] = []
			return render_template('add_columns_names.html', columns=columns)
		except ValueError as e:
			return f'Por favor, digitar um número. Erro: {e}'
	return render_template('index.html')

@app.route('/columns_name', methods=['GET', 'POST'])
def columns_name():
	if request.method == 'POST':
		data = request.form.to_dict()
		input = []
		for name, value in data.items():
			if data[name] == '':
				return 'Favor, digitar um valor para cada campo.'
			else:
				input.append(value)
				session['columns'] = input
	return render_template("add_rows.html")


@app.route('/row_values', methods=['GET', 'POST'])
def row_values():
	if request.method == 'POST':
		data = request.form
		tupla = []
		for i in session['columns']:
			if data[i] == "":
				return 'Por favor, digitar um valor para cada célula.'
			else:	
				tupla.append(data[i])
	tupla = tuple(tupla)
	session['rows'].append(tupla)
	return redirect(request.referrer)


@app.route('/conclude_table', methods=['GET', 'POST'])
def make_table():
	if request.method == 'POST':
		data = request.form
		if data['table_name'] != '':
			write_csv(data['table_name'], session['rows'], session['columns'])
			return render_template('index.html')
		return 'Favor, digitar um nome para sua tabela.'
	return render_template('conclude.html')