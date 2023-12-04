# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from input_file import GetInput

# ins = GetInput()
# ins.get_input('1')

def get_counts():
    nums = []
    with open('day1.txt') as file:
        for line in file:
            line_nums = [x for x in line if x.isdigit()]
            try:
                nums.append(int(f"{line_nums[0]}{line_nums[-1]}"))
            except Exception as e:
                print(e)

    print(sum(nums))

get_counts()
