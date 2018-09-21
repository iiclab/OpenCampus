import cv2
import numpy as np
import argparse

## A4 ratio
out_h = 840
out_w = 1260
blank = 20

out_c = 3

Out_img_path = 'output.png'

def parse_args():
    parser = argparse.ArgumentParser(description='Faster R-CNN demo')
    #parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',default=0, type=int)
    #parser.add_argument('--cpu', dest='cpu_mode',help='Use CPU (overrides --gpu)',action='store_true')
    parser.add_argument('--content', dest='content_path', help='content image poath')
    parser.add_argument('--create', dest='create_path', help='create image poath')
    parser.add_argument('--style', dest='style_path', help='style image poath')
    parser.add_argument('--out', dest='out_path', help='output image poath')
    #parser.add_argument('--test', dest='test', help='test', action='store_true')
    #parser.add_argument('--iter', dest='iter', help='iteration', default=100, type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    content_img = cv2.imread(args.content_path)
    if content_img is None:
        raise Exception("not found input >>", args.content_path)
    content_h, content_w = content_img.shape[:2]

    create_img = cv2.imread(args.create_path)
    if create_img is None:
        raise Exception("not found output >>", args.create_path)
    create_h, create_w = create_img.shape[:2]

    style_img = cv2.imread(args.style_path)
    if style_img is None:
        raise Exception("not found con >>", args.style_path)
    style_h, style_w = style_img.shape[:2]

    
    whole_img = np.empty((out_h, out_w, out_c), dtype=np.uint8)
    whole_img.fill(255)


    # Reszie create image

    if max(create_h, create_w) == create_w:

        out_in_h = out_h - blank * 3
        out_in_w = out_w - blank * 2

        #----
        # Process Create image
        cre_ratio = 1. * out_in_w / create_w
        cre_rh = int(create_h * cre_ratio)
        cre_rw = int(create_w * cre_ratio)

        cre_h = out_in_h // 3 * 2

        cre_cx = out_w // 2
        cre_cy = cre_h // 2 + blank
        
        if cre_rh > (cre_h):
            cre_ratio = 1. * cre_h / create_h
            cre_rh = int(create_h * cre_ratio)
            cre_rw = int(create_w * cre_ratio)
            
        create_img = cv2.resize(create_img, (cre_rw, cre_rh))
        cre_nh, cre_nw = create_img.shape[:2]
        
        cre_x1 = cre_cx - cre_nw // 2
        cre_x2 = cre_x1 + cre_nw
        cre_y1 = cre_cy - cre_nh // 2
        cre_y2 = cre_y1 + cre_nh
        
        whole_img[cre_y1:cre_y2, cre_x1:cre_x2, :] = create_img

        #----
        # Process Content image
        in_content_w = (cre_rw - blank) // 2
        in_content_h = out_in_h // 3

        con_ratio = 1. * in_content_w / content_w
        con_rh = int(content_h * con_ratio)
        con_rw = int(content_w * con_ratio)

        con_h = out_in_h // 3

        #con_cx = (in_content_w - blank) // 2 + x1
        con_cx = cre_x1 + in_content_w // 2
        con_cy = out_h - 20 - in_content_h // 2

        if con_rh > (con_h):
            con_ratio = 1. * con_h / content_h
            con_rh = int(content_h * con_ratio)
            con_rw = int(content_w * con_ratio)

        content_img = cv2.resize(content_img, (con_rw, con_rh))
        con_nh, con_nw = content_img.shape[:2]
        
        con_x1 = con_cx - con_nw // 2
        con_x2 = con_x1 + con_nw
        con_y1 = con_cy - con_nh // 2
        con_y2 = con_y1 + con_nh

        whole_img[con_y1:con_y2, con_x1:con_x2, :] = content_img

        #----
        # Process style image

        in_style_w = (cre_rw - blank) // 2
        in_style_h = out_in_h // 3
        
        sty_ratio = 1. * in_style_w / style_w
        sty_rh = int(style_h * sty_ratio)
        sty_rw = int(style_w * sty_ratio)

        sty_h = out_in_h // 3

        style_cx = cre_x2 - in_style_w // 2
        style_cy = out_h - 20 - in_style_h // 2

        if sty_rh > (in_style_h):
            sty_ratio = 1. * in_style_h / style_h
            sty_rh = int(style_h * sty_ratio)
            sty_rw = int(style_w * sty_ratio)

        style_img = cv2.resize(style_img, (sty_rw, sty_rh))
        style_nh, style_nw = style_img.shape[:2]
        
        style_x1 = style_cx - style_nw // 2
        style_x2 = style_x1 + style_nw
        style_y1 = style_cy - style_nh // 2
        style_y2 = style_y1 + style_nh

        whole_img[style_y1:style_y2, style_x1:style_x2, :] = style_img

    elif max(create_h, create_w) == create_h:
        out_in_h = out_h - blank * 2
        out_in_w = out_w - blank * 3

        #----
        # Process Create image
        cre_ratio = 1. * out_in_h / create_h
        cre_rh = int(create_h * cre_ratio)
        cre_rw = int(create_w * cre_ratio)

        cre_w = out_in_w // 3 * 2

        cre_cx = cre_w // 2 + blank
        cre_cy = out_h // 2
        
        if cre_rw > (cre_w):
            cre_ratio = 1. * cre_w / create_w
            cre_rh = int(create_h * cre_ratio)
            cre_rw = int(create_w * cre_ratio)
            
        create_img = cv2.resize(create_img, (cre_rw, cre_rh))
        cre_nh, cre_nw = create_img.shape[:2]
        
        cre_x1 = cre_cx - cre_nw // 2
        cre_x2 = cre_x1 + cre_nw
        cre_y1 = cre_cy - cre_nh // 2
        cre_y2 = cre_y1 + cre_nh
        
        whole_img[cre_y1:cre_y2, cre_x1:cre_x2, :] = create_img

        #----
        # Process Content image
        in_content_w = out_in_w // 3
        in_content_h = (cre_rh - blank) // 2

        con_ratio = 1. * in_content_h / content_h
        con_rh = int(content_h * con_ratio)
        con_rw = int(content_w * con_ratio)

        con_w = out_in_w // 3

        con_cx = out_w - blank - in_content_w // 2
        con_cy = cre_y1 + in_content_h // 2

        if con_rw > (con_w):
            con_ratio = 1. * con_w / content_w
            con_rh = int(content_h * con_ratio)
            con_rw = int(content_w * con_ratio)

        content_img = cv2.resize(content_img, (con_rw, con_rh))
        con_nh, con_nw = content_img.shape[:2]
        
        con_x1 = con_cx - con_nw // 2
        con_x2 = con_x1 + con_nw
        con_y1 = con_cy - con_nh // 2
        con_y2 = con_y1 + con_nh

        whole_img[con_y1:con_y2, con_x1:con_x2, :] = content_img

        #----
        # Process style image

        in_style_w = out_in_w // 3
        in_style_h = (cre_rh - blank) // 2
        
        sty_ratio = 1. * in_style_h / style_h
        sty_rh = int(style_h * sty_ratio)
        sty_rw = int(style_w * sty_ratio)

        sty_w = out_in_w // 3

        style_cx = out_w - blank - in_content_w // 2
        style_cy = cre_y2 - (in_style_h) // 2

        if sty_rw > (in_style_w):
            sty_ratio = 1. * in_style_w / style_w
            sty_rh = int(style_h * sty_ratio)
            sty_rw = int(style_w * sty_ratio)

        style_img = cv2.resize(style_img, (sty_rw, sty_rh))
        style_nh, style_nw = style_img.shape[:2]
        
        style_x1 = style_cx - style_nw // 2
        style_x2 = style_x1 + style_nw
        style_y1 = style_cy - style_nh // 2
        style_y2 = style_y1 + style_nh

        whole_img[style_y1:style_y2, style_x1:style_x2, :] = style_img
        
    cv2.imwrite(args.out_path, whole_img)
    print("Output >>", args.out_path)

if __name__ == '__main__':
    main()
