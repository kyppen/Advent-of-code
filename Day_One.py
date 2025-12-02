from collections import deque

filename = "Input.txt"

def read_file_to_queue(queue):
    with open(filename, 'r') as file:
        for line in file:
            cleaned_line = line.rstrip()
            queue.append(cleaned_line)
    print("Items added to queue")
def main():
    zero_click = 0
    current_rotation = 50
    queue = deque()
    read_file_to_queue(queue)
    iterations = 0
    for element in queue:
        iterations += 1
        direction = element[:1]
        amount = element[1:]


        for _ in range(int(amount)):
            if direction == "R":
                current_rotation += 1
                if current_rotation == 100:
                    current_rotation = 0
            elif direction == "L":
                current_rotation -= 1
                if current_rotation == -1:
                    current_rotation = 99

            if current_rotation == 0:
                zero_click += 1





    print(f"final print {current_rotation}")
    print(f"count {zero_click}")
    print(f"iterations: {iterations}")

main()