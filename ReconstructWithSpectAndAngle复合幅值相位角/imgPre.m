function [ori_img] = imgPre(img_path)
    ori_img = rgb2gray(imread(img_path)); % ¶ÁÍ¼+±äÎª»Ò¶ÈÍ¼
end