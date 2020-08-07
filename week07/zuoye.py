from abc import ABCMeta, abstractmethod

class Zoo():
    def __init__(self,name):
        self.name = name
        self.animal_dict = {}

    def add_animal(self,cls):
        #以字典的形式，动物类别作为键，动物实例作为value，同一动物物种键值相同
        temp_id = id(cls)
        key_animal = str(type(cls))
        if self.animal_dict.get(key_animal) == None:
            self.animal_dict[key_animal] = [temp_id]
        elif ( self.animal_dict.get(key_animal) != None) and (temp_id not in  self.animal_dict[key_animal]):
             self.animal_dict[key_animal].append(temp_id)
        else:
            print("%s动物已存在"% (cls.name))





class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, an_type, shape, character, belong):

        self.an_type = an_type
        self.shape = shape
        self.character = character
        if  self.shape == "小":
            mark1 = 1
        elif self.shape == "中等":
            mark1 = 2
        elif self.shape == "大":
            mark1 = 3
        if self.an_type == '食肉' and mark1 >= 2 and self.character == '凶猛':
            self.belong = '凶猛动物'
        else:
            self.belong = '非凶猛动物'


class Cat(Animal):
    sound = '喵'
    def __init__(self,name,an_type,shape,character):
        self.name = name
        self.an_type = an_type
        self.shape = shape
        self.character = character
        super().__init__(self.an_type, self.shape, self.character,'')

def getattr(cls1,name):
    for  key in cls1.animal_dict.keys():
        if name in key:
            print("有%s这个动物" % (name))
            break
        else:
            print("没有%s这个动物" % (name))



if __name__ == '__main__':
    cat1 = Cat('大花猫','食肉','小','凶猛')

    z = Zoo('时间动物园')
    z.add_animal(cat1)
    have_cat = getattr(z, 'Cat')
    print(cat1.belong)

