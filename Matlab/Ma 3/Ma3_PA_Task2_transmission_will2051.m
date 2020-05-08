function [Td] = Ma3_PA_Task2_transmission_will2051(absorptivity,width,angShadow,angSlat,spacing,F1,F2,F3)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Takes in data about the blind and calculates transmission
%
% Function Call
% Ma3_PA_Task2_transmission_will2051()
%
% Input Arguments
% width - slat width (mm)
% spacing - slat spacing (mm)
% angSlat - slat angle with the horizontal (degrees)
% angShadow - vertical shadow angle
% absorptivity - Absorptivity Constant
% F1 - fraction of total radiation reflected by the lower slat that passed into the room when the
% whole width is illuminated
% F2 - fraction of total radiation reflected by the lower slat that is intercepted by the upper slat
% when the whole width is illuminated
% F3 - fraction of radiation reflected by the upper slat that passes into the room
%
% Output Arguments
% Td - total fraction of incident radiation transmitted by the blind
%
% Assignment Information
%   Assignment:     Ma3_PA Task 2 transmission
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
Td = 1 - ((width * sin((angShadow + angSlat) * pi / 180)) / (spacing * cos(angShadow * pi / 180)) * (1 - F1 * (1 - absorptivity) - (F2 * power(1 - absorptivity,2) * (F3 + F1 * F2 * (1 - absorptivity)) / (1 - power(F2,2) * power(1 - absorptivity,2)))));


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