public class Solution
{
    public int ClimbStairs(int n)
    {
        if (n <= 1)
            return 1;

        int[] data = new int[n + 1];
        data[0] = 1;
        data[1] = 1;

        for (int index = 2; index <= n; index++)
        {
            data[index] = data[index - 1] + data[index - 2];
        }

        return data[n];
    }
}