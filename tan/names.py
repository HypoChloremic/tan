



alt_names = ["REST", "ORD"]
# Very ugly indeed
base_name   = [["VT1{}".format(x), "HT1{}".format(x)] for x in range(3,7)]
name = [[base_name[x][x%2]+" ORD", base_name[x][x%2]+" REST", base_name[x][(x+1)%2]+" ORD", base_name[x][(x+1)%2]+" REST"] for x in range(len(base_name)) ]

for pos in name:
	for x in range(4):
		print(pos[x])