scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)
print(scores['白元芳'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
print(scores.get('武则天', 60))
print(scores.popitem())
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('骆昊', 85))
print(scores)
scores.clear()
print(scores)