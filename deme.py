id = input('输入前17位身份证号码:')
if len(id) != 17 or id.isdigit() == False:
    print('请重新输入前17位身份证号码')
else:
    c = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    z = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    code = sum(int(id[i]) * c[i] for i in range(17)) % 11
    # print('第18位身份证号码是:', sfz + z[code])
sfzkey = id + z[code]
print('完整的身份证号码是:', sfzkey)