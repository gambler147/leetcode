class Solution {
    public int minJumps(int[] arr) {
        // use a hashmap to record a list of positions in each list
        int n = arr.length;
        Map<Integer, List<Integer>> posmap = new HashMap<>();
        for (int i=0; i<n; i++) {
            if (!posmap.containsKey(arr[i])) {
                posmap.put(arr[i], new ArrayList<>());
            }
            posmap.get(arr[i]).add(i);
        }
        
        // bfs
        List<Integer> l = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Set<Integer> visited_val = new HashSet<>();
        l.add(0);
        visited.add(0);
        
        int res = 0;
        while (l.size() > 0) {
            List<Integer> tmp = new ArrayList<>();
            for (int idx : l) {
                if (idx == n-1) {
                    return res;
                }
                
                // push idx - 1 and idx + 1 to tmp if not visited
                if (idx - 1 >= 0 && (!visited.contains(idx-1))&& (!visited_val.contains(arr[idx-1]))) {
                    tmp.add(idx-1);
                    visited.add(idx-1);
                }
                
                if (idx + 1 < n && (!visited.contains(idx+1)) && (!visited_val.contains(arr[idx+1]))) {
                    tmp.add(idx+1);
                    visited.add(idx+1);
                }
                
                // push indices j where arr[j] == arr[idx] to tmp
                if (!visited_val.contains(arr[idx])) {
                    visited_val.add(arr[idx]);
                    List<Integer> js = posmap.get(arr[idx]);
                    for (int j : js) {
                        if (!visited.contains(j)) {
                            tmp.add(j);
                            visited.add(j);
                        }
                    }
                }
            }
            res++;
            l = tmp;
        }
        return -1;
    }
}
