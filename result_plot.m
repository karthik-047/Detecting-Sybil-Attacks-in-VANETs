dist = [200,250,300,350];

det = [100,100,100,100];

fp1 = [21.8,9.09,3.6,0];
fp2 = [14.5,3.6,1.8,1.8];
fp3 = [18.1,5.45,3.6,1.8];
fp4 = [20,8,3.6,3.6];
fp5 = [16,12,6,4];

figure;
plot(dist,det,'-o',dist,det,'-o',dist,det,'-o');
title('Impact of distance threshold on Detection Rate');
xlabel('Distance Affinity');
ylabel('Detection Percentage');

figure;
plot(dist,fp1,'-o',dist,fp2,'-o',dist,fp3,'-o',dist,fp4,'-o',dist,fp5,'-o');
title('Impact of distance threshold on False Positive Rate');
xlabel('Distance Affinity');
ylabel('False Positive Percentage');
legend('Scenario1','Scenario2','Scenario3','Scenario4','Scenario5')