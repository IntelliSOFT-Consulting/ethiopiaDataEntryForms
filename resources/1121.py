import csv

str1 = ' <td><input id="pdPOsfQXESt-%s-val" name="entryfield" title="SDG_11.2.1_II:Population with convenient access to public transport %s" value="[ SDG_11.2.1_II:Population with convenient access to public transport %s ]" /></td>\n'

str2 = ' <td><input id="joMJzDHiGvR-%s-val" name="entryfield" title="SDG_11.2.1_II:Total city population %s" value="[ SDG_11.2.1_II:Total city population %s ]" /></td>\n'

de1 = ""
de2 = ""

with open("1121.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row['CategoryOption']
        uid = row['Uid']

        print(uid)

        de1 += str1 % (uid, cat, cat)
        de2 += str2 % (uid, cat, cat)
with open("1121-1.html", "w") as f1:
    f1.write(de1)


with open("1121-2.html", "w") as f1:
    f1.write(de2)
