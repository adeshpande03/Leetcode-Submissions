class Robot:
    def __init__(self, label, position, health, direction):
        self.label = label
        self.position = position
        self.health = health
        self.direction = direction
        self.prev = None
        self.next = None

class RobotList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, robot):
        if not self.head:
            self.head = self.tail = robot
        else:
            self.tail.next = robot
            robot.prev = self.tail
            self.tail = robot

    def remove(self, robot):
        if robot.prev:
            robot.prev.next = robot.next
        if robot.next:
            robot.next.prev = robot.prev
        if robot == self.head:
            self.head = robot.next
        if robot == self.tail:
            self.tail = robot.prev

    def collide(self, left, right):
        if left.health > right.health:
            left.health -= 1
            self.remove(right)
            right = right.next
        elif right.health > left.health:
            right.health -= 1
            self.remove(left)
            left = left.prev if left.prev else right
        else:
            self.remove(left)
            self.remove(right)
            left = left.prev if left.prev else right.next
            right = right.next if right.next else None

        return left, right

    def collide_all(self):
        curr = self.head
        while curr:
            if curr.prev and curr.prev.direction == 'R' and curr.direction == 'L':
                _, curr = self.collide(curr.prev, curr)
            elif curr.next and curr.direction == 'R' and curr.next.direction == 'L':
                curr, _ =  self.collide(curr, curr.next)
            else:
                curr = curr.next

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [Robot(i + 1, pos, health, dir) for i, (pos, health, dir) in enumerate(zip(positions, healths, directions))]
        robots.sort(key=lambda robot: robot.position)

        robot_list = RobotList()
        for robot in robots:
            robot_list.append(robot)
        
        robot_list.collide_all()

        remaining = []
        curr = robot_list.head
        while curr:
            remaining.append(curr)
            curr = curr.next
        remaining.sort(key=lambda robot: robot.label)
        return [robot.health for robot in remaining]