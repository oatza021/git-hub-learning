"""xdd"""
def main(num):
	"""Xdd"""
	if num < 10:
		print(num+1)
		num += 1
		main(num)
main(int(input()))
