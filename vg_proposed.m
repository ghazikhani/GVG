% i=1;
% j=3;
% k=2;
% x=-1;
% y=-2;
% z=1;
function [con]=vg_proposed(i,j,k,x,y,z)
mina=min(0,z);
maxa=max(0,z);
f1=((y-x)/(j-i))*(k-i)+x;
if( mina <= f1 ) & (f1 <= maxa)
    con=0;
else 
    con=1;
end
end  

