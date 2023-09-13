class Node {
    constructor (value){
        this.value = value;
        this.next = null;
    }
}

class SLL {
    constructor (data) {
        this.head = null;
    }

    addToFront (data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
        return this;
    }

    removeFromFront () {
        if(this.head){
            let newHead = this.head.next;
            this.head = newHead
        }
        return this;
    }

    showFrontValue () {
        if(this.head){
            console.log(this.head.value);
        }else{
            console.log(null);
        }
        return this;
    }

    displayAllValues () {
            let runner = this.head;
            let allNodeValues = '';
    
            while (runner) {
                allNodeValues += runner.value.toString();
                if(runner.next) {
                    allNodeValues += ', ';
                }
                runner = runner.next;
            }
            return allNodeValues;
        }

}

List1 = new SLL();
console.log(List1.addToFront(5).addToFront(10).addToFront(20).addToFront(40))
console.log(List1.displayAllValues())
