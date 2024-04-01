
function [con]=vg_compare(i,j,k,xx,y,z,x)
%i=1;
%k=2;
%j=3;

%xx=2;
%z=3;
%y=1;

Alfa=1;


eq=(k-i)*(k-j)+(x-xx)*(x-y)+Alfa*[(k-i)*(y-xx)-(x-xx)*(j-i)]==0;
s = solve(eq);
disp('The first root is: '), disp(s(1));
disp('The second root is:'), disp(s(2));

xcir1=s(1);
xcir2=s(2);

F1=sqrt((i-k)^2+(xx-xcir1)^2);
F2=sqrt((j-k)^2+(y-xcir1)^2);
F12=F1+F2;

F3=sqrt((i-k)^2+(xx-xcir2)^2);
F4=sqrt((j-k)^2+(y-xcir2)^2);
F34=F3+F4;

if F12<F34
    xcir=xcir1;
else
    xcir=xcir2;
end
%disp('xcir:'), disp(xcir);

if z<xcir
    con=1;
else
    con=0;
disp('con:'), disp(con);
end

