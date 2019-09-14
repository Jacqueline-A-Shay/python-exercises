def normalize_name(valid_py_name):
	NG_py_identifier = set('!@#$%^&*()+,?')
	valid_py_name = str(valid_py_name)
	valid_py_name = valid_py_name.strip()
	valid_py_name = valid_py_name.replace(' ','_')

	valid_py_name = valid_py_name.lower()

	return "".join([i for i in valid_py_name if i not in NG_py_identifier])

"""LETTERS = ' _abcdefghijklmnopqrstuvwxyz0123456789'
def normalize_name(python_identifier):
    python_identifier = python_identifier.lower()
    valid_chars = []
    for character in python_identifier:
        if character in LETTERS:
            valid_chars.append(character)
    return ''.join(valid_chars).strip().replace(' ', '_')"""



def cumsum(list_of_num):
	post_process = []
	sum_num = 0
	for i in list_of_num:
		sum_num = sum_num + i
		post_process.append(sum_num)
	return post_process


