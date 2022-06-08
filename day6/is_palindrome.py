def is_palindrome(num):
    referce_1 = num
    referce_2 = 0
    while referce_1 > 0:
        referce_2 = referce_2 * 10 + referce_1 % 10
        referce_1 = referce_1 // 10 
    return num == referce_2

print(is_palindrome(121)) 
