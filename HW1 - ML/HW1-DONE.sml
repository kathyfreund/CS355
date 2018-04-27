(* LINKS *)
(* http://rigaux.org/language-study/syntax-across-languages-per-language/SML.html *)




(*Helper functions - NOTE: tried using L.take, L.drop, and L.length but did not work :( *)
fun drop(xs, n) =							(* https://gist.github.com/edalorzo/4670775 *)
	if n < 0 then raise Subscript
	else if n = 0 then xs
	else 
		case xs of 
			[] => []
		  | (_::xs') => drop(xs', n-1);

fun take(xs, n) =
	if n < 0 
	then raise Subscript
	else 
		case xs of 
			[] => []
		  | (x::xs') => if n > 0 then x::take(xs',n-1) else [];

fun len(xs) =								
	case xs of
		[] => 0
	 | (_::xs') => 1 + len(xs')

fun reversingLists([]) = []
    | reversingLists(x::rest) = 
        rev(x)::reversingLists(rest);















(* DONE - WORKING ====== Problem 1 ====== *)
fun inList (x, []) = false							(* should be [‘’a * ‘’a] because they need to be comparable types *)
	| inList (x, y::rest) =							(* x = value to find, y = head of list, rest = rest of the list *)
		if y = x 
			then true						
		else 
			inList(x, rest);					(* should return bool *)

fun inListTesting (n, L, output) =
	if inList(n, L) = output then true else false;
		
val inListTest1 = inListTesting(1,[], false);
val inListTest2 = inListTesting(1,[1,2,3], true);
val inListTest3 = inListTesting([1],[[1]], true);
val inListTest4 = inListTesting([1], [[3],[5]], false);
val inListTest5 = inListTesting("c", ["b","c","z"], true);











				


(* DONE - WORKING ====== Problem 2 ======*)		
fun removeDuplicates ([]) = []
	| removeDuplicates(x::rest) = 
	    if inList(x, rest)
			then removeDuplicates(rest)			(* skip over *)
		else 
			x::removeDuplicates(rest);

fun removeDuplicatesTesting (L, output) =
	if removeDuplicates(L) = output then true else false;
		
val removeDuplicatesTest1 = removeDuplicatesTesting([1,5,1,3,4,3,5], [1,4,3,5]);
val removeDuplicatesTest2 = removeDuplicatesTesting(["a","e","c","a","a","b","c","d"], ["e","a","b","c","d"]);
val removeDuplicatesTest3 = removeDuplicatesTesting([],[]);














(* DONE - WORKING ====== Problem 3 ====== *)
fun listIntersect([],l) = []
    | listIntersect((x::rest),l) = 
        if inList(x,l) 
            then removeDuplicates(x::listIntersect(rest,l)) 
        else  
            listIntersect(rest,l);


fun listIntersectTesting (L1, L2, output) =
	if listIntersect(L1, L2) = output then true else false;
		
val listIntersectTest1 = listIntersectTesting([1], [1], [1]);
val listIntersectTest2 = listIntersectTesting([1,2,3], [1,1,2], [1,2]);
val listIntersectTest3 = listIntersectTesting([[2,3],[1,2],[2,3]], [[1],[2,3]], [[2,3]]);
val listIntersectTest4 = listIntersectTesting([1,2,3], [], []);














(* DONE - WORKING ====== Problem 4 ====== *)
fun range min step max =
	if min >= max andalso step >= 0
		then []
	else if min <= max andalso step <= 0
		then []
	else
	    min::(range (min+step) step max);


fun rangeTesting(min, step, max, output) =
	if (range min step max) = output then true else false;
		
val rangeTest1 = rangeTesting(0, 5, 30, [0,5,10,15,20,25]);
val rangeTest2 = rangeTesting(10, 1, 10, []);
val rangeTest3 = rangeTesting(5, ~1, 0, [5,4,3,2,1]);
val rangeTest4 = rangeTesting(1, ~1, 10, []);














(* DONE - WORKING ====== Problem 5 ====== *)
fun numbersToSum sum [] = []
	| numbersToSum sum (x::rest) = 
		if x >= sum
			then []
		else
		    x::(numbersToSum (sum-x) rest);


fun numbersToSumTesting(sum, L, output) =
	if (numbersToSum sum L) = output then true else false;
		
val numbersToSumTest1 = numbersToSumTesting(100, [10, 20, 30, 40], [10, 20, 30]);
val numbersToSumTest2 = numbersToSumTesting(30, [5, 4, 6, 10, 4, 2, 1, 5], [5, 4, 6, 10, 4]);
val numbersToSumTest3 = numbersToSumTesting(1, [2], []);
val numbersToSumTest4 = numbersToSumTesting(1, [], []);















(* DONE - WORKING ====== Problem 6 - replace ====== *)
fun replace index value [] = []
    | replace index value (x::rest) =
        if index = 0
            then (value::rest)
	    else

	        x::(replace (index-1) value rest);


fun replaceTesting(index, value, L, output) =
	if (replace index value L) = output then true else false;
		
val replaceTest1 = replaceTesting(3, 40, [1, 2, 3, 4, 5, 6], [1, 2, 3, 40, 5, 6]);
val replaceTest2 = replaceTesting(0, "X", ["a", "b", "c", "d"], ["X", "b", "c", "d"]);
val replaceTest3 = replaceTesting(4, false, [true, false, true, true, true], [true, false, true, true, false]);


















(*DONE - WORKING ====== Problem 7.1 - groupNleft ====== *) 			
fun groupNright n [] = [[]]
    | groupNright n L =
    if len(L) > n
        then take(L, n)::(groupNright n (drop(L, n)))
    else
        [L];


fun groupNrightTesting(n,L,output) =
	if (groupNright n L) = output then true else false;

val groupNrightTest1 = groupNrightTesting(2,[1,2,3,4,5],[[1,2],[3,4],[5]]);
val groupNrightTest2 = groupNrightTesting(3,[1,2,3,4,5],[[1,2,3],[4,5]]);














(* DONE - WORKING====== Problem 7.2 - groupNright ====== *)
fun groupNleft n L = 
    reversingLists(rev(groupNright n (rev(L))));

fun groupNleftTesting (n,L,output) =
	if (groupNleft n L) = output then true else false;

val groupNleftTest1 = groupNleftTesting(2,[1,2,3,4,5],[[1],[2,3],[4,5]]);
val groupNleftTest1 = groupNleftTesting(3,[1,2,3,4,5],[[1,2],[3,4,5]]);





