/* What is the maximum number of squares of size 2x2 that can be fit in a right angled isosceles triangle of base B.
One side of the square must be parallel to the base of the isosceles triangle.
Base is the shortest side of the triangle
Input
First line contains T, the number of test cases.
Each of the following T lines contains 1 integer B.
Output
Output exactly T lines, each line containing the required answer.*/




#include <stdio.h>

int main() {
  setbuf(stdin, NULL);
  int t, b;
  scanf("%d", &t);
  while(t--) {
    scanf("%d", &b);
    printf("%d\n", find_squares(b));
  }
  return 0;
}

int find_squares(b) {
  int squares = 0;
  if(b < 4) {
    return 0;
  } else {
    squares = b/4;
    b -= squares * 2;
    squares = squares * squares;
    return squares + 2 * find_squares(b);
  }
}
