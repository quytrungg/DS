#include <iostream>

void input(int m, int n, int k,int *&a,int *&b,int **&c){
    for(int i = 0; i < m; ++i){
        std::cin >> a[i];
    }
    for(int i = 0; i < n; ++i){
        std::cin >> b[i];
    }
    for(int i = 0; i < k; ++i){
        c[i] = new int[2];
        std::cin >> c[i][0];
        std::cin >> c[i][1];
    }
}

void process(int m, int n, int k,int *a,int *b,int **c,int min){
    for(int i = 0; i < k; ++i){
        min = INT_MAX;
        for(int j = c[i][0]-1; j < c[i][1]; j++){
            for(int l = 0; l < n; l++){
                if(abs(b[l] - a[j]) < min){
                    min = abs(b[l] - a[j]);
                }
            }
        }
        std::cout << min << '\n';
    }
}

int main(){
    int m, n, k, min;
    std::cin >> m >> n >> k;
    int *a = new int[m];
    int *b = new int[n];
    int **c = new int*[k];
    input(m, n, k, a, b, c);
    process(m, n, k, a, b, c, min);
    return 0;
}