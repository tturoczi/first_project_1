#Összegzés

numbers = [10 ,24 ,21 ,25, 2, 234, 64, 234, 534]
sum=numbers[0]
for number in numbers:
    if sum < number:
        sum = number

print(sum)

#Szélsőérték keresés tétele

#leghosszabb
nevek= ["as", "fasafs", "aff", "adafgffad", "sdghgds", "gsdkjhdgshdshjbdgjsbdshjvbdfs"]
len1= nevek[0]
for a in nevek:
    if len(len1) < len(a):
        len1 = a
print (a)

numbers = [10 ,24 ,21 ,25, 2, 234, 64, 234, 534]
count=0
for number in numbers:
    if number%2 == 0:
        count += 1
print(count)


#eldöntés
nevek= ["as", "fasafs", "aff", "adafgffad", "sdghgds", "gsdkjhdgshdshjbdgjsbdshjvbdfs"]
for name in nevek:
    if name == "affa":
        print("van")
        break
    else:
        print("nincs")


#páros
numbers = [10 ,24 ,21 ,25, 2, 234, 64, 234, 534]
eredmeny= []
for number in numbers:
    if number%2 == 0:
        eredmeny.append(number)
print(eredmeny)

#transzformáció
nevek= ["as", "fasafs", "aff", "adafgffad", "sdghgds", "gsdkjhdgshdshjbdgjsbdshjvbdfs"]
lenght_of_nevek= []
for name in nevek:
    lenght_of_nevek.append(len(name))
print(lenght_of_nevek)


