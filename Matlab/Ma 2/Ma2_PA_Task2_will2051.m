%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Takes in data from a CSV file and displays data calculated using
% the CSV data and plots the mile markers vs. lane width
%
% Assignment Information
%   Assignment:     Ma2_PA Task 2
%   Author:         Zachary Williams, will2051@purdue.edu
%   Team ID:        001-01
%  	Contributor:    Jeff Zuo, zuo21@purdue.edu
%   My contributor(s) helped me:	
%     [ ] understand the assignment expectations without
%         telling me how they will approach it.
%     [X] understand different ways to think about a solution
%         without helping me plan my solution.
%     [ ] think through the meaning of a specific error or
%         bug present in my code without looking at my code.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% ____________________
%% INITIALIZATION
data = csvread("Ma2_PA_Task2_LaneWidth_TrafficSpeed_v3.csv");
mileMarker = data(:,1);
laneWidth = data(:,2);
speedOver65 = data(:,3);
speed55to64 = data(:,4);
speed45to54 = data(:,5);
speed35to44 = data(:,6);
speed25to34 = data(:,7);
speed15to24 = data(:,8);
speed0to14 = data(:,9);


%% ____________________
%% CALCULATIONS
maxWidth = max(laneWidth);
maxMileMarker = mileMarker(find(laneWidth == maxWidth));
minWidth = min(laneWidth);
minMileMarker = mileMarker(find(laneWidth == minWidth));

less10Range = find(laneWidth < 10);
P = less10Range(1,:);
Q = less10Range(end);

means145toP = mean(data(1:P,3:9));
meansPtoQ = mean(data(P:Q,3:9));
meansQto146 = mean(data(Q:end,3:9));

laneWidthPQ = laneWidth(P:Q);
above10 = find(laneWidthPQ > 10);
percAbove10 = (numel(above10) / numel(laneWidthPQ)) * 100;

%% ____________________
%%  FORMATTED FIGURE

plot(mileMarker,laneWidth,'-o');
title("Mile Marker vs. Lane Width");
ylabel("LaneWidth");
xlabel("Mile Marker");

%Part D
% This is not a worry as generally there will be some points that leak
% through and unless a significant amount of the points are incorrect it is
% not an issue.

%Part F
% This does not change my answer for Part D as I got an answer of about 4
% percent which is not a significant amount of the data points.

%% ____________________
%% OUTPUTS
fprintf("Lane Min: %.3f   Min Mile Marker: %.3f\n", minWidth, minMileMarker);
fprintf("Lane Max: %.3f   Max Mile Marker: %.3f\n", maxWidth, maxMileMarker);
fprintf("Mile P: %.3f  Mile Q: %.3f\n", mileMarker(P),mileMarker(Q));
fprintf("Percentage above 10: %.3f", percAbove10);

%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.