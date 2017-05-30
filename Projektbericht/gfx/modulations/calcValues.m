
%t  = (0:1/fn:1)';

fc = 1000; %carrier frequency
fa = 10*fc; %sample frequemcy
Ta= 1/fa; %sample period

fn = 50; %message frequency
Tn = 1/fn; %message period

stop = 3*Tn;
t = 0:Ta:(stop-Ta);
x = 12*sin(2*pi*fn*t);
c = 5*sin(2*pi*fc*t);
y = 5*fmmod(x,fc,fa,40);


%FREQUENZMODULATION
h = figure(1)
set(h,'Position',[0 0 1000 300]);;
%subplot(3,1,1)
plot(t,x,'b-','LineWidth',2);
title('Nachrichtensignal')
xlabel('t/s')
ylabel('u_m/V')
grid on

subplot(3,1,2)
%plot(t,c,'b-','LineWidth',2)
title('Trägersignal')
xlabel('t/s')
ylabel('u_c/V')
grid on
 
subplot(3,1,3)
%plot(t,y,'b-','LineWidth',2)
title('Frequenzmoduliertes Signal')
xlabel('t/s')
ylabel('u_{fm}/V')
grid on
%print(h,'fm.tex', '-dlatex');

CSVdata = [t' ,x', c', y'];
csvwrite("FM.csv",CSVdata)


%AMPLITUDENMODULATION
h = figure(2)
set(h,'Position',[0 0 1000 300]);
subplot(3,1,1)
%%plot(t,x,'b-','LineWidth',2);
title('Nachrichtensignal')
xlabel('t/s')
ylabel('u_m/V')
grid on

subplot(3,1,2)
%plot(t,c,'b-','LineWidth',2)
title('Trägersignal')
xlabel('t/s')
ylabel('u_c/V')
grid on


subplot(3,1,3)
y = ammod(x+15,fc,fa);
%plot(t,y,'b-','LineWidth',2)
title('Amplitudenmoduliertes Signal')
xlabel('t/s')
ylabel('u_{am}/V')
grid on
%print(h,'am.tex', '-dlatex')
CSVdata = [t' ,x', c', y'];
csvwrite("AM.csv",CSVdata)

%PULSWEITENMODULATION
h = figure(3)
set(h,'Position',[0 0 1000 300]);
subplot(3,1,1)
%plot(t,x,'b-','LineWidth',2);
title('Nachrichtensignal')
xlabel('t/s')
ylabel('u_m/V')
grid on

subplot(3,1,2)
c = 12*sawtooth(2*pi*fc*t,0.5);
%plot(t,c,'b-','LineWidth',2)
title('Trägersignal')
xlabel('t/s')
ylabel('u_c/V')
grid on

for i=1:length(c)
  if c(i)>x(i)
  y(i) = 0;
  else
  y(i) = 1;
  endif
endfor


subplot(3,1,3)
%plot(t,y,'b-','LineWidth',2)
title('Pulsweitenmoduliertes Signal')
xlabel('t/s')
ylabel('u_{pwm}/V')
ylim([-0.5 1.6])
axis
grid on

%print(h,'pwm.tex', '-dlatex');
CSVdata = [t' ,x', c', y'];
csvwrite("PWM.csv",CSVdata)