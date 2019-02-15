mon = '01';

%surface data:
T = importdata(['SurfTair_' mon '.txt']);
precip = importdata(['Precip_' mon '.txt']);
sw = importdata(['SurfSW_' mon '.txt']);

T(T>1e36) = nan;
precip(precip>1e36) = nan;
sw(sw>1e36) = nan;

%corresponding lat and lon:
lat = importdata('latitude.txt');
lon = importdata('longitude.txt');

%plot DIC:
figure;
pcolor(lon, lat, precip)
shading flat
colorbar
xlabel('Longitude', 'fontsize', 14)
ylabel('Latitude', 'fontsize', 14)
title(['Surface air temperature month ' mon], 'fontsize', 16)
