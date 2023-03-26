#Bio Data
Name = input('Enter your name ')
Location = input('Enter your current location ')
Age = input('Enter you Date of birth ')
Color = input('Enter your favorite color ')
Hobbies = input('Enter your hobbies ')
client= [Name, Location, Age, Color, Hobbies]

Data=(Name, Location, Age, Color, Hobbies)
Total_data=tuple(Data)
print(Total_data)

print(Total_data.count('dd'))



