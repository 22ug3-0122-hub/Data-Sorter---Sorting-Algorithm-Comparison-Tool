# 22ug3-0122

import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def generate_random_data(size=10, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]


def display_table(results):
    print("\n--- Sorting Algorithm Performance Comparison ---")
    print("{:<15} {:<20} {:<20}".format("Algorithm", "Execution Time (s)", "Steps / Operations"))
    print("-" * 55)
    for algo, result in results.items():
        print("{:<15} {:<20.6f} {:<20}".format(algo, result['time'], result['steps']))
    print("-" * 55)


def main():
    data = []
    results = {}

    while True:
        print("\n--- Data Sorter: Sorting Algorithm Comparison Tool ---")
        print("1. Enter numbers manually")
        print("2. Generate random numbers")
        print("3. Perform Bubble Sort")
        print("4. Perform Merge Sort")
        print("5. Perform Quick Sort")
        print("6. Compare all algorithms (show performance table)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                user_input = input("Enter numbers separated by spaces: ")
                data = [int(x) for x in user_input.split()]
                print("✅ Data successfully stored.")
            except ValueError:
                print("❌ Invalid input! Please enter only integers.")

        elif choice == '2':
            try:
                size = int(input("Enter number of elements: "))
                data = generate_random_data(size)
                print(f"✅ Random dataset generated: {data}")
            except ValueError:
                print("❌ Invalid input! Enter a valid number.")

        elif choice == '3':
            if not data:
                print("⚠️ No data available. Please enter or generate data first.")
                continue
            sorted_data, time_taken, steps = bubble_sort(data)
            print("\nBubble Sort Result:", sorted_data)
            print(f"Execution Time: {time_taken:.6f}s | Steps: {steps}")
            results["Bubble Sort"] = {'time': time_taken, 'steps': steps}

        elif choice == '4':
            if not data:
                print("⚠️ No data available. Please enter or generate data first.")
                continue
            sorted_data, time_taken, steps = merge_sort(data)
            print("\nMerge Sort Result:", sorted_data)
            print(f"Execution Time: {time_taken:.6f}s | Steps: {steps}")
            results["Merge Sort"] = {'time': time_taken, 'steps': steps}

        elif choice == '5':
            if not data:
                print("⚠️ No data available. Please enter or generate data first.")
                continue
            sorted_data, time_taken, steps = quick_sort(data)
            print("\nQuick Sort Result:", sorted_data)
            print(f"Execution Time: {time_taken:.6f}s | Steps: {steps}")
            results["Quick Sort"] = {'time': time_taken, 'steps': steps}

        elif choice == '6':
            if not results:
                print("⚠️ No sorting results yet. Perform sorting first.")
            else:
                display_table(results)

        elif choice == '7':
            print("👋 Exiting program. Thank you for using Data Sorter!")
            break

        else:
            print("❌ Invalid choice! Please select a valid menu option (1–7).")


if __name__ == "__main__":

    main()
