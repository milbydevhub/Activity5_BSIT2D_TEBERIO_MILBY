from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_structure(structure):
    print("Current state:", structure)


def operate_stack(stack):
    while True:
        print("\n--- STACK OPERATIONS ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        if isinstance(stack, ArrayStack):
            print("5. Check if full")
            print("6. Back to main menu")
        else:
            print("5. Back to main menu")

        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print("Pushed:", value)
                show_structure(stack)
            elif choice == "2":
                print("Popped:", stack.pop())
                show_structure(stack)
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
            elif isinstance(stack, ArrayStack) and choice == "5":
                print("Stack is full." if stack.is_full() else "Stack is not full.")
            elif (isinstance(stack, ArrayStack) and choice == "6") or (
                not isinstance(stack, ArrayStack) and choice == "5"
            ):
                break
            else:
                print("Invalid choice. Please try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def operate_queue(queue):
    while True:
        print("\n--- QUEUE OPERATIONS ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        if isinstance(queue, ArrayQueue):
            print("5. Check if full")
            print("6. Back to main menu")
        else:
            print("5. Back to main menu")

        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("Enqueued:", value)
                show_structure(queue)
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
                show_structure(queue)
            elif choice == "3":
                print("Front element:", queue.peek_front())
            elif choice == "4":
                print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
            elif isinstance(queue, ArrayQueue) and choice == "5":
                print("Queue is full." if queue.is_full() else "Queue is not full.")
            elif (isinstance(queue, ArrayQueue) and choice == "6") or (
                not isinstance(queue, ArrayQueue) and choice == "5"
            ):
                break
            else:
                print("Invalid choice. Please try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def balanced_parentheses(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack = []

    for character in text:
        if character in opening:
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0


def parentheses_exercise():
    expression = input("Enter an expression using () [] {}: ")
    if balanced_parentheses(expression):
        print("Result: Balanced")
    else:
        print("Result: Not Balanced")


def print_queue_exercise():
    jobs = []
    print("\nEnter print jobs. Leave the Job ID blank to finish.")
    while True:
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid whole number for pages.")
            continue
        jobs.append({"id": job_id, "pages": pages})
        print("Job added to the rear of the queue.")

    if not jobs:
        print("No print jobs were added.")
        return

    print("\nPrint order (FIFO):")
    wait_order = 1
    while jobs:
        job = jobs.pop(0)
        print(f"Wait order {wait_order}: Job {job['id']} - {job['pages']} page(s) printed.")
        wait_order += 1


def main():
    while True:
        print("\n===== MODULE 5: STACKS AND QUEUES =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Balanced Parentheses Exercise")
        print("6. Print Queue Simulation")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                capacity = int(input("Enter stack capacity: "))
                operate_stack(ArrayStack(capacity))
            except ValueError as error:
                print("Error:", error)
        elif choice == "2":
            operate_stack(LinkedStack())
        elif choice == "3":
            try:
                capacity = int(input("Enter queue capacity: "))
                operate_queue(ArrayQueue(capacity))
            except ValueError as error:
                print("Error:", error)
        elif choice == "4":
            operate_queue(LinkedQueue())
        elif choice == "5":
            parentheses_exercise()
        elif choice == "6":
            print_queue_exercise()
        elif choice == "7":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
