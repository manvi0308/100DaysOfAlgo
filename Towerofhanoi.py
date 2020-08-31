# Problem Tower of Hanoi - A classical mathematical problem
'''About: Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk
4) That is we cant have a bigger disk over smaller disk'''

'''Sources: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
   Sources: https://www.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/e/move-three-disks-in-towers-of-hanoi'''
   # Khan Academy link provides excellent visualization of problem

def tower_of_hanoi(from_disk , to_disk , aux_disk , n):
    if(n==1) : #Base case
        print('Move disk 1 from',from_disk,'To',to_disk)
        return
    tower_of_hanoi(from_disk , aux_disk ,to_disk , n-1) # recursive call over n-1 disks
    print('Move disk',n,'from',from_disk ,'To',to_disk)
    tower_of_hanoi(aux_disk ,to_disk , from_disk, n-1)

print('input the number of disks : ',end = '')
disks = input()
tower_of_hanoi('A','B','C',int(disks))
