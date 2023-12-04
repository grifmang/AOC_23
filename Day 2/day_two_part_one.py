def main():
    total = 0

    with open('day2.txt') as file:
        for line in file:
            isValid = True
            vals = {
                "green": 13,
                "red": 12,
                "blue": 14
            }
            game_id = line.split(':')[0].split(' ')[-1]
            line = line.split(':')[1].replace(';', ',')
            line = line.split(',')
            for element in line:
                element = element.strip()
                if int(element.split(' ')[0]) > vals[element.split(' ')[1]]:
                    isValid = False
                    break
            
            if isValid: total += int(game_id)

    return total


if __name__ == '__main__':
    print(main())