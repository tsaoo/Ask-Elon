#include <iostream>
#include <cctype>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
/*#include <pybind11/pybind11.h>

namespace py = pybind11;
*/
using namespace std;

int main(int argc, char *argv[]) {
    string fileIn = "tweets.txt";
    string fileOut = "clean.txt";

    ifstream f;

    f.open(fileIn);


    string namesIn[10000];
    int count = 0;
    while (!f.eof()) {
        f >> namesIn[count];
        count++;        
    }
    f.close();

    for (int j = 0; j < count; j++) {
        if (namesIn[j][0] == '{') {
            namesIn[j].erase(0, 11);
        }
        if (namesIn[j][0]) {
            if (namesIn[j][1] == '@' || namesIn[j][0] == '@' || namesIn[j][0] == ':') {
                namesIn[j].erase(0, namesIn[j].size());
        }
        }
    }
    for (int j = 0; j < count; j++) {
        for (size_t k = 0; k < namesIn[j].size()+1; k++) {
            if (namesIn[j][k] >= 65 && namesIn[j][k] <= 90) {
                namesIn[j][k] = tolower(namesIn[j][k]);
            }
            else if (namesIn[j][k] < 97 || namesIn[j][k] > 122) {
                namesIn[j].erase(k, k+1);
            }
        }
    }

    ofstream out (fileOut);

    for (int a = 0; a < count; a++) {
        if (namesIn[a].size() <= 2 || isalpha(namesIn[a][0]) == false || (namesIn[a][0] == 'h' && namesIn[a][1] == 't')) {
            continue;
        }
        out << namesIn[a] << endl;
    }

    out.close();
    
    return 0;
}
/*
PYBIND11_MODULE(parse, handle) {
    handle.doc() = "This is module doc";
    handle.def("parse", &main);
}
*/