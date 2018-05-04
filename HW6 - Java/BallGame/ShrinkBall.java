import java.awt.Color;

public class ShrinkBall extends BasicBall
{
    private double or; //original radius

	public ShrinkBall(double r, Color c) //similar to BasicBall constructor
	{
		super(r, c);
		or = r;
		name = "ShrinkBall";
	}

	public boolean isHit(double x, double y) //same as in BasicBall
	{
		if((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) 
		{
			return true;
		}
		return false;
	}
	
	@Override
	public int reset()  //This is a larger ball which gets smaller by 33% (i.e., 2/3 of the original size) each time the player hits it. 
	{
		if(radius <= 0.5*or) //When the ball size is less than or equal to 25% of the initial size the ball, the ball will be reset to its original size 
		{
			radius = or; //when radius is halved, area of circle becomes 1/4 original area
		}
		else //cut by 1/3
		{
			radius = radius * 0.8165; //square root of 2/3 * original radius
		}
		return super.reset();
	}
	
	@Override
	public int getScore()
	{
		return 20; //A hit to a shrink ball will increase the player’s score by 20 points.
	}

}