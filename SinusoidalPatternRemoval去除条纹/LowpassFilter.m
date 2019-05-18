function [H] = LowpassFilter(f_img, d0, method)
    % f_img: after fft2 and fftshift
	% d0: radias, cut-off frequency
	% ret: res_fimg--being notched in middle
	
	[m, n] = size(f_img);
	x0 = floor(m / 2);
	y0 = floor(n / 2);
	for u = 1:m
		for v = 1:n
			duv = Distance(x0, y0, u, v);
			switch lower(method)
				case {'butterworth', 'btw'}
					H(u, v) = 1 / (1 + (d0 / duv)^(2*n));
				case {'gaussian'}
					H(u, v) = 1 - exp(- (duv^2) / (2 * d0^2));
				otherwise % otherwise: error
					H = zeros(m, n);
			end
		end
	end

end
