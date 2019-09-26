cars = ["ford", "volvo", "BMW"]
for car in cars:
    print(car)

cars.append("Honda")
cars.pop(1) # removes item 2 -> volvo
cars.remove("BMW")

print(cars)