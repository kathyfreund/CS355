public class Player
{
    private int hits;
    private int score;
    private String mosthitball;
    
    public Player() //starting off
    {
        hits = 0;
        score = 0;
        mosthitball = "";
    }

	//getters
    public int getHits()
    {
        return hits;
    }

    public int getScore()
    {
        return score;
    }

	//setters
    public String getmosthitball()
    {
        return mosthitball;
    }


    public void setmosthitball(String s)
    {
        mosthitball = s;
    }

	//functions
    public void updateScore(int x)
    {
        score = score + x;
    }


    public void ballhit()
    {
        ++hits;
    }
    
}














