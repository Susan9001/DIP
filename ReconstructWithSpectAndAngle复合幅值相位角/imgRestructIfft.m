function [m1pa2_img] = imgRestructIfft(fm_img, fpa_img)
    m1 = abs(fm_img); % magnitude
    pa2 = angle(fpa_img); % phase angle
    m1pa2_img = ifft2(m1 .* cos(pa2) + m1 .* sin(pa2) .* 1i);
end