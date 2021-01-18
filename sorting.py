class myList(list):
    def reorder(self, newList):
        assert len(newList) == len(self)

        for i in range(len(self)):
            self[i] = newList[i]

    def bubbleSort(self):
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, len(self) - 1):
                if self[i] > self[i + 1]:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    sorted = False

    @staticmethod
    def mergeLists(list_one, list_two):
        i, j = 0, 0
        merged_list = []

        while i < len(list_one) and j < len(list_two):
            if list_one[i] < list_two[j]:
                merged_list.append(list_one[i])
                i += 1
            else:
                merged_list.append(list_two[j])
                j += 1

        if i < len(list_one):
            merged_list += list_one[i:]
        else:
            merged_list += list_two[j:]

        return merged_list

    def mergeSort(self):
        subLists = [[element] for element in self]
        while len(subLists) > 1:
            i = 0
            while i + 1 < len(subLists):
                list_one = subLists.pop(i)
                list_two = subLists.pop(i)
                subLists.insert(i, myList.mergeLists(list_one, list_two))
                i += 1

        self.reorder(subLists[0])

    @staticmethod
    def partition(array):
        pivot = array[0]

        lesserList = myList([element for element in array if element < pivot])
        greaterList = myList([element for element in array if element > pivot])
        equalList = myList([element for element in array if element == pivot])

        return lesserList, equalList, greaterList

    @staticmethod
    def __quickSort(array):
        if len(array) < 2:
            return array
        else:
            lesserList, equalList, greaterList = myList.partition(array)
            return myList.__quickSort(lesserList) + equalList + myList.__quickSort(greaterList)

    def quickSort(self):
        self.reorder(myList.__quickSort(self))

l = myList(range(10, 0, -1))
l.quickSort()
print(l)

