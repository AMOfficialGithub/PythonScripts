import re
names = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu", "Peter Price", "Weifung Xu"]
winners = [name for name in names if re.search("[Xx]", name)]
print(winners)