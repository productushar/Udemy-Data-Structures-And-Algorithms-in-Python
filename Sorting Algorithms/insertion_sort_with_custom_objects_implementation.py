# Insertion Sort - Exercise: Sorting Custom Objects

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return str(self.name)

def insertion_sort(people):

    for i in range(len(people)):
        j = i

        while j > 0 and people[j-1] > people[j]:
            people[j-1], people[j] = people[j], people[j-1]
            j = j - 1


# Testing   
if __name__ == '__main__':
    
    n = [Person('Adam',23),Person('Ana',17),Person('Kevin',32),Person('Daniel',37)]
    insertion_sort(n)
    for i in n:
        print(i.age)
