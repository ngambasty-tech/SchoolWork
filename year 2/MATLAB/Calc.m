function result = Calc(x,y,option)

if option == "add"
    result = Add(x,y);
elseif option == "sub"
    result = Subtract(x,y);
elseif option == "mul"
    result = Multiply(x,y);
elseif option == "div"
    result = Divide(x,y);
else
    disp('invalid input')
end
    function a= Add(x,y)
        a = x + y;
    end

    function s=  Subtract(x,y)
        s = x-y;
    end
    function d = Divide(x,y)
        d = x/y;
    end
    function m = Multiply(x,y)
        m = x*y;
    end

end
