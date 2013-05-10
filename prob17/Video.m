Obj = VideoReader('video.avi');
nFrames = Obj.NumberOfFrames;
data = zeros(3424,1);
for ind = 1: nFrames
    if mod(ind,500) == 0
        ind
    end
    frame = read(Obj, ind);
    data(ind) = frame(347,413,1);
end
data = data > 100;
s = '';
b = [128 64 32 16 8 4 2 1];
for i=1:8:nFrames
    s = [s char(sum(b .* data(i:(i+7))'))];
end
s