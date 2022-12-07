
txt = "Hello World"[::1]
print(txt)

txt = "Hello World"[::-1]
print(txt)

# ----- OR --------
def my_function(x):
  return x[::-1]

mytxt = my_function("Hello World")

print(mytxt)


txt = ['Hello World', 'My dear']
separator = ', '
print(separator.join(txt))