key = 'my var'
value = 1.234
old_way = '%-10s = %.2f'%(key,value)
print(old_way)

new_way = '%(key)-10s = %(value).2f' % {
    'value': value,'key': key}

pantry = [
    ('eggs',1.25),
    ('apples',2.5),
    ('cherries',15)
]

# modification friendly
for i,(item,count) in enumerate(pantry):
    new_way1 = '%(loop)d: %(item)-10s = %(count)d' % {
        'loop':i+1,
        'item':item.title(),
        'count':round(count)
    }

    new_way2 = '{}: {} = {}'.format(
        i + 1,
        item.title(),
        round(count)
    )

    print(new_way2)


# predefine printing template
menu = {
    'A': 'apple',
    'B': 'banana',
    'C': 'cat'
}

template = ('Monday : %(A)s \n'
            'Tuesday : %(B)s \n'
            'Wednesday : %(C)s')
formatted = template % menu
print(template%menu)

# thousands separators
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

# centering
b = 'my string'
formatted = format(b, '^20s')
print('*',formatted,'*')

#format multiple values
formatted = '{} = {}'.format(key,value)
print(formatted)

print('{} replace {{}}'.format(1.234))

formatted = '{1} = {0}'.format(key,value)

formatted = '{0} loves cat, {0} loves dog'.format(key)
print(formatted)


