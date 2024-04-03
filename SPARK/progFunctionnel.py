
def filter(ftc):
	lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	lstreturn = []
	for i in lst:
		if not ftc(i):
			lstreturn.append(i)
	print(lstreturn)
	return lstreturn

# Lambda function
# fonction sans nom, exécute une seule fois

# Predicate
# Fonction qui retourne un booléen
filter(lambda x: x % 2)
