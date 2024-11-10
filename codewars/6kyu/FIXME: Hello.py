class Dinglemouse(object):
    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.order_list = []

    def setAge(self, age):
        self.age = age
        if "age" not in self.order_list:
            self.order_list.append("age")
        return self

    def setSex(self, sex):
        self.sex = "male" if sex == "M" else "female"
        if "sex" not in self.order_list:
            self.order_list.append("sex")
        return self

    def setName(self, name):
        self.name = name
        if "name" not in self.order_list:
            self.order_list.append("name")
        return self

    def make_hello(self):
        result = ["Hello."]
        for x in self.order_list:
            if x == "age":
                result.append(f"I am {self.age}.")
            elif x == "sex":
                result.append(f"I am {self.sex}.")
            elif x == "name":
                result.append(f"My name is {self.name}.")
        return result

    def hello(self):
        return " ".join(self.make_hello())
