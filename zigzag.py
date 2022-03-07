def zigzag(number):
    ans = []
    while len(number) >= 3:
        print(number)
        num = number[:3]
        if num[0] > num[1] < num[2] or num[0] < num[1] > num[2]:
            ans.append(1)
            number.pop(0)
        else:
            ans.append(0)
            number.pop(0)
    return ans


numb = [1, 2, 3, 2,5]
zigzag(numb)
