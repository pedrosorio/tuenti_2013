#include <fstream>
#include <iostream>
#include <string>

using namespace std;

unsigned char c[1<<28];

int main() {
  string filename;
  int x;

  for (int i = 0; i < (1<<28); i++)
    c[i] = 0;
  
  cin >> filename;
  ifstream file;
  file.open(filename, ios::binary);
  
  unsigned int i=0;
  while(file.good()) {
    file.read((char*)&x, sizeof(int));
    c[x>>3] |= (1 << (x & 7));
    i++;
  }
  file.close();
  int missing = 0;
  x = 0;
  while (missing < 100) {
    if (!(c[x>>3] & (1 << (x & 7)))) {
      cout << x << endl;
      missing++;
    }
    x++;
  }
  
  return 0;
}