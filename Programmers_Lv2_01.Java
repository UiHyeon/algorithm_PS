import java.util.*;

class Solution {
    private static ArrayList<Edge>[] graph;
    private static int[] distance;
    
    private static void dijkstra(){
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        queue.add(new Edge(1, 0));
        while(!queue.isEmpty()){
            Edge edge = queue.poll();
            int node = edge.vertex;
            int weight = edge.weight;
            if(distance[node] < weight){
                continue;
            }
            for(int i=0; i < graph[node].size(); i++){
                int new_node = graph[node].get(i).vertex;
                int new_weight = graph[node].get(i).weight + weight;
                if(distance[new_node] > new_weight){
                    distance[new_node] = new_weight;
                    queue.add(new Edge(new_node, new_weight));
                }
            }
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        graph = new ArrayList[N + 1];
        distance = new int[N+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        
        for(int i=0; i<=N; i++){
            graph[i] = new ArrayList<>();
        }
        for(int i=0; i < road.length; i++){
            graph[road[i][0]].add(new Edge(road[i][1], road[i][2]));
            graph[road[i][1]].add(new Edge(road[i][0], road[i][2]));
        }
        
        distance[1] = 0;
        dijkstra();
        
        for(int i=0; i < distance.length; i++){
            if(distance[i] <= K){
                answer++;
            }
        }
        return answer;
    }
    private static class Edge implements Comparable<Edge> {
        int vertex; //
        int weight; //배달주문 시간

        public Edge(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return weight - o.weight;
        }
    }
}