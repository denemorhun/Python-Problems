from LinkedList import LinkedList
import Node

def main():
    LL = LinkedList()

    LL.insert_at_tail(1)
    LL.insert_at_tail(2)
    LL.insert_at_tail(4)
    LL.print_list()

    print(LL.search(4))

if __name__ == "__main__":
    main()