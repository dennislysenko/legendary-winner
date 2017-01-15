import csv

with open('prelim/emojipasta_sub.csv', 'r') as f:
    r = csv.reader(f, delimiter=',', quotechar='"')
    o = open('prelim/corpus.txt', 'w')
    for row in r:
        if not row:
            continue

        o.write(row[0])

    o.close()
