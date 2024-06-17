def remove_zeros(nums: list) -> list:
    """
    Дан массив целых чисел. Нужно удалить из него нули. 
    Дополнительная память не потребляется
    """
    write_idx: int = 0

    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    
    return nums[:write_idx] 


arr: list = [0, 1, 0, 3, 12]
print(remove_zeros(arr))
