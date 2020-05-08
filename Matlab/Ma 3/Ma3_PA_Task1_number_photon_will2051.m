function [numPhot,times] = Ma3_PA_Task1_number_photon_will2051(time,voltage)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Takes voltages and times and outputs the number of photons and the times
% at which the photons are detected
%
% Function Call
% Ma3_PA_Task1_photon_data_will2051()
%
% Input Arguments
% time - array of time values in milliseconds
% voltage - array of voltage values
%
% Output Arguments
% times - array of time values photons are detected at
% numPhot - number of photons detected
%
% Assignment Information
%   Assignment:     Ma3_PA Task 1 number
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


%% ____________________
%% CALCULATIONS
range = find(voltage > 1);
times = time(range);
numPhot = length(times);


%% ____________________
%% FORMATTED TEXT & FIGURE DISPLAYS



%% ____________________
%% COMMAND WINDOW OUTPUT



%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.