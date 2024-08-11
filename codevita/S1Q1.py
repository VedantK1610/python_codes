def valency_sum(element):
    ascii_sum = sum(int(digit) for i in element for digit in str(ord(i)))
    while ascii_sum > 9:
        ascii_sum = sum(int(digit) for digit in str(ascii_sum))
    return ascii_sum

def balance(compound, ep):
    e1, e2 = compound[0], compound[1]
    v1, v2 = valency_sum(e1), valency_sum(e2)

    possible_combinations = []
    max_multiplier1 = ep // v1
    max_multiplier2 = ep // v2
    for m1 in range(1, max_multiplier1):
        if m1*v1 > ep:
            break
        for m2 in range(1,max_multiplier2):
            curr = m1 * v1 + m2 * v2
            if curr > ep:
                break
            if curr==ep:
                combination = f"{e1}{m1} {e2}{m2}"
                possible_combinations.append((m1 * v1, combination))

    if possible_combinations:
        possible_combinations.sort(reverse=True)
        for _, comb in possible_combinations:
            print(comb)
    else:
        print("Not Possible")

# Example usage:
compound = input().strip()
ep = int(input().strip())

balance(compound, ep)
