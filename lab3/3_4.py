def sort_file_contents(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    sorted_lines = sorted(line.strip() for line in lines)

    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(sorted_lines))

    print(f"Sorted contents written to {output_file}")

# Example usage:
sort_file_contents("input.txt", "sorted_output.txt")
