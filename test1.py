palindrome = "Never Odd or Even"
	# We'll create two strings, to compare them
new_string = ""
reverse_string = ""
	# Traverse through each letter of the input string
for word in (palindrome):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
	if word != (" "):
			new_string = new_string+(word)
			reverse_string = new_string[::-1]
	# Compare the strings
print (new_string)
print (reverse_string)
