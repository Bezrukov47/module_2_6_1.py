# Дополнительное практическое задание по модулю: "Основные операторы"
def generate_password(n):
    pairs = []
    for i in range(1, len(range(1, n + 1))):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    result = ""
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += ''.join(map(str, pair))
    return result
# Проверка использования путем перебора цифр из диапазона
n = 17  #  от 3 до 20
password = generate_password(n)
print(f"Пароль для {n}: {password}")
