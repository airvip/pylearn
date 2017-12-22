#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#一、定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
#二、以Field类为父类，定义StringField，IntegerField 类
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(50)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

#三、定医院类，控制Model类对象的创建
class ModelMetaclass(type):
    '''定义元类'''
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            # 保存类属性和列的映射关系到mappings字典
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            # 将类属性移除，使定义的类字段不污染User类属性，只在实例中可以访问这些key
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系，创建类时添加一个__mappings__类属性
        attrs['__table__'] = name.lower() # 表名是类名的小写，创建类时添加一个__table__类属性
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)


#四、编写Model基类
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

#最后，我们使用定义好的ORM接口，使用起来非常的简单。
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('name')

# 创建一个实例：
u = User(id=1, name='airvip')
# 保存到数据库：
u.save()



'''

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')

# 创建一个实例：
u = User(id=1, name='airvip')
# 保存到数据库：
u.save()
'''