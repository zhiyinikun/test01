#namelist=['a1','b2','a']
#namepop=namelist.pop(0)#默认弹出末尾的值 从列表删除后依然可以弹出使用
#namelist.sort()#排序
#print(namelist)

# cslist=['a','b','c']
# for cs in cslist[:2]:#遍历输出切片
#     print(cs)
# print(cslist[2:3])#切片输出
# cs2list=cslist[:]#复制整个列表
# cs2list.append('d')#复制的列表中添加元素
# print(cs2list)

#相当于给元组重新赋值
# dimensions = (200, 50)#定义元组
# print("遍历元组:")
# for dimension in dimensions:#元组的遍历
#     print(dimension)
# dimensions=(400,100)
# print("\n修改元组变量")
# for dimension in dimensions:
#     print(dimension)

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +", I see your favorite language is " + favorite_languages[name].title() + "!")

# yz_users=['long','he','liu']#创建一个待验证的列表
# yzcg_users=[]#创建一个存放验证过了的列表
# while yz_users:#循环验证待验证列表
#     yz_user=yz_users.pop()#每次循环验证 都弹出该用户
#     print('验证的用户名为：'+yz_user)
#     yzcg_users.append(yz_user)#验证后添加到空列表中
# print("显示所有已验证的用户：")
# print(yz_users)
# for yzcg_user2 in yzcg_users:#遍历已经验证的用户
#     print(yzcg_user2.title())


# def user_cs(username):###username是形参
#     print('hello'+username)
# user_cs('kall')#实参'''
def get_name(first_name, last_name, mid_name=''):
    if mid_name:#判断mid_name为ture也就是有数据
        full_name=first_name+' '+mid_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name#将值返回导函数
name=get_name('long','wen','jie')
print(name)
names=get_name('long','wenjie')
print(names)