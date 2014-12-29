
u = {
	'1':'one',
	'2':'two',
	'3':'three',
	'4':'four',
	'5':'five',
	'6':'six',
	'7':'seven',
	'8':'eight',
	'9':'nine',
}

t = {
	'1':'ten',
	'2':'twenty',
	'3':'thirty',
	'4':'forty',
	'5':'fifty',
	'6':'sixty',
	'7':'seventy',
	'8':'eighty',
	'9':'ninety',
}

ts = {
	'1':'eleven',
	'2':'twelve',
	'3':'thirteen',
	'4':'fourteen',
	'5':'fifteen',
	'6':'sixteen',
	'7':'seventeen',
	'8':'eighteen',
	'9':'nineteen',
}

def solution(max):
	total = 0
	for i in range(1	, max+1):
		words = get_words(i)
		total += len(''.join(words))
	print(total)

def get_words(number):
	source = str(number)
	result = []
	length = len(source)
	if length > 0:
		source_0 = source[length-1]
		if source_0 in u:
			result.append(u[source_0])
		else:
			pass
	if length > 1:
		source_1 = source[length-2]
		if source_1 == '1' and source_0 != '0':
			if source_1 in ts:
				result.pop()
				result.append(ts[source_0])
			else:
				pass
		else:
			if source_1 in t:
				result.append(t[source_1])
			else:
				pass
	if length > 2:
		source_2 = source[length-3]
		if source_2 in u:
			if len(result) > 0:
				result.append('and')
			result.append('hundred')
			result.append(u[source_2])
		else:
			pass
	if length > 3:
		source_3 = source[length-4]
		if source_3 in u:
			if len(result) > 0 and result[0] != 'hundred' and 'and' not in result:
				result.append('and')
			result.append('thousand')
			result.append(u[source_3])
		else:
			pass
	result.reverse()
	return result
	
if __name__ == '__main__':
	solution(1000)