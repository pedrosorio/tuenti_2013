#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

//count of characters in hashable form 
//uses 2 bytes per count, assumes no string
//has more than 65535 equal characters
//(though even 1 byte would be reasonable for the
//described application)
string counter(string s) {
  string ret(52,1);
  for (int i = 0; i < s.size(); i++) {
    int c = s[i] - 'a';
    if (ret[2*c] == 0xff) {
      ret[2*c+1]++;
      ret[2*c] = 0;
    }
    else
      ret[2*c]++;
  }
  return ret;
}

//build hash charcounts -> dictionary_word_index
//and save them in a binary file
void preprocess_dictionary(string dicname) {
  unordered_map<string, vector<int> > count_map;
  ifstream file;
  string s;
  file.open(dicname.c_str());
  int nstr = 0, nct = 0;
  
  while(file >> s) {
    if (nstr%100000 == 0)
      cout << nstr << endl;
    string c = counter(s);
    if (count_map.find(c) != count_map.end())
      count_map[c].push_back(nstr);
    else {
      nct++;
      vector<int> v(1,nstr);
      count_map[c] = v;
    }
    nstr++;
  }
  file.close();
  
  ofstream fout;
  dicname += "_processed";
  fout.open(dicname, ios::out | ios::binary);
  fout.write((char*)&nct, sizeof(int));
  for(unordered_map<string, vector<int> >::iterator it = count_map.begin(); it != count_map.end(); it++) {
    fout.write(it->first.c_str(), 53);
    int sz = it->second.size();
    fout.write((char*)&sz, sizeof(int));
    for (int i = 0; i < it->second.size(); i++)
      fout.write((char*)&(it->second[i]), sizeof(int));
  }
  fout.close();
}
  
int main (int argc, char *argv[]) {
  //pass the name of a dictionary file to preprocess it
  if (argc == 2) {
      string s(argv[1]);
      preprocess_dictionary(s);
      return 0;
  }
  
  unordered_map<string, vector<int> > count_map;
  string s, dicname, procdicname;
  vector<string> dic;
  //get comment
  getline(cin, s);
  //get dictionary file name
  getline(cin, dicname);
  procdicname = dicname + "_processed";
  ifstream file, fileproc;
  file.open(dicname);
  fileproc.open(procdicname, ios::binary);
 
  //read dictionary words
  while(file >> s)
    dic.push_back(s);
  file.close();
  
  //read preprocessed dictionary
  int nct, nvec, aux;
  char str[53];
  fileproc.read((char*)&nct, sizeof(int));
  for(int i = 0; i < nct; i++) {
    fileproc.read(str, 53);
    s = "";
    s += str;
    fileproc.read((char*)&nvec, sizeof(int));
    vector<int> v;
    for (int j = 0; j < nvec; j++) {
      fileproc.read((char*)&aux, sizeof(int));
      v.push_back(aux);
    }
    count_map[s] = v;
  }
  fileproc.close();
  
  //get comment
  getline(cin, s);
  //get number of words to process
  int nwords;
  cin >> nwords;
  getline(cin, s);

  //get comment
  getline(cin, s);
  
  //process words
  for (int i = 0; i < nwords; i++) {
    cin >> s;
    vector<int> v = count_map[counter(s)];
    //(could sort in preprocess stage, but the number
    //of words per count is extremely small
    //max = 5 for bigDictionary)
    vector<string> vs;
    for (int j = 0; j < v.size(); j++)
      vs.push_back(dic[v[j]]);
    sort(vs.begin(), vs.end());
    cout << s << " ->";
    for (int j = 0; j < vs.size(); j++) {
      if (vs[j] != s)
	cout << ' ' << vs[j];
    }
    cout << endl;
  }
  return 0;
}
  
  
