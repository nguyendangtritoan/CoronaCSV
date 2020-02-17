
import csv
import matplotlib.pyplot as plt
import numpy as np

country = ['']
confirmed = [0]
with open('2019_nCoV_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # get rid of first line
    for line in csv_reader:
        print(line)
        for x in range(len(country)):
            already_has = False
            if line[2]+'-'+line[3] == country[x]:
                already_has = True
                confirmed[x] = int(float(line[-3]))
                break
        if not already_has:
            country.append(line[2]+'-'+line[3])
            confirmed.append(int(float(line[-3])))

index = np.arange(len(country))

# Draw pie chart
# plt.figure(figsize=(50,50))
# plt.pie(confirmed, labels=country, autopct="%.1f%%")

# Draw bar chart
plt.bar(index, confirmed)
plt.xlabel('Country', fontsize=5)
plt.ylabel('Number of people', fontsize=5)
plt.xticks(index, country, fontsize=5, rotation=90)
plt.title('Confirmed Corona suffered')

# Draw line chart
# plt.plot(index, confirmed)
plt.show()


