%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133
% Program Description 
% Program inputs data from a csv and compares the predicted data
% for volume to calculated data for volume with a graph
%
% Assigment Information
%   Assignment:     Ma2 PA Task 1
%   Author:         Zachary Williams, will2051@purdue.edu
%   Team ID:        001-01
%  	Contributor:    Name, login@purdue [repeat for each]
%   My contributor(s) helped me:	
%     [ ] understand the assignment expectations without
%         telling me how they will approach it.
%     [ ] understand different ways to think about a solution
%         without helping me plan my solution.
%     [ ] think through the meaning of a specific error or
%         bug present in my code without looking at my code.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% ____________________
%% INITIALIZATION
data = csvread("Ma2_PA_Task1_Data_volume_power.csv",2,0);

power = data(:,1);
volOEP4 = data(:,2);
volIEP3 = data(:,3);

%% ____________________
%% CALCULATIONs
volCalcOEP4 = 67.1 * log10(power)-1.3;
volCalcIEP3 = 77.7 * log10(power)-7.3;

%% ____________________
%% FORMATTED FIGURE
plot(power,volOEP4,'b-*',power,volIEP3,'r-^',power,volCalcOEP4,'k>-.',power,volCalcIEP3,'g-+');
title("OEP4 and IEP3 Volume vs. Power");
xlabel("Power (mW)");
ylabel("Volume (dB)");
grid on;

legend(["OEP4 Predicted = Blue","IEP3 Predicted = Red","OEP4 Calculated = Black","IEP3 Calculated = Green"],"Location","southeast");
%% ____________________
%% ANALYSIS

%% -- Q1
% The model for IEP3 best fits the data given, as there is very little
% difference between the predicted and calculated data

%% -- Q2
% IEP3 is more sensitive because it has a greater slope.


%% -- Q3
% OEP4 would give a greater battery life at 60 dB and IEP3 would have
% a greater battery life at 30 dB.


%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The script I am submitting
% is my own original work.