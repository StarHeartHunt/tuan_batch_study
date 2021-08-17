import sys

api_headers = {
    "Host": "tuanapi.12355.net",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://tuan.12355.net",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 Mobile Safari/537.36 MMWEBID/8628 MicroMessenger/7.0.21.1783(0x27001543) Process/tools WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64",
    "X-Requested-With": "com.tencent.mm",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://tuan.12355.net/wechat/view/YouthLearning/page.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

youthstudy_headers = {
    "Host": "youthstudy.12355.net",
    "Connection": "keep-alive",
    "Origin": "https://youthstudy.12355.net",
    "X-Litemall-Token": "",
    "X-Litemall-IdentiFication": "young",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 Mobile Safari/537.36 MMWEBID/8628 MicroMessenger/7.0.21.1783(0x27001543) Process/tools WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64",
    "Accept": "*/*",
    "X-Requested-With": "com.tencent.mm",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://youthstudy.12355.net/h5/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

get_sign_url = "https://tuanapi.12355.net/questionnaire/getYouthLearningUrl"
get_token_url = "https://youthstudy.12355.net/apih5/api/user/get"
get_chapter_url = "https://youthstudy.12355.net/apih5/api/young/chapter/new"
save_history_url = (
    "https://youthstudy.12355.net/apih5/api/young/course/chapter/saveHistory"
)

logger_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": (
                "<g>{time:MM-DD HH:mm:ss}</g> "
                "[<lvl>{level}</lvl>] "
                "<c><u>{name}</u></c> | "
                # "<c>{function}:{line}</c>| "
                "{message}"
            ),
        }
    ]
}
