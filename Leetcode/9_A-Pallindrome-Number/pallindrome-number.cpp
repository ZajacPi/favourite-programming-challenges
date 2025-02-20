#include <iostream>  
#include <string>    

bool ispallindrome(int x) {
    if(x<0){
        return false;
    }
    int r = 0;
    int current;
    int t = x;
    while (t>0){
        r *= 10;
        current = t % 10;
        r += current;
        t-=current;
        t/=10;

    }
    if(r == x){
        return true;
    }
    else{
    return false;
    }
}

int main() {
    int x = 1214;
    bool message = ispallindrome(x);  // call the function and store the result in 'message'
    std::cout << message << std::endl;      // print the returned message to the console
    return 0;  // return 0 to indicate successful execution
}