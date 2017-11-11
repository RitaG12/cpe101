def main():
	str1 = str(input("Enter string1: "))
	str2 = str(input("Enter string2: "))
	p =my_strspn(str1, str2)
	print("Result: ", p)

def my_strspn(str1, str2):
	count =0
	for s in str1:
		if s not in str2:
				break
		count+=1
	return count

if __name__ == "__main__":
	main()
