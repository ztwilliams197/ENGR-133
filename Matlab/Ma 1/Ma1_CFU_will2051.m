%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% This program calculates the concentration of dissolved oxygen using
% given variables
%
% Assignment Information
%   Assignment:     Ma1_CFU
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
doSAT = 9;
k1 = .2;
k2 = .4;
l0 = 20;
t = 14;
d0 = 4;

%% ____________________
%% CALCULATIONS
DO = doSAT - (k1 * l0) / (k2 - k1) * (exp(-k1 * t) - exp(-k2 * t)) - d0 * exp(-k2 * t);

%% ____________________
%% OUTPUTS
fprintf("The concentration of DO is %.2f [mg/L].", DO);

%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.