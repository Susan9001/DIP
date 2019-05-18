function [output_img, H] = SinusoidalPatternRemoval(img, midH, midW)
    % img1: the original grey image
    % midH: the height of the retangular notch in the middle
    % midW: the width of the rectangle
    % ret: res_img1--the img after pattern-removal; H--the filter
    
    % to get H
    [height, width] = size(img);
	u0 = floor(height / 2);
	v0 = floor(width / 2);
	half_midH = floor(midH / 2);
	half_midW = floor(midW / 2);
	H = ones(height, width);
    for u = 1 : (u0 - half_midH)
		for v = (v0 - half_midW) : (v0)
			H(u, v) = 0; % the upper-left half
			H(u, width - v) = 0; % the upper-right half
			H(height - u, v) = 0; % the lower-left
			H(height - u, width - v) = 0; % the lower-right
		end
    end
    
    % to process the img
    f_img = fftshift(fft2(img)); % have been shifted
    f_img = f_img .* H; % filtering
    output_img = ifft2(ifftshift(f_img)); % output without interference;
    
end



