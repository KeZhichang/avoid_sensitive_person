# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:29:13 2018

@author: zhichang
"""

import face_recognition

#sensitive_person_image = ['BoXilai.jpg','CaiYingwen.png','ChenShuibian.png','Dalai.jpg','DengXiaoping.jpg','GuoBoxiong.jpg','HanZheng.jpg','HuJintao.jpg','HuChunhua.jpg'\
#                          ,'JiangZemin.jpg','LiDenghui.jpg','LiJia.jpg','LiKeqiang.jpg','LingJihua.jpg','LiuXiaobo.jpg','LiuZhigeng.jpg','LiXi.jpg'\
#                         ,'WangHuning.jpg','WangQingliang.jpg','WangQishan.jpg','WangYang.jpg','Wuerkaixi.jpg','XiJinping.jpg','XiZhongxun.jpg'\
#                        ,'XuCaihou.jpg','ZhaoLeji.jpg','ZhaoXiancong.jpg','ZhongShijian.jpg','ZhouYongkang.jpg','ZhuMingguo.jpg']

sensitive_image1 = face_recognition.load_image_file('image/BoXilai.jpg')
sensitive_image2 = face_recognition.load_image_file('image/CaiYingwen.png')
sensitive_image3 = face_recognition.load_image_file('image/ChenShuibian.png')
sensitive_image4 = face_recognition.load_image_file('image/Dalai.jpg')
sensitive_image5 = face_recognition.load_image_file('image/DengXiaoping.jpg')
sensitive_image6 = face_recognition.load_image_file('image/GuoBoxiong.jpg')
sensitive_image7 = face_recognition.load_image_file('image/HanZheng.jpg')
sensitive_image8 = face_recognition.load_image_file('image/HuJintao.jpg')
sensitive_image9 = face_recognition.load_image_file('image/HuChunhua.jpg')
sensitive_image10 = face_recognition.load_image_file('image/JiangZemin.jpg')
sensitive_image11 = face_recognition.load_image_file('image/LiDenghui.jpg')
sensitive_image12 = face_recognition.load_image_file('image/LiJia.jpg')
sensitive_image13 = face_recognition.load_image_file('image/LiKeqiang.jpg')
sensitive_image14 = face_recognition.load_image_file('image/LingJihua.jpg')
sensitive_image15 = face_recognition.load_image_file('image/LiuXiaobo.jpg')
sensitive_image16 = face_recognition.load_image_file('image/LiuZhigeng.jpg')
sensitive_image17 = face_recognition.load_image_file('image/LiXi.jpg')
sensitive_image18 = face_recognition.load_image_file('image/LiZezhong.jpg')
sensitive_image19 = face_recognition.load_image_file('image/LiZhanshu.jpg')
sensitive_image20 = face_recognition.load_image_file('image/MaoZedong.jpg')
sensitive_image21 = face_recognition.load_image_file('image/MaXingrui.jpg')
sensitive_image22 = face_recognition.load_image_file('image/QianFangli.jpg')
sensitive_image23 = face_recognition.load_image_file('image/Rebiya.jpg')
sensitive_image24 = face_recognition.load_image_file('image/SunZhengcai.jpg')
sensitive_image25 = face_recognition.load_image_file('image/SuRong.jpg')
sensitive_image26 = face_recognition.load_image_file('image/WangHuning.jpg')
sensitive_image27 = face_recognition.load_image_file('image/WangQingliang.jpg')
sensitive_image28 = face_recognition.load_image_file('image/WangQishan.jpg')
sensitive_image29 = face_recognition.load_image_file('image/Wuerkaixi.jpg')
sensitive_image30 = face_recognition.load_image_file('image/XiJinping.jpg')
sensitive_image31 = face_recognition.load_image_file('image/XiZhongxun.jpg')
sensitive_image32 = face_recognition.load_image_file('image/XuCaihou.jpg')
sensitive_image33 = face_recognition.load_image_file('image/ZhaoLeji.jpg')
sensitive_image34 = face_recognition.load_image_file('image/ZhaoXiancong.jpg')
sensitive_image35 = face_recognition.load_image_file('image/ZhongShijian.jpg')
sensitive_image36 = face_recognition.load_image_file('image/ZhouYongkang.png')
sensitive_image37 = face_recognition.load_image_file('image/ZhuMingguo.jpg')
sensitive_image38 = face_recognition.load_image_file('image/WangYang.jpg')

sensitive_image1_encoding = face_recognition.face_encodings(sensitive_image1)[0]
sensitive_image2_encoding = face_recognition.face_encodings(sensitive_image2)[0]
sensitive_image3_encoding = face_recognition.face_encodings(sensitive_image3)[0]
sensitive_image4_encoding = face_recognition.face_encodings(sensitive_image4)[0]
sensitive_image5_encoding = face_recognition.face_encodings(sensitive_image5)[0]
sensitive_image6_encoding = face_recognition.face_encodings(sensitive_image6)[0]
sensitive_image7_encoding = face_recognition.face_encodings(sensitive_image7)[0]
sensitive_image8_encoding = face_recognition.face_encodings(sensitive_image8)[0]
sensitive_image9_encoding = face_recognition.face_encodings(sensitive_image9)[0]
sensitive_image10_encoding = face_recognition.face_encodings(sensitive_image10)[0]
sensitive_image11_encoding = face_recognition.face_encodings(sensitive_image11)[0]
sensitive_image12_encoding = face_recognition.face_encodings(sensitive_image12)[0]
sensitive_image13_encoding = face_recognition.face_encodings(sensitive_image13)[0]
sensitive_image14_encoding = face_recognition.face_encodings(sensitive_image14)[0]
sensitive_image15_encoding = face_recognition.face_encodings(sensitive_image15)[0]
sensitive_image16_encoding = face_recognition.face_encodings(sensitive_image16)[0]
sensitive_image17_encoding = face_recognition.face_encodings(sensitive_image17)[0]
sensitive_image18_encoding = face_recognition.face_encodings(sensitive_image18)[0]
sensitive_image19_encoding = face_recognition.face_encodings(sensitive_image19)[0]
sensitive_image20_encoding = face_recognition.face_encodings(sensitive_image20)[0]
sensitive_image21_encoding = face_recognition.face_encodings(sensitive_image21)[0]
sensitive_image22_encoding = face_recognition.face_encodings(sensitive_image22)[0]
sensitive_image23_encoding = face_recognition.face_encodings(sensitive_image23)[0]
sensitive_image24_encoding = face_recognition.face_encodings(sensitive_image24)[0]
sensitive_image25_encoding = face_recognition.face_encodings(sensitive_image25)[0]
sensitive_image26_encoding = face_recognition.face_encodings(sensitive_image26)[0]
sensitive_image27_encoding = face_recognition.face_encodings(sensitive_image27)[0]
sensitive_image28_encoding = face_recognition.face_encodings(sensitive_image28)[0]
sensitive_image29_encoding = face_recognition.face_encodings(sensitive_image29)[0]
sensitive_image30_encoding = face_recognition.face_encodings(sensitive_image30)[0]
sensitive_image31_encoding = face_recognition.face_encodings(sensitive_image31)[0]
sensitive_image32_encoding = face_recognition.face_encodings(sensitive_image32)[0]
sensitive_image33_encoding = face_recognition.face_encodings(sensitive_image33)[0]
sensitive_image34_encoding = face_recognition.face_encodings(sensitive_image34)[0]
sensitive_image35_encoding = face_recognition.face_encodings(sensitive_image35)[0]
sensitive_image36_encoding = face_recognition.face_encodings(sensitive_image36)[0]
sensitive_image37_encoding = face_recognition.face_encodings(sensitive_image37)[0]
sensitive_image38_encoding = face_recognition.face_encodings(sensitive_image38)[0]

sensitive_image_encoding = [sensitive_image1_encoding,sensitive_image2_encoding,sensitive_image3_encoding,sensitive_image4_encoding\
                            ,sensitive_image5_encoding,sensitive_image6_encoding,sensitive_image7_encoding,sensitive_image8_encoding\
                            ,sensitive_image9_encoding,sensitive_image10_encoding,sensitive_image11_encoding,sensitive_image12_encoding\
                            ,sensitive_image13_encoding,sensitive_image14_encoding,sensitive_image15_encoding,sensitive_image16_encoding\
                            ,sensitive_image17_encoding,sensitive_image18_encoding,sensitive_image19_encoding,sensitive_image20_encoding\
                            ,sensitive_image21_encoding,sensitive_image22_encoding,sensitive_image23_encoding,sensitive_image24_encoding\
                            ,sensitive_image25_encoding,sensitive_image26_encoding,sensitive_image27_encoding,sensitive_image28_encoding\
                            ,sensitive_image29_encoding,sensitive_image30_encoding,sensitive_image31_encoding,sensitive_image32_encoding\
                            ,sensitive_image33_encoding,sensitive_image34_encoding,sensitive_image35_encoding,sensitive_image36_encoding\
                            ,sensitive_image37_encoding,sensitive_image38_encoding]