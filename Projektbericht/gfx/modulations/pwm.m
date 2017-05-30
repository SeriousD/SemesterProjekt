pkg load communications
graphics_toolkit('gnuplot')
%t  = (0:1/fn:1)';

fc = 1000; %carrier frequency
fa = 100*fc; %sample frequemcy
Ta= 1/fa; %sample period

fn = 50; %message frequency
Tn = 1/fn; %message period

stop = 2*Tn;
t = 0:Ta:(stop-Ta);
x = 12*sin(2*pi*fn*t);
c = 5*sin(2*pi*fc*t);
#y = 5*fmmod(x,fc,fa,40);


h = figure('Position',[0,0,730,270]);
c = 12*sawtooth(2*pi*fc*t,0.5);

for i=1:length(c)
  if c(i)>x(i)
  y(i) = 0;
  else
  y(i) = 1;
  endif
endfor

hold on;
plot(t,y,'-','LineWidth',3)
area (t, y, "FaceColor", [0.7 0.7 1]);
hold off;
title('Pulsweitenmoduliertes Signal')
xlabel('t/s')
ylabel('u_{pwm}/V')
ylim([-0.5 1.6])
%axis
grid on
set (gcf,'paperposition',[0 0 8 3]) 
%set (h,'papertype', '<custom>')
%set (h,'paperunits','inches');
%set (h,'papersize',[3 1.5])
%print(h,'pwmArea.tex', '-dtex');
%print -dtex "S730,340" pwmArea.tex

CSVdata = [t', y'];
csvwrite("PWMarea.csv",CSVdata)

