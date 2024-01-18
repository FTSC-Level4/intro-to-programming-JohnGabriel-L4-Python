age= 64

#First I used 'if' then 'elif' so I can execute them as a group.
if age < 2:
    print('You are a baby')
elif age <= 3:
    print('You are a toddler')
elif age <= 12:
    print('You are a kid')
elif age <= 19:
    print('You are a teenager')
elif age <= 64:
    print('You are an adult')
else:
    print('You are an elder')

# 'elif' is a combination of 'else' and 'if', allowing for the evaluation of multiple conditions.