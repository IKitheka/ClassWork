class Palindrome:
    def __init__(self):
        self.stack=[]
        self.queue=[]

    def push_character(self,ch):
        self.stack.append(ch)

    def enqueue_character(self,ch):
        self.queue.append(ch)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.pop(0)

def is_palindrome(s):

    obj=Palindrome()

    for char in s:
        obj.push_character(char)
        obj.enqueue_character(char)

    is_palindrome_show=True

    for i in range(len(s)):
        if obj.pop_character()!=obj.dequeue_character():
            is_palindrome_show=False
            break

    return is_palindrome_show



def main():
        # Read input
        s = input("Enter a word:").strip()

        # Check if palindrome
        if is_palindrome(s):
            print(f"The word, {s}, is a palindrome.")
        else:
            print(f"The word, {s}, is not a palindrome.")


if __name__ == "__main__":
        main()
