import csv

from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

plt.title("xxxxxxxxxxxx21", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("yyyy", fontsize=16)
plt.tick_params(aixs='both', which='major', labelsize=16)

plt.show()

