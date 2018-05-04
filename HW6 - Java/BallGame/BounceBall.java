import java.awt.Color;

public class BounceBall extends BasicBall
{
    private int bounces;
    
    public BounceBall(double r, Color c) //similar to BasicBall constructor
    {
        super(r, c);
        bounces = 0;
        name = "BounceBall";
    }
    
    
    @Override
    public void move() //same as function in BasicBall, except we need to keep track of bounces
    {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        {
            if (bounces <= 3) 
            {
                if (Math.abs(rx) > 1.0) //Please note that the direction (sign) of the speed will change due to the bounce
                {
                    vx *= -1.0;
                }
                else 
                {
                    vy *= -1.0;
                }
                bounces++;
            }
            else 
            {
                isOut = true;
            }
        }
    }
    
    
    @Override
    public int getScore() //A hit to a bounce ball will increase the player’s score by 15 points
    {
    	return 15;
    }
    
    
}