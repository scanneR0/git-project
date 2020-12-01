import re

INPUT = "name234name1.544name149.431.10name0.99name123.05"

print ("%.2f" % (sum(float(match[1].replace(".","")+match[-1]) for match in re.findall(r"((\d{1,3}(\.(\d){3})*)(\.\d\d)?)", INPUT))))