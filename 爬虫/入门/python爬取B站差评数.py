# -*- coding: UTF-8 -*-
import json
import requests

def require_dislike (video_id) :
    """
    Get the number of dislike for a certain video.
    :para video_id: video_id (av number) for the target video
    :return dislike_no: the number of dislike for the video
    """
    URL_VIDinfo = "http://api.bilibili.com/archive_stat/stat?aid="
    PARAMS = {"aid": video_id}
    VID_info = requests.get (url=URL_VIDinfo,params=PARAMS),json ()
    dislike_no = VID_info ["data"]["dislike"]
    return dislike_no

def main () :
    video_dict = {"最新版i9MacBook Pro吃相太难看" : "27378490",
                  "Python虽慢、月薪两万" : "26863199",
                  "macOS完爆Windows和Linux" : "26350301"}
    for video_name,video_id in video_dict.items () :
        print (video_name + ":" + str (require_dislike (video_id)))

if __name__ == "__main__" :
    main ()