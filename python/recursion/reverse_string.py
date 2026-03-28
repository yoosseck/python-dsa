def reverseString(str):
    result = ''
    for char in reversed(str):
        result += char

    return result


def reverseStringRecursive(str):
    if str == "":
        return ""
    else:
        return reverseStringRecursive(str[1:]) + str[0]


print(reverseString("yoyo master"))
print(reverseStringRecursive("yoyo master"))
