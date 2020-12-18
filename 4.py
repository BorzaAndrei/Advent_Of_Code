import re


with open("input/4.txt") as r:
    # passports = []
    count = 0
    passport = {}

    correct_fields = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None, 'ecl': None, 'pid': None, 'cid': None}
    almost_correct_fields = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None, 'ecl': None, 'pid': None}
    for line in r.readlines():
        if line == '\n':
            if passport.keys() == correct_fields.keys() or passport.keys() == almost_correct_fields.keys():
                correct = True
                correct = correct and 1920 <= int(passport["byr"]) <= 2002
                correct = correct and 2010 <= int(passport["iyr"]) <= 2020
                correct = correct and 2020 <= int(passport["eyr"]) <= 2030
                correct = correct and re.findall("^#[0-9a-f]{6}$", passport["hcl"])
                correct = correct and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                correct = correct and re.findall("^[0-9]{9}$", passport["pid"])
                height = int(re.findall("[0-9]+", passport["hgt"])[0])
                if "cm" in passport["hgt"]:
                    correct = correct and 150 <= height <= 193
                else:
                    correct = correct and 59 <= height <= 76

                if correct:
                    count += 1

            passport = {}
        else:
            fields = line.split()
            for field in fields:
                data = field.split(':')
                passport[data[0]] = data[1]
    print(count)
