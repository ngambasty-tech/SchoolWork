x=linspace(1,3,10);
y=sin(x);
% plot(x,y);
% plot(x,y,'b*')

plot(x,y,x,y);
xlabel("x");
ylabel("x^2");
legend("x^2","sinx");
title("test sample");