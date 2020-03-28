class Node {
    constructor(data){
        this.data = data
        this.next = null
    }
}

class LinkedList{
    constructor(){
        this.head = null
    }  

    print(){
        if (this.head === null){
            return
        }
        else {
            let current_node = this.head
            // console.log(this.head.next)
            while(current_node !== null){
                console.log(current_node.data)
                // console.log('ss')
                current_node = current_node.next
            }
        }
    }

    push(data){
        const new_node = new Node(data)
        if (this.head === null) {
            this.head = new_node
            // console.log('1: ',this.head)
            return
        }
        let current_node = this.head
        // console.log(current_node.next)
        while (this.head.next != null){
            this.head = current_node.next
            // console.log('2: ', current_node)
        }
        this.head = new_node
        // console.log('3: ',current_node)

    }
}

const list = new LinkedList()
list.push(1)
list.push(2)
list.print()