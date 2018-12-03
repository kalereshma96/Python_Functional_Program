def get_anagram_prime(self):
    store_prime = Utility().get_prime()
    prime_anagram = []
    first_string_list = []
    second_string_list = []
    count = 0
    for each_index in range(0, len(store_prime) - 1):
        first_string_list = []
        s1 = str(store_prime[each_index])
        first_string = s1
        count = 0
        for i in first_string:
            first_string_list.append(i)

        for i in range(0, len(first_string_list) - 1):

            for j in range(i + 1, len(first_string_list)):
                temp = ''
                if first_string_list[i] > first_string_list[j]:
                    temp = first_string_list[i]
                    first_string_list[i] = first_string_list[j]
                    first_string_list[j] = temp

        first_string = ''
        for i in range(0, len(first_string_list)):
            first_string = first_string + first_string_list[i]

        for next_index in range(each_index + 1, len(store_prime)):

            second_string = str(store_prime[next_index])

            for i in second_string:
                second_string_list.append(i)

            for i in range(0, len(second_string_list) - 1):

                for j in range(i + 1, len(second_string_list)):
                    temp = ''
                    if second_string_list[i] > second_string_list[j]:
                        temp = second_string_list[i]
                        second_string_list[i] = second_string_list[j]
                        second_string_list[j] = temp

            second_string = ''
            for i in range(0, len(second_string_list)):
                second_string = second_string + second_string_list[i]

            if first_string == second_string:
                prime_anagram.append(store_prime[next_index])
                count += 1

            second_string_list = []

        if count >= 1:
            prime_anagram.append(store_prime[each_index])

    return prime_anagram
#
# utility_obj=Utility()
# store_prime_palindrome=utility_obj.get_palindrome_prime()
#
# print("The Prime Numbers which are Palindrome are as follows")
# for i in store_prime_palindrome:
#     print(i)
#
# print("The Prime Numbers which are Anagram are as follows")
# prime_anagram=[]
# prime_anagram=utility_obj.get_anagram_prime()
# for i in prime_anagram:
#     print(i)