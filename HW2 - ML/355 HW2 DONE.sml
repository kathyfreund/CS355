(* HELPER FUNCTIONS *)
fun reversingLists([]) = []
    | reversingLists(x::rest) = 
        rev(x)::reversingLists(rest);

fun map f [] = []
    | map f (x::rest) = 
        (f x)::(map f rest);

fun inList (n,[]) = false
    | inList(n,x::rest) = 
        if n=x 
            then true 
        else inList(n,rest);

fun removeDuplicates [] = []
    | removeDuplicates (x::rest) = 
        if inList(x,rest) 
            then (removeDuplicates rest)
        else x::(removeDuplicates rest);
        
fun fold f base [] = base
    | fold f base (x::rest) = 
        f x (fold f base rest);
        
        
        
        
        
        
        
        
        



(* ---------- PROBLEM 1 ---------- *)
(* 1.A - WORKING *)
fun countInList [] x = 0
	| countInList (y::rest) x = 
		if x = y
			then 1 + (countInList rest x)
		else
			countInList rest x;
			


(* 1.B - WORKING *)
fun zipTailHelper [] L2 newL = newL
    | zipTailHelper L1 [] newL = newL
    | zipTailHelper (x::restx) (y::resty) newL = 
        zipTailHelper restx resty ((x,y)::newL);

fun zipTail L1 L2 =
    rev(zipTailHelper L1 L2 []);
		   
		
(* 1.C - WORKING *)		
fun histogram [] = []
    | histogram L1 = 
        removeDuplicates (zipTail L1 (map (countInList L1) L1));

    










(* ---------- PROBLEM 2 ---------- *)
(* 2.A - WORKING *)
fun f1 x y = x + y;

fun deepSum [] = 0
    | deepSum L = 
        fold f1 0 (map (fold f1 0) L); (* little fold sums up all the sublists, outer fold sums up the whole list *)




(* 2.B - WORKING *)
fun f2 (NONE) (NONE) = NONE
    | f2 (SOME(x)) (NONE) = SOME(x)
    | f2 (NONE) (SOME(y)) = SOME(y)
    | f2 (SOME(x)) (SOME(y)) = SOME(x+y);


fun deepSumOption [] = NONE
    | deepSumOption L =  
        fold f2 NONE (map (fold f2 NONE) L);
    
    
    



    
    
    
    
    
    
    
    
(* ---------- PROBLEM 3 ---------- *)
(* WORKING *)	
fun unzip [] = [[],[]] 
    | unzip L = [map (fn (x,_) => x) L, map (fn (_,y) => y) L];  (* fn (x,_) returns first element, fn (_,y) returns second element *)
















(* ---------- PROBLEM 4 ---------- *)
(* 4.AB - WORKING *)
datatype either = ImAString of string | ImAnInt of int;
datatype eitherTree = eLEAF of either | eINTERIOR of (either*eitherTree*eitherTree);


(* 4.C - WORKING *)
fun eitherSearch (eLEAF(ImAString(_))) _ = false
    | eitherSearch(eLEAF(ImAnInt(value))) x = (x = value)
	| eitherSearch(eINTERIOR(ImAString(_), t1, t2)) x =  ((eitherSearch t1 x) orelse (eitherSearch t2 x))
	| eitherSearch(eINTERIOR(ImAnInt(value), t1, t2)) x =
		if x = value
			then true
		else
			((eitherSearch t1 x) orelse (eitherSearch t2 x));


(* 4.D - WORKING *)
fun eitherTest() = 
    let     (* TRIED DOING IT WITHOUT A LOOP BUT IT YELLS AT ME :( *)
        val testing = eINTERIOR(ImAnInt(1), eINTERIOR(ImAString("2"), eLEAF(ImAnInt(4)), eINTERIOR(ImAString("5"), eLEAF(ImAString("8")), eLEAF(ImAnInt(9)))), eINTERIOR(ImAString("3"), eINTERIOR(ImAString("6"), eLEAF(ImAnInt(10)), eLEAF(ImAString("11"))), eLEAF(ImAnInt(7))))
  
        val test1 = (eitherSearch testing 1) = true
        val test4 = (eitherSearch testing 4) = true
        val test5 = (eitherSearch testing 5) = false
        val test7 = (eitherSearch testing 7) = true
        val test11 = (eitherSearch testing 11) = false
        val test12 = (eitherSearch testing 12) = false
    in
        print("\nTesting eitherSearch:-------------------- \nTest1: " ^ Bool.toString(test1) ^ "\n" ^ "Test4: " ^ Bool.toString(test4) ^ "\n" ^ "Test5: " ^ Bool.toString(test5) ^ "\n" ^ "Test7: " ^ Bool.toString(test7) ^ "\n" ^ "Test11: " ^ Bool.toString(test11) ^ "\n" ^ "Test12: " ^ Bool.toString(test12) ^ "\n\n")
    end;
    





(* ---------- PROBLEM 5 ---------- *)
(* 5.A - WORKING *)
datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) * ('a Tree);
datatype 'a myTree = myLEAF of 'a | myNODE of 'a*'a*('a myTree)*('a myTree);


fun findMin (LEAF v) = v
	| findMin (NODE (left, right)) = Int.min((findMin left), (findMin right));
	
fun findMax (LEAF v) = v
	| findMax (NODE (left, right)) = Int.max((findMax left), (findMax right));






(* 5.B - WORKING *)
fun minmax (LEAF(v)) = myLEAF(v)
    | minmax (NODE(t1,t2)) = 
        myNODE((findMin (NODE(t1,t2))), (findMax (NODE(t1,t2))), (minmax t1), (minmax t2));
    
    

(* 5.C - WORKING *)
(* HAD TO MAKE TWO PRINTING FUNCTIONS, ONE FOR TREE AND ONE FOR MYTREE *)
fun postTree (LEAF(z)) = (Int.toString(z) ^ " ")
    | postTree (NODE(x, y)) = (postTree x) ^ (postTree y);
    
fun postTree2 (myLEAF(z)) = (Int.toString(z) ^ " ")
    | postTree2 (myNODE(min, max, x, y)) = ("(" ^ Int.toString(min) ^ "," ^ Int.toString(max) ^ ") " ^ (postTree2 x) ^ (postTree2 y));
    
fun minmaxTree tt = 
    print("Testing: " ^ (postTree tt) ^ "\nTested: " ^ (postTree2 (minmax tt)) ^ "\n");


val tree1 = NODE(NODE(LEAF(7), NODE(LEAF(8), LEAF(9))), NODE(NODE(LEAF(10), LEAF(11)), LEAF(12)));
val tree2 = NODE(NODE(NODE(LEAF(27), LEAF(50)), NODE(LEAF(61), LEAF(72))), LEAF(89));
val tree3 = NODE(NODE(NODE(LEAF(0), LEAF(9)), LEAF(6)), NODE(LEAF(3), LEAF(10)));

















(* TEST FUNCTIONS *)
print(" ---------- TESTING FUNCTIONS ---------- \n\n");


fun countInListTest () = 
    let
        val cil1 = (countInList ["3","5","5","-","4","5","1"] "5") = 3;
        val cil2 = (countInList [] "5") = 0;
        val cil3 = (countInList [true, false, false, false, true, true, true] true) = 4;
        val cil4 = (countInList [[],[1,2],[3,2],[5,6,7],[8],[]] []) = 2;
    in
        print("\nTesting countInList:-------------------- \nTest1: " ^ Bool.toString(cil1) ^ "\nTest2: " ^ Bool.toString(cil2) ^ "\nTest3: " ^ Bool.toString(cil3) ^ "\nTest4: " ^ Bool.toString(cil4) ^ "\n\n")
    end;
val _ = countInListTest();









fun zipTailTest () =
    let
        val zip1 = ((zipTail [1,2,3,4,5] ["one","two"]) = [(1,"one"),(2,"two")])
        val zip2 = ((zipTail [1] [1,2,3,4]) = [(1,1)])
        val zip3 = ((zipTail [1,2,3,4,5] []) = [])
        val zip4 = ((zipTail [] [1,2,3,4,5]) = [])
    in
        print("\nTesting zipTail:-------------------- \nTest1: " ^ Bool.toString(zip1) ^ "\nTest2: " ^ Bool.toString(zip2) ^ "\nTest3: " ^ Bool.toString(zip3) ^ "\nTest4: " ^ Bool.toString(zip4) ^ "\n\n")
    end;
val _ = zipTailTest();









fun histogramTest() =
    let
        val h1 = ((histogram [1,3,2,2,3,0,3]) = [(1,1), (2,2), (0,1), (3,3)])
        val h2 = ((histogram [[1,2],[3],[],[3],[1,2]]) = [([], 1), ([3], 2), ([1,2],2)])
        val h3 = ((histogram []) = [])
        val h4 = ((histogram [true, false, false, false, true, true, true]) = [(false, 3), (true, 4)])
    in
        print("\nTesting histogram:-------------------- \nTest1: " ^ Bool.toString(h1) ^ "\nTest2: " ^ Bool.toString(h2) ^ "\nTest3: " ^ Bool.toString(h3) ^ "\nTest4: " ^ Bool.toString(h4) ^ "\n\n")
    end;
val _ = histogramTest();









fun deepSumTest() = 
    let
        val ds1 = (deepSum [[1,2,3],[4,5],[6,7,8,9],[]]) = 45;
        val ds2 = (deepSum [[10,10],[10,10,10],[10]]) = 60;
        val ds3 = (deepSum [[]]) = 0;
        val ds4 = (deepSum []) = 0;
    in
        print("\nTesting deepSum:-------------------- \nTest1: " ^ Bool.toString(ds1) ^ "\nTest2: " ^ Bool.toString(ds2) ^ "\nTest3: " ^ Bool.toString(ds3) ^ "\nTest4: " ^ Bool.toString(ds4) ^ "\n\n")
    end;
val _ = deepSumTest();









fun deepSumOptionTest() = 
    let
        val dso1 = (deepSumOption [[SOME(1),SOME(2),SOME(3)],[SOME(4),SOME(5)],[SOME(6),NONE],[],[NONE]]) = SOME(21);  
        val dso2 = (deepSumOption [[SOME(10),NONE],[SOME(10), SOME(10), SOME(10),NONE,NONE]]) = SOME(40);
        val dso3 = (deepSumOption [[NONE]]) = NONE;
        val dso4 = (deepSumOption []) = NONE;
    in
        print("\nTesting deepSumOption:-------------------- \nTest1: " ^ Bool.toString(dso1) ^ "\nTest2: " ^ Bool.toString(dso2) ^ "\nTest3: " ^ Bool.toString(dso3) ^ "\nTest4: " ^ Bool.toString(dso4) ^ "\n\n")
    end;
val _ = deepSumOptionTest();









fun unzipTest() = 
    let
        val u1 = (unzip [(1,2),(3,4),(5,6)]) = [[1,3,5], [2,4,6]];
        val u2 = (unzip [("1","a"),("5","b"),("8","c")]) = [["1", "5", "8"], ["a", "b", "c"]];
    in
        print("\nTesting unzip:-------------------- \nTest1: " ^ Bool.toString(u1) ^ "\nTest2: " ^ Bool.toString(u2) ^ "\n\n")
    end;
val _ = unzipTest();







eitherTest();










fun findMinTest() = 
    let
        val fm1 = (findMin (NODE(NODE(LEAF(5),NODE(LEAF(6),LEAF(8))),LEAF(4)))) = 4;
        val fm2 = (findMin (NODE(NODE(NODE(LEAF(0),LEAF(11)),LEAF(6)),NODE(LEAF(3),LEAF(10))))) = 0;
        val fm3 = (findMin (LEAF(5))) = 5;
    in
        print("\nTesting findMin:-------------------- \nTest1: " ^ Bool.toString(fm1) ^ "\nTest2: " ^ Bool.toString(fm2) ^ "\nTest3: " ^ Bool.toString(fm3) ^ "\n\n")
    end;
val _ = findMinTest();









fun findMaxTest() = 
    let
        val fmx1 = (findMax (NODE(NODE(LEAF(5),NODE(LEAF(6),LEAF(8))),LEAF(4)))) = 8;
        val fmx2 = (findMax (NODE(NODE(NODE(LEAF(0),LEAF(11)),LEAF(6)),NODE(LEAF(3),LEAF(10))))) = 11;
        val fmx3 = (findMax (LEAF(5))) = 5;
    in
        print("\nTesting findMax:-------------------- \nTest1: " ^ Bool.toString(fmx1) ^ "\nTest2: " ^ Bool.toString(fmx2) ^ "\nTest3: " ^ Bool.toString(fmx3) ^ "\n\n")
    end;
val _ = findMaxTest();






print("\nTesting minmaxTree:-------------------- \n");
minmaxTree tree1;
minmaxTree tree2;
minmaxTree tree3;

