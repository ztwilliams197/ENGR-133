function [time,voltage] = Ma3_PA_Task1_photon_data_will2051()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Reads photon data from a text file and outputs a Voltage vs Time plot
% and the number of photons and times the photons are detected
%
% Function Call
% Ma3_PA_Task1_photon_data_will2051()
%
% Input Arguments
% Void
%
% Output Arguments
% time - array of time values in milliseconds
% voltage - array of voltage values
%
% Assignment Information
%   Assignment:     Ma3_PA Task 1 data
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
data = load("Ma3_PA_Task1_photon.txt");
time = data(:,1);
voltage = data(:,2);

%% ____________________
%% CALCULATIONS
[numPhot,times] = Ma3_PA_Task1_number_photon_will2051(time,voltage);


%% ____________________
%% FORMATTED TEXT & FIGURE DISPLAYS
Ma3_PA_Task1_signal_plot_will2051(time,voltage);


%% ____________________
%% COMMAND WINDOW OUTPUT
fprintf("Number of Photons Detected: %d\n", numPhot);
fprintf("Times Photons are Detected: %d\n", times);



%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.