from operator import methodcaller


class Node(object):
    """
    双链表中的链表节点对象
    """

    def __init__(self, key=None, value=None, freq=0):
        """
        Args:
            key:对应输入的key
            value:对应输入的value
            freq:被访问的频率
            pre:指向前一个节点的指针
            next:指向后一个节点的指针
        """
        self.key = key
        self.value = value
        self.freq = freq
        self.pre = None
        self.next = None


class LinkedList(object):
    """
    自定义的双向链表
    """

    def __init__(self):
        """
        Args:
            __head:双向链表的头结点
            __tail:双向链表的尾节点
        """
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.pre = self.__head

    def insertFirst(self, node):
        """
        将指定的节点插入到链表的第一个位置
        Args:
            node:将要插入的节点
        """
        node.next = self.__head.next
        self.__head.next.pre = node
        self.__head.next = node
        node.pre = self.__head

    def delete(self, node):
        """
        从链表中删除指定的节点

        Args:
            node:将要删除的节点
        """
        if self.__head.next == self.__tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None

    def getLast(self):
        """
        从链表中获取最后一个节点
        Returns:
            双向链表中的最后一个节点，如果是空链表则返回None
        """
        if self.__head.next == self.__tail:
            return None
        return self.__tail.pre

    def isEmpty(self):
        """
        判断链表是否为空，除了head和tail没有其他节点即为空链表
        Returns:
            链表不空返回True，否则返回False
        """
        return self.__head.next == self.__tail


class LFUCache(object):
    """
    自定义的LFU缓存
    """

    def __init__(self, capacity):
        """
        Args:
            __capacity:缓存的最大容量
            __keyMap: key->Node 这种结构的字典
            __freqMap:freq->LinkedList 这种结构的字典
            __minFreq:记录缓存中最低频率
        """
        self.__capacity = capacity
        self.__keyMap = dict()
        self.__freqMap = dict()
        self.__minFreq = 0

    def get(self, key):
        """
        获取一个元素，如果key不存在则返回-1，否则返回对应的value
        同时更新被访问元素的频率
        Args:
            key:要查找的关键字
        Returns:
            如果没找到则返回-1，否则返回对应的value
        """
        #你的代码在这里#
        if key not in self.__keyMap:
            return -1

        self.__keyMap[key].freq += 1

        self.__freqMap[self.__keyMap[key].freq-1].delete(self.__keyMap[key])
        if self.__keyMap[key].freq not in self.__freqMap:
            self.__freqMap[self.__keyMap[key].freq] = LinkedList()
        self.__freqMap[self.__keyMap[key].freq].insertFirst(self.__keyMap[key])

        if self.__freqMap[self.__keyMap[key].freq-1].isEmpty():
            del self.__freqMap[self.__keyMap[key].freq-1]

        return self.__keyMap[key].value

    def put(self, key, value):
        """
        插入指定的key和value，如果key存在则更新value，同时更新频率
        如果key不存并且缓存满了，则删除频率最低的元素，并插入新元素
        否则，直接插入新元素
        Args:
            key:要插入的关键字
            value:要插入的值
        """
        #你的代码在这里#
        if key in self.__keyMap:
            self.__keyMap[key].value = value
            self.__keyMap[key].freq += 1

            self.__freqMap[self.__keyMap[key].freq -
                           1].delete(self.__keyMap[key])
            if self.__keyMap[key].freq not in self.__freqMap:
                self.__freqMap[self.__keyMap[key].freq] = LinkedList()
            self.__freqMap[self.__keyMap[key].freq].insertFirst(
                self.__keyMap[key])

            if self.__freqMap[self.__keyMap[key].freq-1].isEmpty():
                del self.__freqMap[self.__keyMap[key].freq-1]
        else:
            if len(self.__keyMap) >= self.__capacity:
                for (_, second) in self.__freqMap.items():
                    tmp = second.getLast()
                    second.delete(tmp)
                    del self.__keyMap[tmp.key]
                    break
                self.__keyMap[key] = Node(key, value, 1)
            else:
                self.__keyMap[key] = Node(key, value, 1)

        if 1 not in self.__freqMap:
            self.__freqMap[1] = LinkedList()
        self.__freqMap[1].insertFirst(self.__keyMap[key])




if __name__ == '__main__':
    operation = eval(input())
    data = eval(input())
    cache = eval("{}({})".format(operation.pop(0), data.pop(0)[0]))
    output = []
    for i, j in zip(operation, data):
        if i == 'put':
            methodcaller('put', j[0], j[1])(cache)
            output.append(None)
        elif i == 'get':
            output.append(methodcaller('get', j[0])(cache))
    print(output)
# [None, None, 1, None, -1, 3, None, -1, 3, 4]

