function [ori_img] = imgPre(img_path)
    ori_img = rgb2gray(imread(img_path)); % ��ͼ+��Ϊ�Ҷ�ͼ
end