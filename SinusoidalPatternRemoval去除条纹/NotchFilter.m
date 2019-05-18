function [H] = NotchFilter(f_img, mid_height, mid_width)
    % f_img: after fft2 and fftshift
    % d0: radias, cut-off frequency
    % ret: been notched in middle
	
	[m, n] = size(f_img);
	u0 = floor(m / 2);
	v0 = floor(n / 2);
	half_mid_height = floor(mid_height / 2);
	half_mid_width = floor(mid_width / 2);
	H = ones(height, width);
	for u = 0 : (u0 - half_mid_height);
		for v = (v0 - half_mid_width) : (v0);
			H(u, v) = 0 % the upper-left half;
			H(u, n - v) = 0 % the upper-right half;
			H(m - u, n) = 0;
			H(m - u, n - v) = 0;
		end
	end
end
