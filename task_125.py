def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convert_temperature(temperature):
    unit = temperature[-1]
    value = float(temperature[:-1])
    try:
        if unit == "C":
            unit = "F"
            value = celsius_to_fahrenheit(value)
            rounded_value = round(value, 1)
            return str(rounded_value) + unit
        elif unit == "F":
            return str(value) + unit
        else:
            raise ValueError("Invalid Unit")
    except ValueError as e:
        return f"Error: {e}"


def main():
    input_file_path = input("Enter the input file location: ")
    output_file_path = "text_files/converted_temperatures.txt"
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            """
            # Writes all the records to the new file (including the non converted ones)
            for line in input_file:
                line = line.strip()
                converted_temp = convert_temperature(line)
                output_file.write(f"{converted_temp}\n")"""

            # Write only the converted records to the new file
            for line in input_file:
                if "C" in line:
                    line = line.strip()
                    converted_temp = convert_temperature(line)
                    output_file.write(f"{converted_temp}\n")

    except FileNotFoundError:
        print("Input file not found.")
    except PermissionError:
        print("Permission denied. Check file permissions.")


if __name__ == "__main__":
    main()




