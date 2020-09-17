#include <bits/stdc++.h>

using namespace std;

int cout(int m, int k){
    int res = 1;
    for(int i = 0; i < k; i++){
        res *= (m - i);
    }

    return res;
}

int get_all(map<pair<int, int>, int> net, int start, int end){
    if(map.find({start, end})){
        return map[{start, end}]
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, k;
    cin >> n >> m >> k;

    vector<int> important(m);

    int tmp;
    for(int i = 0; i < m; i++){
        cin >> tmp;
        important.push_back(tmp);
    }

    map<pair<int, int>, int> net;
    vector<int> nodes_multi;

    int a, b, c;
    while(cin >> a >> b >> c){
        net.insert({{a, b}, c});
        net.insert({{b, a}, c});
        nodes.push_back(a);
        nodes.push_back(b);
    }

    set<int> nodes(nodes_multi.begin(), nodes_multi.end());

    for(auto i:nodes){
        for(auto j:modes){

        }
    }

    for(int i = 0; i < )

    int min = 0;
    // int choice = cout(m, k);
    

    return 0;
}