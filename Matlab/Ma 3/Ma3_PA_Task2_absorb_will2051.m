function [Ad] = Ma3_PA_Task2_absorb_will2051(absorptivity,width,angShadow,angSlat,spacing,F2)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Takes in data about the blind and calculates absorption
%
% Function Call
% Ma3_PA_Task2_absorb_will2051()
%
% Input Arguments
% width - slat width (mm)
% spacing - slat spacing (mm)
% angSlat - slat angle with the horizontal (degrees)
% angShadow - vertical shadow angle
% absorptivity - Absorptivity Constant
% F2 - fraction of total radiation reflected by the lower slat that is intercepted by the upper slat
% when the whole width is illuminated;
%
% Output Arguments
% Ad - total fraction of radiation absorbed
%
% Assignment Information
%   Assignment:     Ma3_PA Task 2 absorption
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
Ad = (absorptivity * width * sin((angShadow + angSlat) * pi / 180)) / (spacing * cos(angShadow * pi / 180) * (1 - F2 * (1 - absorptivity)));


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