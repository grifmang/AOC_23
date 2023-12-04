def convert_phonetic_digits():
    nums = []
    with open('day1.txt') as file:
        for line in file:
            line = line.strip().replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')
            nums.append(line)

    return nums

def get_counts(num_list):
    nums = []
    for line in num_list:
        line_nums = [x for x in line if x.isdigit()]
        try:
            nums.append(int(f"{line_nums[0]}{line_nums[-1]}"))
        except Exception as e:
            print(e)

    print(sum(nums))

converted = convert_phonetic_digits()
print(converted)
get_counts(converted)