import random
when = ['A few years ago', 'Last week', 'Last month', 'Last year', 'A long time ago', 'Yesterday'] 
#['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a man','a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat', 'a child']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' named, ' 
    + random.choice(name) +  ', that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened)+'.')
