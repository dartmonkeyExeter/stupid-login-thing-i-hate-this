output_list = []

a=input()
a=int(a)

for i in range(8):
    output_list.append(round(a % 2))
    a = round(a / 2)
print(str(output_list)[::-1])
