#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;

    

    return answer;
}

int main() {
    string myString = "banana";
    string pat = "ana";

    int idx;
    int answer = 0;

    for (int i = 0; i < myString.size(); i++) {
        idx = 0;
        while (myString[i] == pat[idx++]) { }
        if ( idx == pat.size() ) {
            answer += 1;
        }
    }
    
    cout << answer;
}