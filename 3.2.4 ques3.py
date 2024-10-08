population=100000
for year in range(1,11):
    population +=population*0.05
    print("Year",year, ":",int(population))