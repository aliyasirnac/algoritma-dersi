class DoubleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        newNode = self.Node(item)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def get_list(self):
        currNode = self.head
        while currNode != None:
            print(currNode.data)
            currNode = currNode.next

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        if self.size == 0:
            return None
        poppedNode = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return poppedNode.data
    
    def peek(self):
        if self.size == 0:
            return None
        return self.tail.data
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def  add_to_index(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        newNode = self.Node(item)
        if index == 0:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
        elif index == self.size:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            newNode.prev = currNode.prev
            newNode.next = currNode
            currNode.prev.next = newNode
            currNode.prev = newNode
        self.size += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            removedNode = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            removedNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            removedNode = currNode
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev
        self.size -= 1
        return removedNode.data

    def find(self, item):
        currNode = self.head
        index = 0
        while currNode is not None:
            if currNode.data == item:
                return index
            currNode = currNode.next
            index += 1
        return -1

class MP3Player:
            def __init__(self):
                self.playlist = DoubleLinkedList()
                self.current_index = 0
            
            def display_menu(self):
                print("\n=== MP3 Player ===")
                print("1. Add song to playlist")
                print("2. Remove song from playlist")
                print("3. Show current playlist")
                print("4. Play next song")
                print("5. Play previous song")
                print("6. Show current song")
                print("7. Clear playlist")
                print("8. Exit")
                return input("Choose an option: ")
            
            def run(self):
                while True:
                    choice = self.display_menu()
                    
                    if choice == "1":
                        song = input("Enter song name: ")
                        self.playlist.append(song)
                        print(f"Added '{song}' to playlist")
                        
                    elif choice == "2":
                        if self.playlist.is_empty():
                            print("Playlist is empty!")
                            continue
                        try:
                            index = int(input(f"Enter index (0-{self.playlist.size-1}): "))
                            removed = self.playlist.remove_at_index(index)
                            print(f"Removed '{removed}' from playlist")
                            if self.current_index >= self.playlist.size and self.playlist.size > 0:
                                self.current_index = self.playlist.size - 1
                        except (ValueError, IndexError):
                            print("Invalid index!")
                            
                    elif choice == "3":
                        if self.playlist.is_empty():
                            print("Playlist is empty!")
                        else:
                            print("\nCurrent Playlist:")
                            curr = self.playlist.head
                            index = 0
                            while curr:
                                marker = " -> NOW PLAYING" if index == self.current_index else ""
                                print(f"{index}: {curr.data}{marker}")
                                curr = curr.next
                                index += 1
                                
                    elif choice == "4":
                        if self.playlist.is_empty():
                            print("Playlist is empty!")
                        elif self.current_index < self.playlist.size - 1:
                            self.current_index += 1
                            curr = self.playlist.head
                            for _ in range(self.current_index):
                                curr = curr.next
                            print(f"Playing: {curr.data}")
                        else:
                            print("Already at last song!")
                            
                    elif choice == "5":
                        if self.playlist.is_empty():
                            print("Playlist is empty!")
                        elif self.current_index > 0:
                            self.current_index -= 1
                            curr = self.playlist.head
                            for _ in range(self.current_index):
                                curr = curr.next
                            print(f"Playing: {curr.data}")
                        else:
                            print("Already at first song!")
                            
                    elif choice == "6":
                        if self.playlist.is_empty():
                            print("No songs in playlist!")
                        else:
                            curr = self.playlist.head
                            for _ in range(self.current_index):
                                curr = curr.next
                            print(f"Currently playing: {curr.data}")
                            
                    elif choice == "7":
                        self.playlist.clear()
                        self.current_index = 0
                        print("Playlist cleared!")
                        
                    elif choice == "8":
                        print("Goodbye!")
                        break
                        
                    else:
                        print("Invalid choice! Please try again.")

        # Usage example:
player = MP3Player()
player.run()