def move_disk(disk_number, from_peg, to_peg):
    print("移动碟子"+ str(disk_number) + ",从柱子" + str(from_peg) + "到柱子" + str(to_peg) + ".")
# 有1,2,3三个柱子,1+2+3 = 6
# 所以备用的那个柱子就是 -> = 6-from_peg-to_peg
def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move_disk(n,start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(n-1, start_peg, spare_peg)
        move_disk(n, start_peg, end_peg)
        solve_hanoi(n-1,start_peg, end_peg)

# The number of partitions of a positive integer n, using parts up
# to size m, is the number of ways in which n can be expressed as the sum
# of positive integer parts up to m in increasing order.

def count_partitions(n, m):
    if n == 0:
        return 0
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
