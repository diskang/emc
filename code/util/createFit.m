function [fitresult, gof] = createFit(x, y)
%CREATEFIT(X,Y)
%  Create a fit.
%
%  Data for 'untitled fit 2' fit:
%      X Input : x
%      Y Output: y
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  See also FIT, CFIT, SFIT.
%  Auto-generated by MATLAB on 08-May-2015 21:45:10

%改写和调用方法网址：http://blog.sina.com.cn/s/blog_45eac6860101esch.html


%% Fit: 'untitled fit 2'.
[xData, yData] = prepareCurveData( x, y );

% Set up fittype and options.
ft = fittype( 'exp1' );
opts = fitoptions( ft );
opts.Display = 'Off';
opts.Lower = [-Inf -Inf];
opts.StartPoint = [520.518935375825 -0.0261847914012525];
opts.Upper = [Inf Inf];

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Plot fit with data.
figure( 'Name', 'untitled fit 2' );
h = plot( fitresult, xData, yData );
legend( h, 'y vs. x', 'untitled fit 2', 'Location', 'NorthEast' );
% Label axes
xlabel( 'x' );
ylabel( 'y' );
grid on


