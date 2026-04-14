#Exercise 1
print("Hello\n" "World!")

#По-чист вариант:

print("Hello\nWorld")


#Exercise 2
print('"I love Python!"')


#Exercise 3
name = ("Ivan")
age = 20

print(f"name: {name}", '|', f"age: {age}")

#Малка корекция (за по-красив output):

print(f"Name: {name} | Age: {age}")


#Exercise 4
print("Name\t Age")
print("Ivan\t 20")
print("Maria\t 22")


#Exercise 5
print("C:/Users/Boris/Desktop") #Това е което успях да направя знам че не е вярно!

#Правилното решение:
print("C:\\Users\\Boris\\Desktop")

#📌 Защо?

#\ е специален символ
#трябва да го „escape-нем“ → \\

#Алтернативно (много полезно):

print(r"C:\Users\Boris\Desktop")

#👉 r = raw string (много използвано в Python)


#Exercise 6
print("***")
print("* *")
print("***")


#OVERALL - 6.00