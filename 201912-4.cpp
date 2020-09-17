#include <bits/stdc++.h>
using namespace std;

map<int, vector<int> > chain_state;
// vector<int> net(501 * 501, 0);
queue<pair<pair<int, int>, vector<int> > >  broadcasted_queue;
// unordered_map<pair<int, int>, int> net;
int tt; // 延时
int nn; // 点数
// chain state first: recv(map) second: main(vector)
// node: recv, main

bool can_accept(vector<int> recv, vector<int> node_main){
    return recv.size() == node_main.size() ? recv.back() < node_main.back() : recv.size() > node_main.size();
}   

void print_matrix(vector<int> vec, int max){
    int sum = 0;
    for(int i = 1; i <= max; i++){
        for(int j = 1; j <= max; j++){
            cout << vec[i*501 + j] << " ";
            sum += vec[i*501 + j];
        }
        cout << endl ;
    }
    cout << sum << endl;
}

void broadcast(int node, int time, vector<int> chain){
    for(int i = 1; i <= nn; i++){
        if(net[node * 501 + i] == 1){
            // cout << "update" << endl;
            int node_r = i;
            // chain_state[node_r].first.insert({time + tt, chain});
            broadcasted_queue.push({{time + tt, node_r}, chain});
        }
    }
}

void cout_vec(vector<int> vec, string tag){
    cout << tag << ": ";
    for(auto i: vec){
        cout << i << " ";
    }
    cout << endl;
}

void handle_broadcast(int now){
    while(broadcasted_queue.size() > 0){
        auto task = broadcasted_queue.front();
        
        int time = task.first.first;

        // cout << "time: " << time << " node: " << get<1>(task) << endl;
        
        if (time > now){
            break;
        }
        broadcasted_queue.pop();
        
        // cout << "in" << endl;
        int node = task.first.second;
        vector<int> chain = task.second;

        auto& target_main = chain_state[node];
        bool accept = can_accept(chain, target_main);
        if(accept){
            // cout_vec(chain_state[node].second, "before");
            target_main = chain;
            // cout_vec(chain_state[node].second, "after");
            broadcast(node, time, chain);
        }
    }
}

void gen(int node, int time, int block){
    auto& node_main = chain_state[node];

    handle_broadcast(time);

    node_main.push_back(block);
    broadcast(node, time, node_main);
}

void query(int node, int time, int n){
    handle_broadcast(time);

    auto& node_main = chain_state[node];
    cout << node_main.size() + 1 << " " << '0';
    for(auto i: node_main){
        cout << " " << i;
    }
    cout << endl;

    // cout << node.main.size() << " ";
    // cout
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int m;
    cin >> nn >> m ;

    int p1, p2;
    for(int i = 0; i < m; i++){
        cin >> p1 >> p2;
        net[p1 * 501 + p2] = 1;
        net[p2 * 501 + p1] = 1;
    }

    int k;
    cin >> tt >> k;

    int now = 1;

    int node, time, block = 0;
    for(int i = 0; i < k; i++){
        cin >> node >> time;
        if(cin.get() == '\n' or cin.eof()){
            query(node, time, nn);
        }
        else{
            cin >> block;
            gen(node, time, block);
        }
    }

    return 0;
}