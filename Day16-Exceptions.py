try:
    S = input()
    message = int(S)
except Exception:
    message = 'Bad String'
finally:
    print(message)
