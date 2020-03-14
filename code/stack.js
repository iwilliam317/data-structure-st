class Stack {
    constructor() {
        this.counter = 0
        this.storage = {}
    }

    push(data) {
        this.storage[this.counter] = data
        this.counter++
    }

    pop() {
        if (this.counter === 0) return undefined
        delete this.storage[this.counter - 1]
        this.counter--
    }

    size() {
        return this.counter
    }

    print() {
        for (let i = 0; i < this.counter; i++) {
            console.log(this.storage[i])
        }
    }

}


const stack = new Stack()
stack.push('1')
stack.push('12')
stack.push('13')
stack.push('14')
stack.pop()
stack.print()
stack.size()