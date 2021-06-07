import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] person_1 = {1,2,3,4,5};
        int[] person_2 = {2,1,2,3,2,4,2,5};
        int[] person_3 = {3,3,1,1,2,2,4,4,5,5};
        int ans_1 = 0, ans_2 = 0, ans_3 = 0;
        
        for(int i = 0; i < answers.length; i++){
            if (person_1[i%person_1.length] == answers[i]) ans_1++;
            if (person_2[i%person_2.length] == answers[i]) ans_2++;
            if (person_3[i%person_3.length] == answers[i]) ans_3++;
        };
        
        int max = Math.max(Math.max(ans_1, ans_2),ans_3);
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(ans_1 == max) list.add(1);
        if(ans_2 == max) list.add(2);
        if(ans_3 == max) list.add(3);
        
        answer = new int[list.size()];
        
        for(int i=0; i < answer.length; i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}