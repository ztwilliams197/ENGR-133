function [F1,F2,F3] = Ma3_PA_Task2_fractions_will2051(width,spacing,angle)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
% Brings in width, spacing, and angle values and calculates f1, f2, and f3
%
% Function Call
% Ma3_PA_Task2_fractions_will2051()
%
% Input Arguments
% width - slat width (mm)
% spacing - slat spacing (mm)
% angle - slat angle with the horizontal (degrees)
%
% Output Arguments
% F1 - fraction of total radiation reflected by the lower slat that passed into the room when the
% whole width is illuminated
% F2 - fraction of total radiation reflected by the lower slat that is intercepted by the upper slat
% when the whole width is illuminated
% F3 - fraction of radiation reflected by the upper slat that passes into the room
%
% Assignment Information
%   Assignment:     Ma3_PA Task 2 Fractions
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


%% ____________________
%% CALCULATIONS
plusRoot = sqrt(1 + power(spacing / width, 2) + 2 * (spacing / width) * sin(angle * pi / 180));
minusRoot = sqrt(1 + power(spacing / width, 2) - 2 * (spacing / width) * sin(angle * pi / 180));

F1 = 1/2 * (1 + (spacing / width) - plusRoot);
F2 = 1/2 * (plusRoot + minusRoot - (2 * spacing / width));
F3 = 1/2 * (1 + (spacing / width) - minusRoot);


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

end