numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [(num, "Even") if num % 2 == 0 else (num, "Odd") for num in numbers]
print(results)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total=sum(numbers)
print(total)

celsius = [0, 10, 20, 30, 40, 50]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

numbers = [10, 20, 30]
total=sum(numbers,1000)
print(total)

numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

name ="Alice"
print(name)

msg = "It's a beautiful car"
print(msg)

quote = 'She said, "Nice to meet you!"'
print(quote)

saying ="She said, \"What a beautiful day!\""
print(saying)
print("village" in saying)
print(len(saying))
print(saying[4:30])

new_poem = """Roses are red,
Violets are blue, 
Python is great,
And so are you."""
print(new_poem)

name_1 ="Noel"
name__2 ="Tumpeine"
Full_name = name_1 + " " + name__2
print(Full_name)

name = "Noel"
age = 18
name_age = name + " is " + str(age) + " years old."
print(name_age)

name = "Joel"
age= 10
name_age = f"My name is {name} and I am {age} years old."
print(name_age)

num1 = 10000
num2 = 5000
print(f"The sum of {num1} and {num2} is {num1 + num2}!")

my_work = "I will be a great doctor!"
print(my_work[:10])
print(my_work[10:20])
print(my_work[10:])
print(my_work[:])
print(my_work[0:4:2])

lower_name = "noel the only"
upper_name = lower_name.upper()
print(upper_name)

upper_name = "NOEL THE ONLY"
lower_name = upper_name.lower()
print(lower_name)

my_name = "Noel"
replaced_my_name = my_name.replace("Noel", "Lerrian")
print(replaced_my_name)

first_name = "Noel"
last_name = "Tumpeine"
full_name = first_name + " " + last_name
print(full_name)

experience_years = 5
experience_info = "Experience" + " " + str(experience_years) + " years"
print(experience_info)

my_int_1= 100
my_int_2= 200
my_sum = my_int_1 + my_int_2
print('Integer sum:', my_sum)

int_1 = 70
int_2 =20
diff_int = int_1 - int_2
print('Integer difference:', diff_int)

num_1 = 50
num_2 = 20
product_num = num_1 * num_2
print('Integer product:', product_num)

count = 80
count -=20
print('Count after decrementing by 20:', count)

greetings = "Konnichiwa"
greetings *= 5
print(greetings)

print(999> 1000)
print(500!= 5000)

age = 25
if age <= 20: 
    print("You are still a child.")
else:
    print("You are an adult!")

results = 89
if results >= 90:
    print("You have passed with flying colors!")
else: 
    print("You have failed.")

age = 9
if age >= 25:
    print("You are an adult!")
elif age >= 18:
    print("You are a young adult!")
else:
    print("You are still a child!")

is_citizen = False
age = 18
if is_citizen