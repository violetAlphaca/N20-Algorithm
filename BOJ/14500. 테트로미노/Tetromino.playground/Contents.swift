import Foundation

//

//var Input =
//"""
//4 5
//1 2 3 4 5
//1 2 3 4 5
//1 2 3 4 5
//1 2 3 4 5
//"""

//let a = Input.split(separator: "\n")
//let firstLine = a[0].components(separatedBy: " ")
//let n = Int(firstLine[0])!
//let m = Int(firstLine[1])!
//
//let base = Array.init(repeating: 0, count: m)
//var map: [[Int]] = Array.init(repeating: base, count: n)
//
//for i in 0..<n {
//    map[i] = a[i+1].components(separatedBy: " ").map { Int($0)! }
//}

// 콘솔 입력

let firstLine = readLine()!.components(separatedBy: " ")
let n = Int(firstLine[0])!
let m = Int(firstLine[1])!

let base = Array.init(repeating: 0, count: m)
var map: [[Int]] = Array.init(repeating: base, count: n)
for i in 0..<n {
    map[i] = readLine()!.components(separatedBy: " ").map { Int($0)! }
}

let boolBase = Array.init(repeating: false, count: m)
var visited: [[Bool]] = Array.init(repeating: boolBase, count: n)
var maxScore = 0
var priorityQueue = PriorityQueue(sort: >, elements: elems)

var elems: [Position] = []

for i in 0..<n {
    for j in 0..<m {
        elems.append(Position(x: j, y: i, score: map[i][j]))
    }
}

// main

while !priorityQueue.isEmpty {

    let elem = priorityQueue.dequeue()!
    if elem.score <= maxScore / 4 {
        break
    }
    maxScore = max(maxScore, bfs(elem))
}
print(maxScore)

func bfs(_ pos: Position) -> Int {
    let x = pos.x
    let y = pos.y
    let dx = [0, 1, 0, -1]
    let dy = [1, 0, -1, 0]
    visited = Array.init(repeating: boolBase, count: n)
    
    var score = 0
    var count = 0
    var candidate: PriorityQueue<Position> = PriorityQueue(sort: >, elements: [])
    
    candidate.enqueue(pos)
    visited[y][x] = true
    
    while count < 4 {
        let biggest = candidate.dequeue()!
        score += biggest.score
        count += 1
        
        for i in 0..<4 {
            let nx = biggest.x + dx[i]
            let ny = biggest.y + dy[i]
            if nx >= 0 && ny >= 0 && nx < m && ny < n && !visited[ny][nx] {
                candidate.enqueue(Position(x: nx, y: ny, score: map[ny][nx]))
                visited[ny][nx] = true
            }
        }
    }
    return score
}

//

struct Position: Equatable {
    let x: Int
    let y: Int
    let score: Int
    
    public static func == (_ lhs: Position, rhs: Position) -> Bool {
        return lhs.score == rhs.score
    }
    
    public static func > (_ lhs: Position, rhs: Position) -> Bool {
        return lhs.score > rhs.score
    }
}

// priority queue

public protocol Queue {
    associatedtype Element
    mutating func enqueue(_ element: Element) -> Bool
    mutating func dequeue() -> Element?
    var isEmpty: Bool { get }
    var peek: Element? { get }
}


public struct PriorityQueue<Element: Equatable>: Queue { // 1
    private var heap: Heap<Element> // 2
    public init(sort: @escaping (Element, Element) -> Bool,
         elements: [Element] = []) { // 3
        heap = Heap(sort: sort, elements: elements)
    }
    
    public var isEmpty: Bool { return heap.isEmpty }
    public var peek: Element? { return heap.peek() }
    
    public mutating func enqueue(_ element: Element) -> Bool { // 1
        heap.insert(element)
        return true
    }
    public mutating func dequeue() -> Element? { // 2
        return heap.remove()
    }
}


public struct Heap<Element: Equatable> {
    
    var elements: [Element] = []
    let sort: (Element, Element) -> Bool
    
    public init(sort: @escaping (Element, Element) -> Bool, elements: [Element] = []) {
        self.sort = sort
        self.elements = elements
        
        if !elements.isEmpty {
            for i in stride(from: elements.count / 2 - 1, through: 0, by: -1) {
                siftDown(from: i)
            }
        }
    }
    
    public var isEmpty: Bool {
        return elements.isEmpty
    }
    
    public var count: Int {
        return elements.count
    }
    
    public func peek() -> Element? {
        return elements.first
    }
    
    func leftChildIndex(ofParentAt index: Int) -> Int {
        return (2 * index) + 1
    }
    
    func rightChildIndex(ofParentAt index: Int) -> Int {
        return (2 * index) + 2
    }
    
    func parentIndex(ofChildAt index: Int) -> Int {
        return (index - 1) / 2
    }
    
    public mutating func remove() -> Element? {
        guard !isEmpty else {
            return nil
        }
        elements.swapAt(0, count - 1)
        defer {
            siftDown(from: 0)
        }
        return elements.removeLast()
    }
    
    mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = leftChildIndex(ofParentAt: parent)
            let right = rightChildIndex(ofParentAt: parent)
            var candidate = parent
            
    //        print("count: \(count), left: \(left), right: \(right)")
            if left < count && sort(elements[left], elements[candidate]) {
                candidate = left
   //             print("candidate: \(candidate), sort:\(sort(elements[left], elements[candidate]))")
            }
            if right < count && sort(elements[right], elements[candidate]) {
                candidate = right
    //            print("candidate: \(candidate), sort:\(sort(elements[right], elements[candidate]))")
            }
            if candidate == parent {
                return
            }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
    
    public mutating func insert(_ element: Element) {
        elements.append(element)
        siftUp(from: elements.count - 1)
    }
    
    mutating func siftUp(from index: Int) {
        var child = index
        var parent = parentIndex(ofChildAt: child)
        while child > 0 && sort(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = parentIndex(ofChildAt: child)
        }
    }
    
    mutating func remove(at index: Int) -> Element? {
        guard index < elements.count else {
            return nil
        }
        if index == elements.count - 1 {
            return elements.removeLast()
        } else {
            elements.swapAt(index, elements.count - 1)
            defer {
                siftDown(from: index)
                siftUp(from: index)
            }
            return elements.removeLast()
        }
    }
    
    func index(of element: Element, startingAt i: Int) -> Int? {
        if i >= count { return nil }
        if sort(element, elements[i]) { return nil }
        if element == elements[i] { return i }
        if let j = index(of: element, startingAt: leftChildIndex(ofParentAt: i)) { return j }
        if let j = index(of: element, startingAt: rightChildIndex(ofParentAt: i)) { return j }
        return nil
    }
}
