s = input('Введите строку: ')
r = s.replace(' ', '')
def palindrome():
    if r[::-1] == r:
        return True
    else:
        return False
    
print(palindrome())