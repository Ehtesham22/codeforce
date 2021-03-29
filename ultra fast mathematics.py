a = input()
b = input()
count = ''
for i in range(len(a)):
	if((a[i]=='1' and b[i]=='0')or(a[i]=='0' and b[i]=='1')):
		count += '1'
	else:
		count += '0'
print(count)
