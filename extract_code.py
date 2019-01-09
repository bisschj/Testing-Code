	#OBJ_DES = re.search(r'^set description ".*?"', line.strip(), re.DOTALL | re.M | re.I)
	#OBJ_SESS = re.search(r'^set session .*?', line.strip(), re.DOTALL | re.M | re.I)

	OBJ_DES = re.compile('set description "(.*?)"\n' )	
	#OBJ_DES1 = re.compile('set description "(.*?)"', re.DOTALL | re.M | re.S)	
	OBJ_SESS = re.compile('set session (.*?)\n' )
	OBJ_SID = re.compile('\d{1}-\d{11}')
	OBJ_SO = re.compile('SO\d{6}-\d{6}')

	#OBJ_DES_1 = re.search(r'^edit ".*?^end$', data, re.DOTALL | re.M)


	if os.path.isfile("system vdom-property.txt"):
		file1 = open('system vdom-property.txt', 'r', encoding='utf-8').readlines()

		VDOM_PROP = {}
		VDOM_NME = VDOM_DES = VDOM_SESS = VDOM_SID = VDOM_SO = ' '

		#L_EDT = re.compile('^edit "(.*)"$')


		for fi_line in file1:
			L_EDT = re.search(r'^edit "(.*)"', fi_line, re.DOTALL | re.M )
			L_NEXT = re.search(r'^next$', fi_line, re.DOTALL | re.M )
			L_SET = re.search(r'^set (.+)\n', fi_line, re.DOTALL | re.M )
			#L_SET1 = re.compile(r'^set (.+)\n((?:\n.+)+)',  re.DOTALL | re.M )
			L_SET1 = re.compile(r'^(.+?)\n\n((?:[a-zA-Z0-9_:*-]+\n)+)',  re.M )
			L_SET2 = re.compile(r"\W+") # to remove blanks and newlines

			if L_EDT:
				print( L_EDT.group(1) )
			if 'set session ' in fi_line:
				VDOM_SESS = ( L_SET.group()[12:] )
				print(VDOM_SESS)
			if 'set description ' in fi_line:
				VDOM_DES = ( L_SET1.findall(fi_line) )
				print(VDOM_DES)
				print(" == ")
			if L_NEXT:
				print( L_NEXT.group() )
	