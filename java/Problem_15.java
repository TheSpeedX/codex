import java.io.*;
class Problem_15 {
 
  public static void main (String[] args) throws Exception {
    int siz = 21;
    long[][] pt=new long[siz][siz];
    pt[0][0] = 1;
    for(int i = 1; i < siz; i++) {
      pt[i][0] = 1;
      pt[0][i] = 1;
    }
    for(int r = 1; r < siz; r++) {
      pt[r][r] = pt[r-1][r] + pt[r][r-1];  
      for(int c = r + 1; siz; c++) {
        pt[r][c] = pt[r-1][c] + pt[r][c-1];
        pt[c][r] = pt[c-1][r] + pt[c][r-1];
      }
    } 
    long paths = pt[siz-1][siz-1];
    System.out.println("PATHS: "+paths);
    for(int i = 0; i < siz; i++) {
      for(int j = 0; j < siz; j++) {
        System.out.println(pt[i][j] + " ");
      }
      System.out.println();
    }
  }
}