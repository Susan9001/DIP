function [H] = NotchRectFilter(f_img, mid_height, mid_width)
    % f_img: after fft2 and fftshift
    % d0: radias, cut-off frequency
    % ret: a narrow notch rectangle filter
	
	[height, width] = size(f_img);
	u0 = floor(height / 2);
	v0 = floor(width / 2);
	half_midH = floor(mid_height / 2);
	half_midW = floor(mid_width / 2);
	H = ones(height, width);
	for u = 1 : (u0 - half_midH)
		for v = (v0 - half_midW) : (v0)
			H(u, v) = 0; % the upper-left half
			H(u, width - v) = 0; % the upper-right half
			H(height - u, v) = 0; % the lower-left
			H(height - u, width - v) = 0; % the lower-right
		end
	end
end
