#include <vector>
#include <iostream>
#include <utility>
#include <cmath>

using namespace std;

int from[50000];
int to[50000];
double w[50000];
double d[50000];
vector<int> edf[50000];
int lab[50000];
int tolab[50000];

int main() {
  int N,V,E;
  cin >> N;
  for(int testcase=0;testcase<N;testcase++) {
    
    cin >> V;
    for (int i = 0; i < V; i++) {
      d[i] = 1<<16; // larger than - log(0.8) * 50000
      edf[i].clear();
    }
    
    cin >> E;
    int x,y,p;
    for (int i = 0; i < E; i++) {
      cin >> x >> y >> p;
      from[i] = x;
      to[i] = y;
      edf[x].push_back(i);
      //negative log weights -> negative cycle implies always increasing energy
      w[i] = -log(0.01*(100+p));
    }
    
    
    int inf = 0;
    int nlab;
    int ntolab;
    bool hasinf = true;
    int *alab, *atolab, *aux;
    //while there is an unexplored node
    while(hasinf) {  
      d[inf] = 0;
      nlab = 1;
      lab[0] = inf;
      alab = lab;
      atolab = tolab;
      //cycle V times or until there are no more nodes to expand
      for (int i = 0; i < V && nlab > 0; i++) {
	ntolab = 0;
	//cycle all the edges going from nodes that need to be expanded
	for (int k = 0; k < nlab; k++) {
	  for(int l = 0; l < edf[alab[k]].size(); l++) {
	    int j = edf[alab[k]][l];
	    //if the distance to a node is updated, add it to the nodes to expanded in the next iteration 
	    if (d[from[j]] + w[j] < d[to[j]]) {
	      atolab[ntolab++] = to[j];
	      d[to[j]] = d[from[j]] + w[j];
	    }
	  }
	}
	//switch pointers between "nodes to expand on this iteration" and "nodes to expand on the next iteration"
	aux = alab;
	alab = atolab;
	atolab = aux;
	nlab = ntolab;
      }
      
      //find whether there is some edge which still gives a shorter path after V iterations, if so, there is a negative cycle
      bool neg = false;
      for (int k = 0; k < nlab && !neg; k++) {
	for (int l = 0; l < edf[alab[k]].size(); l++) {
	  int j = edf[alab[k]][l];
	  if (d[from[j]] + w[j] < d[to[j]])
	    neg = true;
	}
      }
      
      
      if (neg) {
	cout << "True" << endl;
	break;
      }
      
      //find whether there is still some vertex node explored (which could lead to a negative cycle)
      hasinf = false;
      for (int i = 0; i < V; i++) {
	if (d[i] == 1<<16) {
	  hasinf = true;
	  inf = i;
	}
      }
      
      if (!hasinf) {
	cout << "False" << endl;
	break;
      }
    }
  }
}