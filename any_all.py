kreipiniai = ['Jonai', 'Antanai', 'Jurgita']

res = list(map(lambda v: 'labas ' + v if v != 'Antanai' else 'eik is cia ' + v, kreipiniai))

print(res)

