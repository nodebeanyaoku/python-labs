# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)

gen = (n for n in nums if n // 1111 == 0)

for i in gen:
    print (i)
