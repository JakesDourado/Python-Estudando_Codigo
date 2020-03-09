dic_criptogragia = {
	
	'a':'*/747/',
	'b':'*/tge/',
	'c':'*/dtt/',
	'd':'*/3g6/',
	'e':'*/9n7/',
	'f':'*/dni/',
	'g':'*/56y/',
	'h':'*/9wl/',
	'i':'*/1vp/',
	'j':'*/381/',
	'k':'*/fgf/',
	'l':'*/df4/',
	'm':'*/2f5/',
	'n':'*/jj2/',
	'o':'*/7ui/',
	'p':'*/buo/',
	'q':'*/6e8/',
	'r':'*/bko/',
	's':'*/a42/',
	't':'*/klo/',
	'u':'*/5a1/',
	'w':'*/jui/',
	'x':'*/56b/',
	'y':'*/lo3/',
	'z':'*/98f/'
}

print(dic_criptogragia.items())

def cripografar(mensagem):
	back = ''
	for element in mensagem:
		if element in dic_criptogragia:
			back = back + dic_criptogragia[element] + '.'
	return back

def descripografar(mensagem):
	back = ''
	mensagem = mensagem.split('.')

	for element in mensagem:
			if element:
				for sub_element in list(dic_criptogragia.items()):
					key = sub_element[0]
					value = sub_element[1]
					if (element == value):
						back = back + key
	return back

print('Modulo criptografia iniciado com sucesso!')