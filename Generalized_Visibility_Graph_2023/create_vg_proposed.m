
clc
clear all;
tic

eeg=xlsread('noisesignal_authism512.csv');

[r_size,c_size]=size(eeg);

condition=zeros(c_size);
adjency_matrix=zeros(c_size,c_size);
adjency_matrix2=zeros(c_size,c_size);

for i=1:c_size
    for j=i+1:c_size
        if ((j-i)==1)
            adjency_matrix(i,j)=1;           
            adjency_matrix2(i,j)=eeg(j);                        
        end
        
        if  j <= c_size
            total_condition=1;
            for k=(i+1) : j-1
                condition(k) = vg_proposed( i,j,k,eeg(1,i) , eeg(1,j) , eeg(1,k));                
                total_condition = total_condition*condition(k);
            end
        else
            j=j+1;
        end
        if total_condition == 1
            adjency_matrix(i,j)=1;            
            adjency_matrix2(i,j)=eeg(j);
        end
    end
end


s=Matrix2GraphML(adjency_matrix,"out_filesample.graphml");
toc