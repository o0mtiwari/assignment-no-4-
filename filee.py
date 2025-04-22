try:
    with open("my_file.txt", "r")as file:
        print("contains of sample.txt:")

        for line in file:
            print(line.strip())
except FilenotFounderror:
    print("Error: the file 'sample.txt' was not found.")
except Exception as e:
    print(f"an unnexpected error occured: {e}")