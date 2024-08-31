#creation of node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
#Linkedlist operations
class LinkedList:
    #constructor to set head to none
    def __init__(self):
        self.head = None
    #insert at begining
    def InsertAtBegining(self,data):
        node = Node(data)
        #if no node is present then assign it head
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
     #insert at index
    def InsertAtIndex(self,data,index):
        #index starts from 0
        #if index is 0 then it is first node, so we can use insert at begining
        if index == 0:
            self.InsertAtBegining(data)
            return
        else:
            node = Node(data)
            position = 0
            current = self.head
            #iterate two pointers to specified index
            while current:
                if position == index-1:
                    node = Node(data)
                    node.next = current.next
                    current.next = node
                position = position+1
                current = current.next
            
    
    #insert at end
    def InsertAtEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        current = self.head
        #iterate to the end 
        while(current.next != None):
            current = current.next
        current.next = node                    
    
    #deletion at begining
    def DeleteAtBegining(self):
        if self.head == None:
            return
        self.head = self.head.next
    
    #deletion at end
    def DeleteAtEnd(self):
        if self.head == None:
            return
        current = self.head
        while(current.next != None and current.next.next != None):
            current = current.next
        current.next = None
    
    #deletion at index
    def DeleteAtIndex(self,index):
        if self.head == None:
            return
        current = self.head
        position = 0
        if position == 0:
            self.DeleteAtBegining()
        else:
            while(current.next != None and position+1 != index):
                position = position+1
                current = current.next
            if current.next != None:
                current.next = current.next.next
            else:
                print("Index not found!")
            
    
    #print function          
    def Print(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            current = self.head
            #iterate pointer once and print the data value, repeat this process
            while current:
                print(str(current.data) + "-->", end=" ")
                current = current.next
            print("None")
#consider as main function
if __name__ == '__main__':
    l1 = LinkedList()
    while True:
        print("1.insert at begining\n2.print\n3.insert at index\n4.insert at end\n5.delete at begining\n6.delete at index\n7.delete at end :")
        choice = int(input("Enter your choice :"))
        
        if choice == 1:
            data = input("Enter data : ")
            l1.InsertAtBegining(data)
        elif choice == 2:
            l1.Print()
        elif choice == 3:
            data = input("Enter data : ")
            index = int(input("Enter index : "))
            l1.InsertAtIndex(data,index)
        elif choice == 4:
            data = input("Enter data : ")
            l1.InsertAtEnd(data)
        elif choice == 5:
            l1.DeleteAtBegining()
        elif choice == 6:
            index = input("Enter index : ")
            l1.DeleteAtIndex(index)
        elif choice == 7:
            l1.DeleteAtEnd()
        else:
            print("Enter correct values!")
            
    
         