You’re asked to write recursive FizzBuzz. Your function takes 2 integers:
start and end, which are the first and last number in the sequence of integers
to return in a list (array). However, if the number is a multiple of 3, put
“Fizz” in the list instead of the number. If it’s a multiple of 5 put “Buzz”
in the list. If it’s a multiple of 3 and 5, put “FizzBuzz” in the list.
Example: fizzbuzz(1, 20) ⇒ [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11,
Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz]
"""

def wrapper(start, end):
    def recursiveFizzBuzz(num):
        if num < end:
            if not num % 3 and not num % 5:
                result.append("FizzBuzz")
            elif not num % 3:
                result.append("Fizz")
            elif not num % 5:
                result.append("Buzz")
            else:
                result.append(num)
            recursiveFizzBuzz(num+1)


    result = []
    recursiveFizzBuzz(start)
    return result

print(wrapper(1, 20))


"""Given a sorted array of strings, write a recursive function to find the index
of the first and last occurrence of a target string. If the target string
is not found in the array, report that.
Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan,
Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani,
Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)"""

instructors = ["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", "Mitchell", "Mitchell", "Mitchell", "Mitchell"]

def wrapper(sorted_array, target):
    def find_indexes(i, found):
        if i < len(sorted_array):
            if sorted_array[i] == target and not found:
                found = True
                result.append(i)
                print('hey')
            elif sorted_array[i] != target and found:
                result.append(i-1)
                # just to stop the above statement from being True
                found = False
            find_indexes(i+1, found)
        # in case the target is the last item(s) in the array
        elif found and len(result) < 2:
            result.append(i-1)
    result = []
    find_indexes(0, False)
    return tuple(result)

print(wrapper(instructors, 'Braus'))


"""Given a string of digits 2 to 9 a user has pressed on a T9 “old school”
telephone keypad, return a list of all letter combinations they could have
been trying to type on the keypad.
Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]"""

def wrapper(nums_string):
    def t9_letters():
        pass
    LOOKUP = {  2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"],
                5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"],
                8:["t","u","v"], 9:["w","x","y","z"]}

    result = []
    if nums_string:
        t9_letters()
    return result