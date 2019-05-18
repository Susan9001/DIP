function [display_spt_map, spectrum_map] = imgFFT(ori_img)
    % spectrum_map: 没有ffshift和log的
    spectrum_map = fft2(ori_img);
    display_spt_map = fftshift(log(spectrum_map + 1));
end
