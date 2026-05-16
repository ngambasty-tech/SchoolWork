function result = Factorial(x)
if x==0 || x==1
    result = 1;
elseif x<0
    disp('invalid input')
else
    result = x * Factorial(x-1);
end
end