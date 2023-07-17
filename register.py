# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
# from wtforms.validators import DataRequired


# class RegisterForms(FlaskForm):
#     email = EmailField("Почта", validators=[DataRequired()])
#     password = PasswordField("Пароль", validators=[DataRequired()])
#     repeat_password = PasswordField(
#         "Повторите пароль", validators=[DataRequired()])
#     name = StringField("Имя", validators=[DataRequired()])
#     submit = SubmitField("Зарегистрироваться", validators=[DataRequired()])

counter = 0


# def count(n, counter):
#     cpiunt = 0
#     for i in range(1, n+1):
#         cpiunt += i
#         counter += 1
#     return cpiunt, counter


# print(count(5, counter))


# def count2(n, counter):
#     counter += 1
#     return (((1+n)*n)//2), counter


# print(count2(5, counter))


# def finder(n, counter):
#     list_1 = []
#     for i in range(1, n+1):
#         if i == 1:
#             list_1.append(i)
#         elif i == 2:
#             list_1.append(i)
#         elif i % 2 == 0:
#             continue
#         else:
#             for j in range(3, (i//2)+1):
#                 if i % j == 0:
#                     break
#                 counter += 1
#             else:
#                 list_1.append(i)
#         counter += 1
#     return list_1, counter


# print(finder(20, counter))

# def num(n):
#     print(n)
#     if (n >= 3):
#         num(n-1)
#         num(n-2)
#         num(n-2)
#     return


# print(num(4))

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-1)+fibo(n-2)


# print(fibo(7))

# k = [[1, 2], [3, 4], [5, 6]]
# print(dict(k))
# m = iter(k)
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

# for i, d in enumerate(k):
#     if 2 < d < 6:
#         k[i] = 0
# print(k)
