class FrontMiddleBackQueue {
    /*
    using two deques, each time we push a new val, we balance the size of two queues
    to make sure front_deque.size() == back_deque.size() or back_deque.size() + 1
    */
    Deque<Integer> front_deque;
    Deque<Integer> back_deque;
    public FrontMiddleBackQueue() {
        front_deque = new ArrayDeque<>();
        back_deque = new ArrayDeque<>();
    }
    
    public void pushFront(int val) {
        this.front_deque.addFirst(val);
        if (this.front_deque.size() > this.back_deque.size()) {
            int front_tail = this.front_deque.pollLast();
            this.back_deque.addFirst(front_tail);
        }
    }
    
    public void pushMiddle(int val) {
        if (this.front_deque.size() == this.back_deque.size()) {
            this.back_deque.addFirst(val);
        } else {
            this.front_deque.addLast(val);
        }
    }
    
    public void pushBack(int val) {
        this.back_deque.addLast(val);
        if (this.back_deque.size() > this.front_deque.size() + 1) {
            int back_head = this.back_deque.pollFirst();
            this.front_deque.addLast(back_head);
        }
    }
    
    public int popFront() {
        if (this.front_deque.size() == 0) {
            if (this.back_deque.size() == 0) return -1;
            return this.back_deque.pollFirst();
        }
        int front = this.front_deque.pollFirst();
        if (this.front_deque.size() < this.back_deque.size() - 1) {
            int back_head = this.back_deque.pollFirst();
            this.front_deque.addLast(back_head);
        }
        return front;
    }
    
    public int popMiddle() {
        if (this.back_deque.size() == 0) return -1;
        if (this.front_deque.size() == this.back_deque.size()) {
            return this.front_deque.pollLast();
        } else {
            return this.back_deque.pollFirst();
        }
    }
    
    public int popBack() {
        if (this.back_deque.size() == 0) return -1;
        int back = this.back_deque.pollLast();
        if (this.front_deque.size() > this.back_deque.size()) {
            int front_tail = this.front_deque.pollLast();
            this.back_deque.addFirst(front_tail);
        }
        return back;
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param_4 = obj.popFront();
 * int param_5 = obj.popMiddle();
 * int param_6 = obj.popBack();
 */