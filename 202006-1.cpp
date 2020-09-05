#include <iostream>
#include <vector>

using namespace std;


bool is_true(int* points, int n, int* line){
    int side_n[2] = {-1, -1};

    while(n--){
        int pos = line[0] + line[1] * points[n * 3 + 0] + line[2] * points[n * 3 +1];
        
        int side = pos > 0 ? 1 : 0;

        if(side_n[points[n * 3 + 2]] == -1){
            side_n[points[n * 3 + 2]] = side;
            continue;
        }
        
        if(side != side_n[points[n * 3 + 2]]){
            return false;
        }
    }

    return true;
}


int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;

    int* points = (int *) malloc(n * 3 * sizeof(int));
    int nn = 0;
    while(n--){
        char c;
	    scanf("%d %d %c", &points[nn * 3], &points[nn * 3 + 1], &c);
        points[nn * 3 + 2] = c == 'A' ? 0 : 1;
	
	nn += 1;
    }

    int* lines = (int *) malloc(m * 3 * sizeof(int));
    int mm = 0;
    while(m--){
        scanf("%d %d %d", &lines[mm * 3], &lines[mm * 3 + 1], &lines[mm * 3 + 2]);
    	mm += 1;
    }

    for(int i = 0; i < mm; i++){
        bool res = is_true(points, nn, lines + i * 3);
        if(res == 0) cout << "No";
        else cout << "Yes";

        if (i < mm -1){
            cout << endl;
        }
    }

    return 0;
}


// 9 3
// 1 1 A
// 1 0 A
// 1 -1 A
// 2 2 B
// 2 3 B
// 0 1 A
// 3 1 B
// 1 3 B
// 2 0 A
// 0 2 -3
// -3 0 2
// -3 1 1