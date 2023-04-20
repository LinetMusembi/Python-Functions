def year_of_birth(name,age):
    year = 2023-age
    print(f"Hello{name},you were born in{year}")

def my_country(country="Kenya"):
    print(f"Hello I am from{country}")

def hello(*names):
    for name in names:
        print(f"Hello{name}")

def sum(*nums):
    answer = 0
    for num in nums:
        answer += num


    return answer   

def multiply_many(**kwargs):
    answer = 1
    for num in kwargs.values():
        answer*=num
#  Assignment

    return answer  
def concatenate_args(*strings):
    answer = ""
    for string in strings:
        answer += string

    return answer


def concatenate_kwargs(**weeks):
    strin = " "
    for week in weeks.values():
        strin += week
    return strin






