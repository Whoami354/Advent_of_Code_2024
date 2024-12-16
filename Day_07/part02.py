with open("input.txt", "r") as lines:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = lines.read().split("\n")

def check_possible(target: int, nums: list[int]) -> bool:
    if len(nums) == 1:
        return target == nums[0]

    num = nums.pop()
    target_str = str(target)
    num_str = str(num)

    if target / num == target // num:
        if check_possible(target // num, nums[:]):
            return True
    if target - num >= 0:
        if check_possible(target - num, nums[:]):
            return True

    if target_str.endswith(num_str) and len(target_str) > len(num_str):
        new_target = int(target_str[: -len(num_str)])
        if check_possible(new_target, nums[:]):
            return True

    return False

total_sum = 0

for line in input:
    target = int(line.split(":")[0])
    nums = list(map(int, line.split(": ")[1].split(" ")))
    if check_possible(target, nums[:]):
        total_sum += target

print(total_sum)