def fizz_buzz(n: int) -> list[str]:
    answer = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        answer.append(word or str(i))
    return answer


print(fizz_buzz(50))
