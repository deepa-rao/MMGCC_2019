% Read monthly surface forcing data for simple terrestrial ecosystem model
% Matlab script
% Mick Follows, Oliver Jahn, Mukund Gupta, Deepa Rao (2019)

% clear all data and close all figures
clear all; 
close all;

% select month using strings
% mon = '01' for january etc. 
% mon = 'mean' for annual mean
%
% create an array of strings representing months
months = {'01','02','03','04','05','06','07','08','09','10','11','12'} ; 

% set mon to January ...
mon = char(months(1)) ;
% uncomment next line to use annual mean
%mon = 'mean' ;

% read in the lat and lon coordinates of the gridded data
lat = importdata('latitude.txt');
lon = importdata('longitude.txt');
nlat = length(lat);
nlon = length(lon);

% initialize array (lat, lon, month)
T = zeros(length(lat),length(lon),12);
sw = zeros(length(lat),length(lon),12);
precip = zeros(length(lat),length(lon),12);

% Reading data for monthly means
for i=1:length(months)
    mon = months{i};
    % surface air temperature (C)
    T(:,:,i) = importdata(['SurfTair_' mon '.txt']);
    % precipitation (cm/month)
    precip(:,:,i) = importdata(['Precip_' mon '.txt']);
    % incident short wave radiation - visible light (W/m2)
    sw(:,:,i) = importdata(['SurfSW_' mon '.txt']);
end

% convert precip from cm/month to m/yr 
precip = precip * 12.0 / 100.0; % Converting to [m/yr]

% mask missing values
T(T>1e36) = nan; % set missing values to NaNs 
precip(precip>1e36) = nan; % set missing values to NaNs 
sw(sw>1e36) = nan; % set missing values to NaNs 

% Make a mask setting ocean points to NaN based on the T file
% Divide T by itself - will give 1s and NaNs
landmask = T ./ T ;

% mask out ocean points in the shortwave file
sw = sw .* landmask; 

%plot surface temperature (C)
figure(1);
pcolor(lon, lat, T(:,:,1))
shading flat
colorbar
xlabel('Longitude', 'fontsize', 14)
ylabel('Latitude', 'fontsize', 14)
title(['Temperature (^oC)'], 'fontsize', 16)



