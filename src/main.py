from generate_data import generate_random_list
from algorithms import insertion_sort, merge_sort, measure_time
from save_data import save_data

def main():
    results_list = []
    while True:
        source_root = input("Enter size of list for sorting or type exit to close the app >>> ")
        if source_root.lower() == 'exit':
            save_data(results_list)
            break
        try:
            list_size = int(source_root)
            random_list = generate_random_list(0, 10000, list_size)
            print(f"Generated list: {random_list}")

            sorted_list_insertion, measured_time_insertion = measure_time(insertion_sort, random_list.copy())
            print(f"Sorted list using Insertion Sort: {sorted_list_insertion}")
            print(f"Time taken by Insertion Sort: {measured_time_insertion:.6f} milliseconds")

            sorted_list_merge, measured_time_merge = measure_time(merge_sort, random_list.copy())
            print(f"Sorted list using Merge Sort: {sorted_list_merge}")
            print(f"Time taken by Merge Sort: {measured_time_merge:.6f} milliseconds")

            sorted_builtin, measured_time_builtin = measure_time(sorted, random_list.copy())
            print(f"Sorted list using Built-in Sort: {sorted_builtin}")
            print(f"Time taken by Built-in Sort: {measured_time_builtin:.6f} milliseconds")

            results_list.append(f"Original List: {random_list}\n")
            results_list.append(f"List Size: {list_size}\n")
            results_list.append(f"Insertion Sort Time: {measured_time_insertion:.6f} milliseconds\n")
            results_list.append(f"Merge Sort Time: {measured_time_merge:.6f} milliseconds\n")
            results_list.append(f"Built-in Sort Time: {measured_time_builtin:.6f} milliseconds\n")
            results_list.append("\n")
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()