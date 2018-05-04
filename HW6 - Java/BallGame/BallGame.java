/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.io.*;
import java.util.*;

public class BallGame { 

    public static void main(String[] args) {
  
        if(args.length == 0)
        {
            System.out.println("Arguments Missing! Please enter # of balls,(ball type, ball radius).");
            System.out.println("For example: '4 basic 0.10 bounce 0.05 shrink 0.13 split 0.05'");
            return;
        }
  
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	Player p = new Player();
		//stored in hashtable to be able to call upon them by name instead of iterating a list
        HashMap<String, Integer> ballsHit = new HashMap<String, Integer>(); //https://docs.oracle.com/javase/7/docs/api/java/util/Hashtable.html
        ballsHit.put("BasicBall", 0);
        ballsHit.put("ShrinkBall", 0);
        ballsHit.put("BounceBall", 0);
        ballsHit.put("SplitBall", 0);
    	
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
   		ArrayList<BasicBall> balls = new ArrayList<BasicBall>(numBalls);
        for (int i=0; i<numBalls; i++)
        {
            switch (ballTypes[i].toLowerCase()) //https://docs.oracle.com/javase/7/docs/api/java/awt/Color.html
            {
                case "basic":
                    balls.add(new BasicBall(ballSizes[i], Color.RED));
                    break;
                case "shrink":
                    balls.add(new ShrinkBall(ballSizes[i], Color.BLUE));
                    break;
                case "bounce":
                    balls.add(new BounceBall(ballSizes[i], Color.GREEN));
                    break;
                case "split":
                    balls.add(new SplitBall(ballSizes[i], Color.YELLOW));
                    break;
                default: //for whatever reason breaks
                    return;
            }
        }
   		
        
        
        //TO DO: initialize the numBallsinGame
   		numBallsinGame = balls.size(); //???
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) { //game is running

        	// TODO: move all balls
            for (BasicBall ball : balls)
            {
                ball.move(); //move one step
            }

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed())
            {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                for(int i = 0; i < balls.size(); i++) //go through list 
                {
                    if (balls.get(i).isHit(x,y))
                    {
                        int numBallsReset = balls.get(i).reset();
                        if (numBallsReset == 2)
						{
							balls.add(new SplitBall(balls.get(i)));
						}
                        //ball.reset();
                        //TO DO: Update player statistics
                        p.ballhit();
						p.updateScore(balls.get(i).getScore());
                        String hashKey = balls.get(i).name;
                        ballsHit.put(hashKey, ballsHit.get(hashKey) + 1);
                        int mostHits = Collections.max(ballsHit.values());
                        for (Map.Entry<String, Integer> entry : ballsHit.entrySet())
                        {
                            if (entry.getValue() == mostHits)
                            { 
                                p.setmosthitball(entry.getKey()); 
                                break;
                            }
                        }
                    }
                }
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. Game should hold the number of visible balls in the game.  
            for (BasicBall ball : balls)
            {
                if (ball.isOut == false) { 
                    ball.draw();
                    numBallsinGame++;
                }
            }
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 15);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics
			StdDraw.text(-0.72, 0.84, "Number of hits: "+ String.valueOf(p.getHits()));
			StdDraw.text(-0.80, 0.78, "Score: "+ String.valueOf(p.getScore()));
			StdDraw.text(-0.60, 0.72, "Ball Type with Most Hits: "+ p.getmosthitball());

            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
