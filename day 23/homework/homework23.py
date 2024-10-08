def find_last_even(numbers_list):
    for i in range(len(numbers_list) - 1, -1, -1):
        if numbers_list[i] % 2 == 0:
            return numbers_list[i]

print(find_last_even([1,2,3,4,5]))


#The main point of our code is to find the last even number
#First we create a variable that will contain the numbers 1 to 5 inclusive


#Then we write the code whose definition is as follows (if numbers_list[i] %2 == 0) that is, if
#the last number is divisible by two, the computer calculates it and sees as a result the code functions and
#extractsthe last even number from the list, in our case this last even number is 4

