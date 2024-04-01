
function [con]=vg_base(i,j,k,x,y,z)
% f1=(z-y)/(j-k);
% f2=(x-y)/(j-i);
if (z<y+(x-y)*((j-k)/(j-i)) )
    con=1;
else
    con=0;
end
end