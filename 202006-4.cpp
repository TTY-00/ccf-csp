#include <bits/stdc++.h>
#define LEN 7
using namespace std;
using ll = long long;
                       //0, 1, 2, 3, 4, 5, 6     
int matrix[LEN][LEN] = {{0, 0, 0, 0, 0, 0, 0}, // 0
                        {0, 0, 1, 0, 0, 0, 0}, // 1
                        {0, 0, 0, 0, 1, 0, 0}, // 2
                        {0, 0, 0, 0, 0, 0, 0}, // 3
                        {0, 1, 0, 0, 0, 0, 1}, // 4
                        {0, 0, 0, 0, 0, 0, 0}, // 5
                        {0, 0, 0, 0, 1, 0, 1}}; // 6

void add_array(ll* input_i, ll* input_o, int length){
    for(int i = 0; i < length; i++){
        input_o[i] = (input_o[i] + input_i[i]) % 998244353;
    }
}

void mul_array(int* input, ll* output, ll times, int length){
    for(int i = 0; i < length; i++){
        output[i] = (ll(input[i]) * times) % 998244353;
    }
}

void print_array(ll* input, ll length, string tag){
    cout << "== " << tag << " ==" << endl;
    for(int i = 0; i < LEN; i++){
        cout << input[i] << " ";
    }
    cout << endl;
}

int sum_array(ll* input, ll length){
    ll sum = 0;

    for(int i = 0; i < length; i++){
        sum = input[i] % 998244353;
    }

    return sum;
}

void count(ll* input, ll* output){
    ll tmp[LEN];
    
    for(int i = 0; i < LEN; i++){
        memset(tmp, 0, sizeof(ll) * LEN);
        mul_array(matrix[i], tmp, input[i], LEN);
        add_array(tmp, output, LEN);
    }

    // print_array(tmp, LEN, "tmp");
    // print_array(output, LEN, "count - output");
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll time;
    ll num;

    ll l1[LEN] = {0, 0, 0, 0, 0, 0, 0};
    ll l2[LEN] = {0, 0, 0, 0, 0, 0, 0};

    ll* in = l1;
    ll* out = l2;
    ll* tmp = NULL;

    cin >> time;
    cin >> num;

    // cout << time << endl;
    // cout << num << endl;

    if(num > LEN){
        cout << 0;
        return 0;
    }

    in[1] = 1;

    for(int t = 0; t < time; t++){
        memset(out, 0, sizeof(ll) * LEN);
        
        count(in, out);
        // print_array(in, LEN, "in");
        // print_array(out, LEN, "out");
        tmp = in;
        in = out;
        out = tmp;
    }


    // cout << "==" << endl;
    // int res = sum_array(in, LEN);
    // cout << in[num] << endl;
    ll res = in[num] % 998244353;
    cout << res;

    return 0;
}