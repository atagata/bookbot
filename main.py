def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        len_counter(file_contents)
        count_characters(file_contents)
        return file_contents, len_counter(file_contents), count_characters(file_contents)
    
def len_counter(file_contents):
        char = file_contents.split()
        return len(char)

def count_characters(file_contents):
    # with open("books/frankenstein.txt") as f:
    #     input_string = f.read().lower()
    input_string = file_contents
    input_string = input_string.lower()
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def counter_report():
    x, y, z = main()
    header = f"--- Begin report of books/frankenstein.txt ---\n{y} words found in the document\n"
    summary = ""
    for key in z:
        #  print(key, type(key), key.isalpha())
        if key.isalpha():
              summary += (f"The '{key}' character was found {z.get(key)} times\n")
        else:
           pass  
    print(f"{header} \n {summary}")
    return(f"{header} \n {summary}")

# main()
counter_report()
