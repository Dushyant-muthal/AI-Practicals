def solve(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    solve(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    solve(n - 1, auxiliary, source, destination)

n = 3
print("Tower of Hanoi with", n, "disks:")
solve(n, "A", "B", "C")
print("All disks moved successfully!")
