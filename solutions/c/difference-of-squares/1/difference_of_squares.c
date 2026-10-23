#include "difference_of_squares.h"
unsigned int sum_of_squares(unsigned int number){
    unsigned int store = 0;
    for(unsigned int i=1;i<=number;i++){
        store = i*i + store;
    }
    return store;
}
unsigned int square_of_sum(unsigned int number){
    unsigned int store = 0;
    for (unsigned int i=1;i<=number;i++){
        store = store + i;
    }
    return store*store;
}

unsigned int difference_of_squares(unsigned int number) {
    return square_of_sum(number) - sum_of_squares(number);
}


