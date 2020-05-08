%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Takes values for blinds and outputs transmission and absorption values
%
% Assignment Information
%   Assignment:     Ma3_PA Task 2 exec
%   Author:         Zach Williams, will2051@purdue.edu
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
spacing = 50;
width = 60;
absorpConst = .76;
angShadow = 45;
horiAngles = [30,45,60];
F1 = [0,0,0];
F2 = [0,0,0];
F3 = [0,0,0];
tranVal = [0,0,0];
absorpVal = [0,0,0];

%% ____________________
%% CALCULATIONS
for i = 1:3
    [F1(i),F2(i),F3(i)] = Ma3_PA_Task2_fractions_will2051(width,spacing,horiAngles(i));
    tranVal(i) = Ma3_PA_Task2_transmission_will2051(absorpConst,width,angShadow,horiAngles(i),spacing,F1(i),F2(i),F3(i));
    absorpVal(i) = Ma3_PA_Task2_absorb_will2051(absorpConst,width,angShadow,horiAngles(i),spacing,F2(i));
end

%% ____________________
%% OUTPUTS
for i = 1:3
    fprintf("The transmission value for Blind 1 at %d degrees is %f.\n",horiAngles(i),tranVal(i));
    fprintf("The absorption value for Blind 1 at %d degrees is %f.\n",horiAngles(i),absorpVal(i));
end

% 7a
%The transmission value for Blind 1 at 30 degrees is -0.572457.
%The absorption value for Blind 1 at 30 degrees is 1.387543.
%The transmission value for Blind 1 at 45 degrees is -0.648144.
%The absorption value for Blind 1 at 45 degrees is 1.416686.
%The transmission value for Blind 1 at 60 degrees is -0.607829.
%The absorption value for Blind 1 at 60 degrees is 1.343479.

%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.