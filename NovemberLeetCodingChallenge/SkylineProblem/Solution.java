class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        /*
        idea: we create a new array as the entry/exit time for the buildings, first come first serve
        we also use a priority queue to store current all heights, and a hashmap to record their 
        their counter
        */
        int n = buildings.length;
        List<Integer[]>states = new ArrayList<>();
        for (int i=0; i<n; i++) {
            states.add(new Integer[] {buildings[i][0], -buildings[i][2]}); // entry serves first
            states.add(new Integer[] {buildings[i][1], buildings[i][2]});
        }
        
        // sort states
        Collections.sort(states, (a,b) -> {
            if (a[0]<b[0]) {
                return -1;
            } else if (a[0].equals(b[0])) {
                return a[1]-b[1];
            } else {
                return 1;
            }
        });
        
        Map<Integer, Integer> counter = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(); // push negative height for a maxheap
        counter.put(0, 1);
        pq.add(0); // ground
        
        int prev = 0; // previous height
        List<List<Integer>> res = new ArrayList<>();
        for (Integer[] l : states) {
            int pos = l[0];
            int h = l[1];
            if (h < 0) {
                // entry point
                pq.add(h);
                counter.put(h, counter.getOrDefault(h, 0) + 1);
            } else {
                // h > 0, exit point
                counter.put(-h, counter.get(-h)-1);
            }
            
            // pop out non-existing heights
            while (counter.get(pq.peek()) == 0) {
                pq.poll();
            }
            
            // if current height is not same as previous, we append
            if (pq.peek() != prev) {
                res.add(Arrays.asList(pos, -pq.peek()));
                prev = pq.peek();
            }
        }
        
        return res;
        
    }
}