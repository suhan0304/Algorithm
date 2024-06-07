#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

map<string, int> dict;
vector<vector<int>> graph;
vector<int> giftParameter;

void splitFunc(string str) {
    istringstream is;
    is.str(str);
    vector<string> words;
    string word;
    while(getline(is, word, ' ')) {
        words.push_back(word);
    }
    graph[dict[words[0]]][dict[words[1]]] += 1;
    graph[dict[words[1]]][dict[words[0]]] += 1;
    giftParameter[dict[words[0]]] += 1;
    giftParameter[dict[words[1]]] += 1;
}

int solution(vector<string> friends, vector<string> gifts) {
    int answer = 0;
    giftParameter = vector<int>(friends.size(), 0);
    for (int i = 0; i< friends.size(); i++) {
        dict.insert({friends[i], i});
    }

    graph = vector<vector<int>>(friends.size(), vector<int>(friends.size(), 0));

    for (int i = 0; i<gifts.size();i++) {
        splitFunc(gifts[i]);
    }

    for (int i = 0; i<friends.size(); i++) {
        int nowGift = 0;
        for (int j = 0; j<friends.size(); j++) {
            if (graph[i][j] > 0) {
                nowGift += 1;
            }
            else if (graph[i][j] == 0) {
                if (giftParameter[i] > giftParameter[j]) {
                    nowGift += 1;
                }
            }
        }
        if (nowGift > answer) {
            answer = nowGift;
        }
    }
    return answer;
}
