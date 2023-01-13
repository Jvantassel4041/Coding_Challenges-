def count_letters(strr):
  # return len(strr)
  ans = 0
  
  for letter in strr:
    print(letter)
    if letter != " ":
      ans += 1
      print(ans)
  return ans

print(count_letters("grandpa farts")==12)

# You may either use Python’s built-in len() function or define your own.

# text = "Number of characters in this text"
# print len(text)

# Custom function

# def count_chars(txt):
# 	result = 0
# 	for char in txt:
# 		result += 1     # same as result = result + 1
# 	return result

# print count_chars(text)