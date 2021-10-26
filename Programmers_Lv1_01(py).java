class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        boolean check = false;

        for(int i=0; i < nums.length; i++){
            for(int j=i+1; j < nums.length; j++){
                for(int k=j+1; k < nums.length; k++){
                    int num = nums[i] + nums[j] + nums[k];
                    if (isSosu(num)){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
    
    public boolean isSosu(int num){
        int max_len = (int)Math.sqrt(num) + 1;
        for(int i=2; i <= max_len; i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}