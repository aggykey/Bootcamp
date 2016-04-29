def reverse_string(string):
	rev_string  = ""
	if string is "":
		return None
	else:
		for b in string:
			rev_string = b+rev_string
    		if rev_string == string:
    			return True
    	return rev_string
print reverse_string('Agnes')