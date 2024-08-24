class TreeObj:
    """Для описания вершин и листьев решающего дерева"""
    def __init__(self, indx, value=None):
        self.index = indx
        self.value = value
        self.__right = None
        self.__left = None

    def get_right(self):
        return self.__right

    def set_right(self, value):
        self.__right = value

    def get_left(self):
        return self.__left

    def set_left(self, value):
        self.__left = value

    right = property(get_right, set_right)
    left = property(get_left, set_left)


class DecisionTree:
    """Для работы с решающим деревом в целом"""

    @classmethod
    def predict(cls, root, x):
        """Для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root
        (возвращает значение узла - атрибут value)"""
        current_obj = root
        while current_obj:
            obj_next = cls.get_next(current_obj, x)
            if obj_next is None:
                break
            current_obj = obj_next
        return current_obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """Возвращает добавленную вершину - объект класса TreeObj"""
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj
    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        return obj.right

# for exemple:

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)
