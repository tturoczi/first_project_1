numbers = []
i=0
while i < 5:
    number= int(input("add meg {i+1}. szam"))
    numbers.append(number)
    i += 1
print(numbers)

result ="kapott szamok"
for number in numbers:
    result= result+str(number) + ","
    if i != len(numbers) -1:
        result = result + ","
        i += 1
