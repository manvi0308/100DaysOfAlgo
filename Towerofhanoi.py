''' Problem Tower of Hanoi - A classical mathematical problem'''

def tower_of_hanoi(from_disk , to_disk , aux_disk , n):
    if(n==1) : #Base case
        print('Move disk 1 from',from_disk,'To',to_disk)
        return
    tower_of_hanoi(from_disk , aux_disk ,to_disk , n-1)
    print('Move disk',n,'from',from_disk ,'To',to_disk)
    tower_of_hanoi(aux_disk ,to_disk , from_disk, n-1)

disks = 6
tower_of_hanoi('A','B','C',disks)
