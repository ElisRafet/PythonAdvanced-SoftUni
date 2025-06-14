def numbers(*args):
    positive_sum = sum(num for num in args if num > 0)
    negative_sum = sum(num for num in args if num < 0)
    result = f'{negative_sum}\n{positive_sum}\n'
    if positive_sum > abs(negative_sum):
        result += 'The positives are stronger than the negatives'
    else:
        result += 'The negatives are stronger than the positives'
    return result

nums = map(int, input().split())
print(numbers(*nums))