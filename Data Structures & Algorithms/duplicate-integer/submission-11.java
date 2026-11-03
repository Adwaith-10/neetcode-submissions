class Solution{
    public Boolean hasDuplicate(int[]nums){
        Set<Integer> seen=new HashSet<>();
        for(int num :nums){
            if(seen.contains(num)){
                return true;
            }
            else{
                seen.add(num);
            }
        }
        return false;
    }
}