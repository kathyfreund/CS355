import java.awt.Color;

public class SplitBall extends BasicBall
{
    public SplitBall(double r, Color c) //similar to BasicBall constructor
    {
        super(r, c);
        name = "SplitBall";
    }
    
    public SplitBall(BasicBall sb) //actual split
    {
        super(sb.radius,sb.color);
        name = "SplitBall";
    }
    
    @Override
    public int reset() 
    {
        rx = 0.0;
        ry = 0.0;  	
        vx = StdRandom.uniform(-0.01, 0.01); ///random speeds
        vy = StdRandom.uniform(-0.01, 0.01);
        return 2;
    }
    
    @Override
    public int getScore() 
    {
    	return 10; // A hit to a split ball will increase the player’s score by 10 points
    }
    
}