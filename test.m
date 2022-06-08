clc
clear

gas  = [1 2 3 4 5];
cost = [3 4 5 1 2];

for i = 1:length(gas)
    temp = 0;
    for j = 1:length(gas)
        temp = gas(i) + temp + cost(j);
        