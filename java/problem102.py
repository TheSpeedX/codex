string[] lines = File.ReadAllLines(filename);
int result = 0;
 
foreach (string line in lines) {
    //Parse the line
    string[] segments = line.Split(',');
    int[,] coordinates = new int[2, segments.Length/2];
 
    int[] A = {Convert.ToInt32(segments[0]) ,
               Convert.ToInt32(segments[1])};
    int[] B = {Convert.ToInt32(segments[2]) ,
               Convert.ToInt32(segments[3])};
    int[] C = {Convert.ToInt32(segments[4]) ,
               Convert.ToInt32(segments[5])};
    int[] P = {0,0};
 
    if (area(A, B, C) ==
        area(A, B, P) +
        area(A, P, C) +
        area(P, B, C))
        result++;
}
